# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Tiny RLVR: on-policy REINFORCE with a leave-one-out baseline, no KL.

Starts from the saved LFM2.5-350M Polish SFT adapter. One gradient update per
fresh rollout group. No answer tokens are supplied to the training loss.
"""
import argparse
import gc
import json
from pathlib import Path
import re
import time


def reward(text, a, b):
    text = text.strip()
    return float(bool(re.fullmatch(r'0|[1-9][0-9]{0,5}', text)) and text == str(a + b))


def advantages(rewards):
    if len(rewards) < 2:
        raise ValueError('Leave-one-out needs at least two samples')
    return [r - (sum(rewards) - r) / (len(rewards) - 1) for r in rewards]


def run(sft_dir, output, groups=12, rollouts=4, device='cpu', max_seconds=90):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
    from peft import PeftModel

    if not 1 <= groups <= 32 or not 2 <= rollouts <= 8 or not 1 <= max_seconds <= 180:
        raise ValueError('Limits: 1–32 groups, 2–8 rollouts, 1–180 training seconds')
    source = Path(sft_dir)
    manifest = json.loads((source / 'result.json').read_text())
    if manifest['model'] != 'lfm2.5-350m' or manifest['task'] != 'polish':
        raise ValueError('Use the LFM2.5-350M Polish SFT run as the warm start')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    spec = manifest['model_spec']
    started = time.monotonic()
    torch.manual_seed(123)
    if device == 'cpu':
        torch.set_num_threads(4)
    dtype = torch.bfloat16 if device == 'cuda' and torch.cuda.is_bf16_supported() else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(source / 'tokenizer')

    def load(adapter, trainable=False):
        base = AutoModelForCausalLM.from_pretrained(spec['id'], revision=spec['revision'],
                                                   dtype=dtype, attn_implementation='sdpa').to(device)
        return PeftModel.from_pretrained(base, adapter, is_trainable=trainable)

    model = load(source / 'adapter', True)
    # eval() disables dropout while still allowing gradients. Rollouts and loss
    # therefore use the same policy distribution.
    model.eval()
    train_pairs = [(201 + (i * 37) % 300, 11 + (i * 19) % 90) for i in range(16)]
    test_pairs = [(601 + i * 23, 13 + i * 7) for i in range(8)]

    def ids_for(a, b):
        prompt = ('Odpowiedz tylko liczbą, bez wyjaśnienia.\n'
                  f'Ola ma {a} monet i dostaje jeszcze {b}. Ile ma razem?')
        return tokenizer.apply_chat_template([{'role': 'user', 'content': prompt}],
                    tokenize=True, add_generation_prompt=True, return_dict=False, enable_thinking=False)

    def generate(a, b, sample=False):
        prefix = torch.tensor([ids_for(a, b)], device=device)
        config = GenerationConfig(max_new_tokens=12, do_sample=sample,
                    num_return_sequences=rollouts if sample else 1,
                    eos_token_id=tokenizer.eos_token_id, pad_token_id=tokenizer.pad_token_id)
        if sample:
            # No top-k/top-p/temperature transformation: exact on-policy sampling.
            config.temperature, config.top_k, config.top_p = 1., 0, 1.
        with torch.no_grad():
            seq = model.generate(input_ids=prefix, attention_mask=torch.ones_like(prefix),
                                 generation_config=config)
        return seq, prefix.shape[1]

    def evaluate(name):
        rows = []
        for a, b in test_pairs:
            seq, start = generate(a, b)
            text = tokenizer.decode(seq[0, start:], skip_special_tokens=True)
            rows.append(dict(a=a, b=b, answer=a+b, prediction=text, reward=reward(text, a, b)))
        (out / f'{name}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
        return sum(r['reward'] for r in rows) / len(rows)

    before = evaluate('before')
    params = [p for p in model.parameters() if p.requires_grad]
    initial = [p.detach().cpu().clone() for p in params]
    optimizer = torch.optim.AdamW(params, lr=1e-5, weight_decay=0.)
    history = []
    training_start = time.monotonic()
    updates = 0
    for group in range(groups):
        a, b = train_pairs[group % len(train_pairs)]
        seq, start = generate(a, b, sample=True)
        completion = seq[:, start:]
        texts = tokenizer.batch_decode(completion, skip_special_tokens=True)
        rewards = [reward(t, a, b) for t in texts]
        adv = torch.tensor(advantages(rewards), device=device)
        record = dict(group=group, a=a, b=b, completions=texts, rewards=rewards,
                      advantages=adv.tolist(), updated=False)
        if adv.abs().sum().item() > 0:
            # Include first EOS but mask padding / everything after it.
            eos = completion.eq(tokenizer.eos_token_id)
            mask = (eos.cumsum(dim=1) - eos.long()).eq(0)
            attention = torch.cat([torch.ones_like(seq[:, :start]), mask.long()], dim=1)
            optimizer.zero_grad(set_to_none=True)
            logits = model(input_ids=seq, attention_mask=attention, use_cache=False).logits
            # Only generated tokens carry the policy gradient; prompt is masked.
            logp = logits[:, start-1:-1, :].float().log_softmax(dim=-1)
            selected = logp.gather(-1, completion.unsqueeze(-1)).squeeze(-1)
            sequence_logp = (selected * mask).sum(dim=1)
            loss = -(adv.detach() * sequence_logp).mean()
            if not torch.isfinite(loss):
                raise RuntimeError('Non-finite policy loss')
            loss.backward()
            torch.nn.utils.clip_grad_norm_(params, 1.)
            optimizer.step()
            updates += 1
            record.update(updated=True, loss=loss.item())
            del logits, logp, selected, sequence_logp, loss
        history.append(record)
        print(f'group={group} rewards={rewards} update={record["updated"]}', flush=True)
        if time.monotonic() - training_start >= max_seconds:
            break
    train_seconds = time.monotonic() - training_start
    changed = any(not torch.equal(a, b.detach().cpu()) for a, b in zip(initial, params))
    model.save_pretrained(out / 'adapter')
    tokenizer.save_pretrained(out / 'tokenizer')
    after = evaluate('after')
    del optimizer, params, initial, model
    gc.collect()
    if device == 'cuda':
        torch.cuda.empty_cache()
    model = load(out / 'adapter')
    model.eval()
    reloaded = evaluate('reloaded')
    same = (out / 'after.json').read_text() == (out / 'reloaded.json').read_text()
    if not same:
        raise RuntimeError('Reload predictions differ')
    result = dict(algorithm='on-policy REINFORCE with leave-one-out baseline; beta=0',
                  model_spec=spec, sft_source=str(source), seed=123, learning_rate=1e-5,
                  groups=len(history), rollouts=rollouts, updates=updates, adapter_changed=changed,
                  before=before, after=after, reloaded=reloaded, reload_matches=same,
                  training_seconds=train_seconds, total_seconds=time.monotonic()-started,
                  peak_vram_gb=torch.cuda.max_memory_allocated()/1e9 if device == 'cuda' else None,
                  diagnostic='nonzero reward signal' if updates else 'all groups had uniform rewards; no learning update')
    (out / 'rl_result.json').write_text(json.dumps(result, indent=2))
    (out / 'rollouts.json').write_text(json.dumps(history, ensure_ascii=False, indent=2))
    print(json.dumps(result, indent=2), flush=True)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sft-dir', required=True)
    p.add_argument('--output', default='runs/rlvr-local')
    p.add_argument('--groups', type=int, default=12)
    p.add_argument('--rollouts', type=int, default=4)
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], default='cpu')
    p.add_argument('--max-seconds', type=int, default=90)
    a = p.parse_args()
    run(a.sft_dir, a.output, a.groups, a.rollouts, a.device, a.max_seconds)
