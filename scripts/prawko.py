# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""LLM robi prawko: answer-only SFT versus a three-action RLVR bandit.

Ordinary uv script; identical constrained A/B/C prediction for all evaluations.
No chain of thought, teacher model, or generated rationale is used.
"""
import argparse
import gc
import hashlib
import json
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parents[1]
LETTERS = 'ABC'


def save(path, obj):
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2))


def question(row, order=(0, 1, 2)):
    prompt = ('Rozwiąż pytanie egzaminacyjne na prawo jazdy w Polsce. '
              'Wybierz jedną poprawną odpowiedź. Odpowiedz wyłącznie literą A, B albo C.\n\n'
              + row['question'] + '\n' + '\n'.join(f'{LETTERS[i]}. {row["options"][j]}' for i, j in enumerate(order)))
    return prompt, order.index(row['answer'])


def run(output, method='screen', model_key='qwen3.5-0.8b', max_seconds=180,
        epochs=5, lr=5e-5, seed=42, device='cuda'):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText
    from peft import LoraConfig, get_peft_model, get_peft_model_state_dict, set_peft_model_state_dict, PeftModel
    if method not in ('screen', 'sft', 'rlvr') or not 60 <= max_seconds <= 720 or not 1 <= epochs <= 40:
        raise ValueError('Use screen/sft/rlvr, 60–720 seconds, 1–40 epochs')
    if not 1e-6 <= lr <= 5e-4:
        raise ValueError('Learning rate out of bounds')
    started = time.monotonic()
    if device == 'cuda':
        torch.cuda.reset_peak_memory_stats()
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    data_path = ROOT / 'datasets/prawko-v2/data.json'
    data = json.loads(data_path.read_text())
    save(out / 'data.json', data)
    spec = json.loads((ROOT / 'config/models.json').read_text())[model_key]
    save(out / 'model_spec.json', spec)
    tokenizer = AutoTokenizer.from_pretrained(spec['id'], revision=spec['revision'])
    tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    ids = [tokenizer.encode(x, add_special_tokens=False) for x in LETTERS]
    if any(len(x) != 1 for x in ids):
        raise ValueError('This experiment needs single-token A/B/C labels')
    label_ids = torch.tensor([x[0] for x in ids], device=device)
    cls = AutoModelForImageTextToText if spec['multimodal'] else AutoModelForCausalLM
    def load():
        return cls.from_pretrained(spec['id'], revision=spec['revision'],
            dtype=torch.bfloat16 if device == 'cuda' else torch.float32,
            attn_implementation='sdpa').to(device)
    torch.manual_seed(seed)
    model = load()
    if method != 'screen':
        targets = [name for name, module in model.named_modules() if isinstance(module, torch.nn.Linear)
                   and name.rsplit('.', 1)[-1] in ('q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj')
                   and 'visual' not in name and 'vision' not in name]
        model = get_peft_model(model, LoraConfig(r=16, lora_alpha=32, lora_dropout=0., target_modules=targets, task_type='CAUSAL_LM'))
    model.eval()

    def encode(rows, orders):
        pairs = [question(r, o) for r, o in zip(rows, orders)]
        prompts = [tokenizer.apply_chat_template([{'role': 'user', 'content': p}], tokenize=False,
                   add_generation_prompt=True, enable_thinking=False) for p, _ in pairs]
        inputs = tokenizer(prompts, padding=True, add_special_tokens=False, return_tensors='pt').to(device)
        if inputs.input_ids.shape[1] > 768:
            raise ValueError('Unexpected long prompt; refusing silent truncation')
        return inputs, torch.tensor([a for _, a in pairs], device=device)

    def logits(inputs):
        # Only project the final hidden state: avoids full prompt-by-vocabulary logits.
        return model(**inputs, use_cache=False, logits_to_keep=1).logits[:, -1, :].float()

    def evaluate(name, rows, rotated=False):
        records = []
        for offset in range(0, len(rows), 8):
            batch = rows[offset:offset+8]
            orders = [(1, 2, 0) if rotated else (0, 1, 2) for _ in batch]
            inputs, answers = encode(batch, orders)
            with torch.no_grad():
                full = logits(inputs)
                probabilities = full[:, label_ids].softmax(-1)
                mass = full.softmax(-1)[:, label_ids].sum(-1)
            for row, order, probs, answer, m in zip(batch, orders, probabilities.tolist(), answers.tolist(), mass.tolist()):
                pred = max(range(3), key=lambda i: probs[i])
                records.append(dict(id=row['id'], question=row['question'],
                    options=[row['options'][j] for j in order], answer=LETTERS[answer], prediction=LETTERS[pred],
                    correct=pred == answer, probabilities=probs, unconstrained_ABC_mass=m))
        save(out / f'{name}.json', records)
        metric = dict(n=len(records), correct=sum(r['correct'] for r in records),
            accuracy=sum(r['correct'] for r in records)/len(records),
            mean_correct_probability=sum(r['probabilities'][LETTERS.index(r['answer'])] for r in records)/len(records))
        print(name, json.dumps(metric), flush=True)
        return metric

    before = {k: evaluate('before_' + k, data[k]) for k in ('train', 'dev', 'test')}
    before['test_rotated'] = evaluate('before_test_rotated', data['test'], True)
    result = dict(method=method, model_spec=spec, seed=seed, data_sha256=hashlib.sha256(data_path.read_bytes()).hexdigest(),
        decoding='Argmax over A/B/C next-token logits; no reasoning; nonthinking chat template',
        training_data='100 official category-B text-only three-choice questions; separate 25 dev and 40 test', before=before)
    if method != 'screen':
        params = [p for p in model.parameters() if p.requires_grad]
        optimizer = torch.optim.AdamW(params, lr=lr, weight_decay=0.)
        def state():
            return {k: v.detach().cpu().clone() for k, v in get_peft_model_state_dict(model).items()}
        initial = state()
        best_state, best_epoch = initial, 0
        best_score = (before['dev']['correct'], before['dev']['mean_correct_probability'])
        rng = random.Random(seed)
        torch.manual_seed(seed)
        history, checkpoints = [], []
        train_started = time.monotonic()
        stop = False
        for epoch in range(epochs):
            order = list(range(len(data['train'])))
            rng.shuffle(order)
            for offset in range(0, len(order), 4):
                rows = [data['train'][i] for i in order[offset:offset+4]]
                permutations = [rng.sample(range(3), 3) for _ in rows]
                inputs, answers = encode(rows, permutations)
                optimizer.zero_grad(set_to_none=True)
                full = logits(inputs)
                logp = full[:, label_ids].log_softmax(-1)
                record = dict(epoch=epoch+1, ids=[r['id'] for r in rows], orders=permutations, answers=answers.tolist())
                if method == 'sft':
                    # Ordinary next-token cross entropy across the FULL vocabulary.
                    loss = torch.nn.functional.cross_entropy(full, label_ids[answers])
                else:
                    # Four independent on-policy A/B/C draws per question, one update.
                    sampled = torch.multinomial(logp.detach().exp(), 4, replacement=True)
                    rewards = sampled.eq(answers[:, None]).float()
                    advantages = rewards - (rewards.sum(-1, keepdim=True) - rewards)/3
                    with torch.no_grad(), model.disable_adapter():
                        reference = logits(inputs)[:, label_ids].log_softmax(-1)
                    kl = (logp.exp() * (logp - reference)).sum(-1).mean()
                    loss = -(logp.gather(-1, sampled) * advantages).mean() + .01 * kl
                    record.update(samples=sampled.tolist(), rewards=rewards.tolist(), advantages=advantages.tolist(), kl=kl.item())
                if not torch.isfinite(loss):
                    raise RuntimeError('Nonfinite loss')
                loss.backward()
                grad = torch.nn.utils.clip_grad_norm_(params, 1.)
                optimizer.step()
                record.update(loss=loss.item(), gradient_norm=grad.item())
                history.append(record)
                del full, logp, loss
                if time.monotonic() - train_started >= max_seconds:
                    stop = True
                    break
            metric = evaluate(f'dev_epoch_{epoch+1}', data['dev'])
            checkpoints.append(dict(epoch=epoch+1, steps=len(history),
                                    elapsed_seconds=time.monotonic()-train_started, **metric))
            score = (metric['correct'], metric['mean_correct_probability'])
            if score > best_score:
                best_score, best_state, best_epoch = score, state(), epoch+1
            print('epoch', epoch+1, 'seconds', time.monotonic()-train_started, flush=True)
            save(out / 'history.json', history)
            save(out / 'checkpoints.json', checkpoints)
            if stop:
                break
        train_seconds = time.monotonic() - train_started
        # The final checkpoint is reported separately, never used to select by test.
        # Selection above is already complete and only uses development data.
        model.save_pretrained(out / 'final_adapter')
        final = {k: evaluate('final_' + k, data[k]) for k in ('train', 'dev', 'test')}
        final['test_rotated'] = evaluate('final_test_rotated', data['test'], True)
        set_peft_model_state_dict(model, best_state)
        changed = any(not torch.equal(initial[k], best_state[k]) for k in initial)
        model.save_pretrained(out / 'adapter')
        tokenizer.save_pretrained(out / 'tokenizer')
        save(out / 'history.json', history)
        save(out / 'checkpoints.json', checkpoints)
        after = {k: evaluate('after_' + k, data[k]) for k in ('train', 'dev', 'test')}
        after['test_rotated'] = evaluate('after_test_rotated', data['test'], True)
        del model, optimizer, params, best_state, initial
        gc.collect()
        if device == 'cuda':
            torch.cuda.empty_cache()
        model = PeftModel.from_pretrained(load(), out / 'adapter')
        model.eval()
        evaluate('reload', data['test'][:8])
        a = json.loads((out / 'after_test.json').read_text())[:8]
        b = json.loads((out / 'reload.json').read_text())
        matched = all(x['prediction'] == y['prediction'] for x, y in zip(a, b))
        if not matched:
            raise RuntimeError('Reload predictions differ')
        result.update(after=after, final=final, training_seconds=train_seconds, steps=len(history),
            selected_epoch=best_epoch, selected_steps=next((c['steps'] for c in checkpoints if c['epoch']==best_epoch),0),
            lora_rank=16, lora_alpha=32, learning_rate=lr, epochs_requested=epochs, max_seconds=max_seconds,
            beta=.01 if method=='rlvr' else None, adapter_changed=changed, reload_matches=matched,
            algorithm='Full-vocabulary next-token SFT' if method=='sft' else 'On-policy categorical REINFORCE/RLOO, four samples, exact three-action reference KL')
    result['total_seconds'] = time.monotonic() - started
    result['peak_vram_gb'] = torch.cuda.max_memory_allocated()/1e9 if device=='cuda' else None
    save(out / 'result.json', result)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', default='runs/prawko-local')
    p.add_argument('--method', choices=['screen', 'sft', 'rlvr'], default='screen')
    p.add_argument('--model', default='qwen3.5-0.8b')
    p.add_argument('--max-seconds', type=int, default=180)
    p.add_argument('--epochs', type=int, default=5)
    p.add_argument('--lr', type=float, default=5e-5)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], default='cpu')
    a = p.parse_args()
    run(a.output, a.method, a.model, a.max_seconds, a.epochs, a.lr, a.seed, a.device)
