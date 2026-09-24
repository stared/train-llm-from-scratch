# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Ordinary Python LoRA SFT, baseline evaluation, and saved-adapter reload.

No TRL, notebook, agent, quantization kernel, or external dataset is required.
"""
import argparse
import gc
import hashlib
import importlib.metadata
import json
from pathlib import Path
import random
import time

from examples import TASKS, dataset, score

ROOT = Path(__file__).resolve().parents[1]
MODELS = json.loads((ROOT / 'scripts/models.json').read_text(encoding='utf-8'))


def run(model_key='qwen3-0.6b', task='routing', steps=40, eval_size=8,
        output='runs/local', device='cpu', max_seconds=180, learning_rate=5e-4):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText
    from peft import LoraConfig, get_peft_model, PeftModel

    if not 1 <= steps <= 200 or not 1 <= eval_size <= 64 or not 1 <= max_seconds <= 600:
        raise ValueError('Limits: 1–200 steps, 1–64 evaluation examples, 1–600 training seconds')
    started = time.monotonic()
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    spec = MODELS[model_key]
    torch.manual_seed(42)
    random.seed(42)
    if device == 'cpu':
        torch.set_num_threads(4)
    dtype = torch.bfloat16 if device == 'cuda' and torch.cuda.is_bf16_supported() else torch.float32
    loader = AutoModelForImageTextToText if spec['multimodal'] else AutoModelForCausalLM
    tokenizer = AutoTokenizer.from_pretrained(spec['id'], revision=spec['revision'])
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    stop_token_id = tokenizer.eos_token_id
    if 'end_of_turn_token' in spec:
        token = spec['end_of_turn_token']
        if token not in tokenizer.get_vocab():
            raise ValueError(f'Missing expected turn-ending token: {token}')
        stop_token_id = tokenizer.convert_tokens_to_ids(token)

    def load_base():
        return loader.from_pretrained(spec['id'], revision=spec['revision'], dtype=dtype,
                                      attn_implementation='sdpa').to(device)

    def prompt_ids(row):
        return tokenizer.apply_chat_template(
            [{'role': 'user', 'content': row['prompt']}], tokenize=True,
            add_generation_prompt=True, enable_thinking=False, return_dict=False)

    train_rows = dataset(task, 'train')
    test_rows = dataset(task, 'test', eval_size)
    for split, rows in [('train', train_rows), ('test', test_rows)]:
        (out / f'{split}.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8', newline='\n')

    encoded = []
    for row in train_rows:
        prefix = prompt_ids(row)
        completion = tokenizer.encode(row['answer'], add_special_tokens=False) + [stop_token_id]
        if len(prefix) + len(completion) > 256:
            raise ValueError('Example exceeds 256 tokens; refusing to silently truncate the answer')
        encoded.append((prefix + completion, [-100] * len(prefix) + completion))
    (out / 'mask_example.json').write_text(json.dumps({
        'prompt': train_rows[0]['prompt'], 'answer': train_rows[0]['answer'],
        'tokens': tokenizer.convert_ids_to_tokens(encoded[0][0]), 'labels': encoded[0][1]}, indent=2), encoding='utf-8', newline='\n')

    def evaluate(model, name):
        model.eval()
        predictions = []
        with torch.inference_mode():
            for row in test_rows:
                ids = torch.tensor([prompt_ids(row)], device=device)
                generated = model.generate(input_ids=ids, attention_mask=torch.ones_like(ids),
                    max_new_tokens=64, do_sample=False, pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=stop_token_id, use_cache=True)
                text = tokenizer.decode(generated[0, ids.shape[1]:], skip_special_tokens=True)
                predictions.append({**row, 'prediction': text, **score(task, text, row['answer'])})
        (out / f'{name}.json').write_text(json.dumps(predictions, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
        result = {key: sum(p[key] for p in predictions) / len(predictions)
                  for key in ('correct', 'format_valid')}
        print(name, result, flush=True)
        return result

    model = load_base()
    baseline = evaluate(model, 'before')
    # Use only attention projections present in the language model. Vision is frozen.
    targets = [name for name, module in model.named_modules()
               if isinstance(module, torch.nn.Linear)
               and name.rsplit('.', 1)[-1] in ('q_proj', 'v_proj')
               and 'vision' not in name and 'visual' not in name]
    if not targets:
        raise ValueError('No supported LoRA targets: this architecture needs an explicit recipe')
    model = get_peft_model(model, LoraConfig(r=8, lora_alpha=16, lora_dropout=0,
                                           target_modules=targets, task_type='CAUSAL_LM'))
    params = [p for p in model.parameters() if p.requires_grad]
    trainable_count = sum(p.numel() for p in params)
    initial = [p.detach().cpu().clone() for p in params]
    optimizer = torch.optim.AdamW(params, lr=learning_rate)
    model.train()
    model.config.use_cache = False
    train_start = time.monotonic()
    history = []
    for step in range(steps):
        optimizer.zero_grad(set_to_none=True)
        total_loss = 0.
        # Effective batch 4 without padding, a small and readable reference loop.
        for _ in range(4):
            ids, labels = random.choice(encoded)
            loss = model(input_ids=torch.tensor([ids], device=device),
                         labels=torch.tensor([labels], device=device), use_cache=False).loss
            if not torch.isfinite(loss):
                raise RuntimeError('Non-finite loss')
            (loss / 4).backward()
            total_loss += loss.item() / 4
        torch.nn.utils.clip_grad_norm_(params, 1.)
        optimizer.step()
        history.append({'step': step + 1, 'loss': total_loss,
                        'seconds': time.monotonic() - train_start})
        if step % 10 == 0:
            print(history[-1], flush=True)
        if time.monotonic() - train_start >= max_seconds:
            break
    training_seconds = time.monotonic() - train_start
    changed = any(not torch.equal(a, b.detach().cpu()) for a, b in zip(initial, params))
    if not changed:
        raise RuntimeError('Adapter parameters did not change')
    model.save_pretrained(out / 'adapter')
    tokenizer.save_pretrained(out / 'tokenizer')
    model.config.use_cache = True
    after = evaluate(model, 'after')
    del optimizer, params, initial, loss, model
    gc.collect()
    if device == 'cuda':
        torch.cuda.empty_cache()
    model = PeftModel.from_pretrained(load_base(), out / 'adapter')
    reloaded = evaluate(model, 'reloaded')
    same = json.loads((out / 'after.json').read_text(encoding='utf-8')) == json.loads((out / 'reloaded.json').read_text(encoding='utf-8'))
    if not same:
        raise RuntimeError('Saved adapter reload changed deterministic predictions')
    result = dict(model=model_key, model_spec=spec, task=task, seed=42,
                  requested_steps=steps, completed_steps=len(history), learning_rate=learning_rate,
                  eval_size=eval_size, trainable_parameters=trainable_count, adapter_changed=changed,
                  reload_matches=same, baseline=baseline, after=after, reloaded=reloaded,
                  training_seconds=training_seconds, total_seconds=time.monotonic() - started,
                  device=torch.cuda.get_device_name() if device == 'cuda' else device, dtype=str(dtype),
                  peak_vram_gb=torch.cuda.max_memory_allocated()/1e9 if device == 'cuda' else None,
                  data_sha256=hashlib.sha256((out / 'train.jsonl').read_bytes()).hexdigest(),
                  versions={p: importlib.metadata.version(p) for p in ['torch', 'transformers', 'peft', 'accelerate']})
    (out / 'loss.json').write_text(json.dumps(history, indent=2), encoding='utf-8', newline='\n')
    (out / 'environment.txt').write_text('\n'.join(sorted(
        f"{d.metadata['Name']}=={d.version}" for d in importlib.metadata.distributions())), encoding='utf-8', newline='\n')
    (out / 'result.json').write_text(json.dumps(result, indent=2), encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2), flush=True)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', choices=MODELS, default='qwen3-0.6b')
    p.add_argument('--task', choices=TASKS, default='routing')
    p.add_argument('--steps', type=int, default=40)
    p.add_argument('--eval-size', type=int, default=8)
    p.add_argument('--output', default='runs/local')
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], default='cpu')
    p.add_argument('--max-seconds', type=int, default=180)
    p.add_argument('--learning-rate', type=float, default=5e-4)
    a = p.parse_args()
    run(a.model, a.task, a.steps, a.eval_size, a.output, a.device, a.max_seconds, a.learning_rate)
