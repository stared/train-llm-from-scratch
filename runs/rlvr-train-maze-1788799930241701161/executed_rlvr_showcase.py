# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Minute-scale RLVR comparisons, also runnable on an ordinary local GPU.

Fresh LoRA; on-policy REINFORCE with a leave-one-out baseline. No SFT targets,
teacher model, best-of-N selection, KL penalty, or reused/off-policy rollouts.
"""
import argparse
import gc
import hashlib
import json
from pathlib import Path
import random
import time

from rlvr_tasks import TASKS, MAX_TOKENS, make_data, check

ROOT = Path(__file__).resolve().parent


def save(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2))


def run(output, task='six_words', stage='train', model_key='qwen3-0.6b',
        max_seconds=300, steps=160, lr=2e-4, seed=42, device='cuda'):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText, GenerationConfig
    from peft import LoraConfig, get_peft_model, PeftModel

    if task not in TASKS or stage not in ('screen', 'train'):
        raise ValueError('Unknown task/stage')
    if not 60 <= max_seconds <= 600 or not 1 <= steps <= 400 or not 1e-6 <= lr <= 5e-4:
        raise ValueError('Bounded runs: 60–600 seconds, 1–400 steps, LR 1e-6–5e-4')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    spec = json.loads((ROOT / 'models.json').read_text())[model_key]
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
        model = get_peft_model(model, LoraConfig(r=16, lora_alpha=32, lora_dropout=0.,
                    target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj'],
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
        advantage = (rewards - (rewards.sum(1, keepdim=True) - rewards) / 3).reshape(-1)
        record = dict(step=step, ids=[r['id'] for r in rows], texts=texts, scores=scores,
                      advantages=advantage.tolist(), updated=False)
        # Every group has ONE on-policy optimizer update, with 2-sequence
        # microbatches. No length normalization of the sequence log probability.
        if advantage.abs().max().item() > 1e-7:
            attention = torch.cat([prefix_attention, mask.long()], dim=1)
            position_ids = (attention.cumsum(-1) - 1).clamp(min=0)
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
        elapsed = time.monotonic() - training_start
        if step % 10 == 0:
            print(f'{task} step={step} updates={updates} mean_reward={rewards.mean().item():.3f} seconds={elapsed:.1f}', flush=True)
            save(out / 'rollouts.json', history)
        if elapsed >= max_seconds:
            break
    training_seconds = time.monotonic() - training_start
    save(out / 'rollouts.json', history)
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
        algorithm='on-policy REINFORCE, leave-one-out baseline, beta=0, sequence-summed log probability',
        training_data='256 synthetic prompts with programmatic rewards; no SFT; no target tokens in loss',
        data_sha256=data_hash, seed=seed, learning_rate=lr, lora_rank=16, lora_alpha=32,
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
    p.add_argument('--model', default='qwen3-0.6b')
    p.add_argument('--max-seconds', type=int, default=300)
    p.add_argument('--steps', type=int, default=160)
    p.add_argument('--lr', type=float, default=2e-4)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], default='cuda')
    a = p.parse_args()
    run(a.output, a.task, a.stage, a.model, a.max_seconds, a.steps, a.lr, a.seed, a.device)
