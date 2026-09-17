# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Minute-scale RLVR comparisons, also runnable on an ordinary local GPU.

Fresh LoRA; on-policy REINFORCE with a leave-one-out baseline. No SFT targets,
teacher model, best-of-N selection, or reused/off-policy rollouts. Optional
reference-policy regularization and development-only checkpoint selection.
"""
import argparse
import gc
import hashlib
import json
from pathlib import Path
import random
import time

from rlvr_tasks import TASKS, MAX_TOKENS, make_data, check

ROOT = Path(__file__).resolve().parents[1]


def save(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2))


def run(output, task='six_words', stage='train', model_key='qwen3.5-4b',
        max_seconds=600, steps=160, lr=5e-5, seed=42, device='cuda', beta=.01, dev_interval=20):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText, GenerationConfig
    from peft import LoraConfig, get_peft_model, PeftModel, get_peft_model_state_dict, set_peft_model_state_dict

    if task not in TASKS or stage not in ('screen', 'train'):
        raise ValueError('Unknown task/stage')
    if not 60 <= max_seconds <= 600 or not 1 <= steps <= 400 or not 1e-6 <= lr <= 5e-4:
        raise ValueError('Bounded runs: 60–600 seconds, 1–400 steps, LR 1e-6–5e-4')
    if not 0 <= beta <= .1 or dev_interval not in (0, 20, 40):
        raise ValueError('beta 0–0.1; dev_interval 0, 20 or 40')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    spec = json.loads((ROOT / 'config/models.json').read_text())[model_key]
    save(out / 'model_spec.json', spec)
    data = make_data(task)
    save(out / 'data.json', data)
    data_hash = hashlib.sha256((out / 'data.json').read_bytes()).hexdigest()
    tokenizer = AutoTokenizer.from_pretrained(spec['id'], revision=spec['revision'])
    tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    dtype = torch.bfloat16 if device == 'cuda' else torch.float32
    cls = AutoModelForImageTextToText if spec['multimodal'] else AutoModelForCausalLM

    def load_base():
        return cls.from_pretrained(spec['id'], revision=spec['revision'], dtype=dtype,
                                  attn_implementation='sdpa').to(device)

    torch.manual_seed(seed)
    model = load_base()
    if stage == 'train':
        targets = [name for name, module in model.named_modules()
                   if isinstance(module, torch.nn.Linear)
                   and name.rsplit('.', 1)[-1] in ('q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj')
                   and 'visual' not in name and 'vision' not in name]
        model = get_peft_model(model, LoraConfig(r=16, lora_alpha=32, lora_dropout=0.,
                    target_modules=targets,
                    task_type='CAUSAL_LM'))
    model.eval()  # gradients still enabled; dropout disabled in loss AND rollout

    def generate(rows, sample=False, copies=1):
        prompts = [tokenizer.apply_chat_template([{'role': 'user', 'content': row['prompt']}],
                    tokenize=False, add_generation_prompt=True, enable_thinking=False)
                   for row in rows for _ in range(copies)]
        inputs = tokenizer(prompts, padding=True, add_special_tokens=False, return_tensors='pt').to(device)
        config = GenerationConfig(max_new_tokens=MAX_TOKENS[task], do_sample=sample,
                    pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id)
        if sample:
            config.temperature, config.top_k, config.top_p = 1., 0, 1.
        with torch.no_grad():
            seq = model.generate(**inputs, generation_config=config)
        start = inputs.input_ids.shape[1]
        completion = seq[:, start:]
        eos = completion.eq(tokenizer.eos_token_id)
        mask = (eos.cumsum(dim=1) - eos.long()).eq(0)
        texts = tokenizer.batch_decode(completion, skip_special_tokens=True)
        return seq, inputs.attention_mask, start, mask, texts

    def evaluate(name, rows, sample=False, copies=1):
        torch.manual_seed(2026)
        results = []
        for start in range(0, len(rows), max(1, 8 // copies)):
            batch = rows[start:start + max(1, 8 // copies)]
            seq, _, offset, mask, texts = generate(batch, sample, copies)
            for i, (row, text) in enumerate(zip([r for r in batch for _ in range(copies)], texts)):
                results.append(dict(id=row['id'], prompt=row['prompt'], text=text,
                    terminated=bool(seq[i, offset:][mask[i]].eq(tokenizer.eos_token_id).any()),
                    **check(task, row, text)))
        save(out / f'{name}.json', results)
        score = dict(n=len(results), successes=sum(r['success'] for r in results),
                     mean_reward=sum(r['reward'] for r in results) / len(results),
                     terminated=sum(r['terminated'] for r in results))
        print(name, json.dumps(score), flush=True)
        return score

    if stage == 'screen':
        metrics = evaluate('screen', data['train'][:8], sample=True, copies=4)
        result = dict(stage=stage, task=task, model_spec=spec, metrics=metrics, data_sha256=data_hash,
                      total_seconds=time.monotonic() - started)
        save(out / 'result.json', result)
        return result

    before = {split: evaluate(f'before_{split}', data[split]) for split in ('dev', 'test')}
    before['sampled_dev'] = evaluate('before_sampled_dev', data['dev'][:12], True, 2)
    best_score = (before['dev']['successes'], before['dev']['mean_reward'])
    best_state = {k: v.detach().cpu().clone() for k, v in get_peft_model_state_dict(model).items()} if dev_interval else None
    best_step = 0
    checkpoints = []
    params = [p for p in model.parameters() if p.requires_grad]
    initial = [p.detach().cpu().clone() for p in params]
    optimizer = torch.optim.AdamW(params, lr=lr, weight_decay=0.)
    rng = random.Random(seed)
    order = list(range(len(data['train'])))
    rng.shuffle(order)
    cursor = 0
    torch.manual_seed(seed)
    training_start = time.monotonic()
    history, updates = [], 0
    for step in range(steps):
        if cursor + 2 > len(order):
            rng.shuffle(order)
            cursor = 0
        rows = [data['train'][i] for i in order[cursor:cursor+2]]
        cursor += 2
        seq, prefix_attention, start, mask, texts = generate(rows, True, 4)
        completions = seq[:, start:]
        scores = [check(task, row, text) for row, text in zip([r for r in rows for _ in range(4)], texts)]
        rewards = torch.tensor([s['reward'] for s in scores], device=device).reshape(2, 4)
        attention = torch.cat([prefix_attention, mask.long()], dim=1)
        position_ids = (attention.cumsum(-1) - 1).clamp(min=0)
        kl = torch.zeros(len(seq), device=device)
        if beta:
            # Monte Carlo sequence log(pi / pi_reference). Fold into rewards,
            # detached, as in RLOO. The reference is the frozen original model.
            with torch.no_grad():
                for i in range(0, len(seq), 2):
                    kwargs = dict(input_ids=seq[i:i+2], attention_mask=attention[i:i+2],
                                  position_ids=position_ids[i:i+2], use_cache=False)
                    logits = model(**kwargs).logits[:, start-1:-1, :].float()
                    current = logits.log_softmax(-1).gather(-1, completions[i:i+2, :, None]).squeeze(-1)
                    del logits
                    with model.disable_adapter():
                        logits = model(**kwargs).logits[:, start-1:-1, :].float()
                        reference = logits.log_softmax(-1).gather(-1, completions[i:i+2, :, None]).squeeze(-1)
                    kl[i:i+2] = ((current-reference) * mask[i:i+2]).sum(-1)
                    del logits, current, reference
        adjusted = rewards - beta * kl.reshape(2, 4)
        advantage = (adjusted - (adjusted.sum(1, keepdim=True) - adjusted) / 3).reshape(-1)
        record = dict(step=step, ids=[r['id'] for r in rows], texts=texts, scores=scores,
                      advantages=advantage.tolist(), sampled_sequence_kl=kl.tolist(), updated=False)
        # Every group has ONE on-policy optimizer update, with 2-sequence
        # microbatches. No length normalization of the sequence log probability.
        if advantage.abs().max().item() > 1e-7:
            optimizer.zero_grad(set_to_none=True)
            loss_value = 0.
            for i in range(0, len(seq), 2):
                logits = model(input_ids=seq[i:i+2], attention_mask=attention[i:i+2],
                               position_ids=position_ids[i:i+2], use_cache=False).logits[:, start-1:-1, :].float()
                logp = logits.log_softmax(-1).gather(-1, completions[i:i+2, :, None]).squeeze(-1)
                sequence_logp = (logp * mask[i:i+2]).sum(-1)
                loss = -(advantage[i:i+2].detach() * sequence_logp).sum() / len(seq)
                if not torch.isfinite(loss):
                    raise RuntimeError('Nonfinite policy gradient')
                loss.backward()
                loss_value += loss.item()
                del logits, logp, sequence_logp, loss
            grad = torch.nn.utils.clip_grad_norm_(params, 1.)
            optimizer.step()
            updates += 1
            record.update(updated=True, loss=loss_value, gradient_norm=grad.item())
        history.append(record)
        if dev_interval and (step + 1) % dev_interval == 0:
            # Preserve rollout RNG: evaluation must not reset future exploration.
            cpu_rng = torch.random.get_rng_state()
            gpu_rng = torch.cuda.get_rng_state() if device == 'cuda' else None
            metric = evaluate(f'checkpoint_dev_{step+1}', data['dev'])
            torch.random.set_rng_state(cpu_rng)
            if gpu_rng is not None:
                torch.cuda.set_rng_state(gpu_rng)
            score = (metric['successes'], metric['mean_reward'])
            checkpoints.append(dict(step=step+1, **metric))
            if score > best_score:
                best_score, best_step = score, step+1
                best_state = {k: v.detach().cpu().clone() for k, v in get_peft_model_state_dict(model).items()}
        elapsed = time.monotonic() - training_start
        if step % 10 == 0:
            print(f'{task} step={step} updates={updates} mean_reward={rewards.mean().item():.3f} seconds={elapsed:.1f}', flush=True)
            save(out / 'rollouts.json', history)
        if elapsed >= max_seconds:
            break
    training_seconds = time.monotonic() - training_start
    save(out / 'rollouts.json', history)
    if dev_interval:
        # Also consider the final batch if a wall-clock cutoff landed between checks.
        metric = evaluate('checkpoint_dev_final', data['dev'])
        score = (metric['successes'], metric['mean_reward'])
        if score > best_score:
            best_score, best_step = score, len(history)
            best_state = {k: v.detach().cpu().clone() for k, v in get_peft_model_state_dict(model).items()}
        set_peft_model_state_dict(model, best_state)
        save(out / 'checkpoint_selection.json', dict(best_step=best_step, best_score=best_score, checkpoints=checkpoints, final=metric))
    changed = any(not torch.equal(a, b.detach().cpu()) for a, b in zip(initial, params))
    model.save_pretrained(out / 'adapter')
    tokenizer.save_pretrained(out / 'tokenizer')
    after = {split: evaluate(f'after_{split}', data[split]) for split in ('dev', 'test')}
    after['sampled_dev'] = evaluate('after_sampled_dev', data['dev'][:12], True, 2)
    del model, optimizer, params, initial
    gc.collect()
    if device == 'cuda':
        torch.cuda.empty_cache()
    model = PeftModel.from_pretrained(load_base(), out / 'adapter')
    model.eval()
    evaluate('reload', data['test'][:8])
    reload_matches = json.loads((out / 'reload.json').read_text()) == json.loads((out / 'after_test.json').read_text())[:8]
    if not reload_matches:
        raise RuntimeError('Reload differs from saved model predictions')
    result = dict(stage=stage, task=task, model=model_key, model_spec=spec,
        algorithm='on-policy REINFORCE, leave-one-out baseline, sequence-summed log probability',
        training_data='Pool of 256 synthetic prompts with programmatic rewards; no SFT; no target tokens in loss',
        unique_training_prompts=len({i for row in history for i in row['ids']}),
        training_prompt_presentations=sum(len(row['ids']) for row in history),
        selected_unique_training_prompts=len({i for row in history[:best_step if dev_interval else len(history)] for i in row['ids']}),
        data_sha256=data_hash, seed=seed, learning_rate=lr, lora_rank=16, lora_alpha=32, beta=beta,
        dev_interval=dev_interval, selected_step=best_step if dev_interval else len(history),
        prompts_per_step=2, samples_per_prompt=4, microbatch=2, max_new_tokens=MAX_TOKENS[task],
        steps=len(history), updates=updates, adapter_changed=changed, reload_matches=reload_matches,
        before=before, after=after, training_seconds=training_seconds,
        total_seconds=time.monotonic()-started,
        peak_vram_gb=torch.cuda.max_memory_allocated()/1e9 if device == 'cuda' else None)
    save(out / 'result.json', result)
    print(json.dumps(result), flush=True)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', default='runs/rlvr-showcase-local')
    p.add_argument('--task', choices=TASKS, default='six_words')
    p.add_argument('--stage', choices=['screen', 'train'], default='train')
    p.add_argument('--model', default='qwen3.5-4b')
    p.add_argument('--max-seconds', type=int, default=600)
    p.add_argument('--steps', type=int, default=160)
    p.add_argument('--lr', type=float, default=5e-5)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--beta', type=float, default=.01)
    p.add_argument('--dev-interval', type=int, default=20)
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], default='cuda')
    a = p.parse_args()
    run(a.output, a.task, a.stage, a.model, a.max_seconds, a.steps, a.lr, a.seed, a.device, a.beta, a.dev_interval)
