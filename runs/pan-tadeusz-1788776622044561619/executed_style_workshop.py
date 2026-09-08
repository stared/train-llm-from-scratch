# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Create style examples once, then train a persona adapter for 1–10 minutes."""
import argparse
import gc
import hashlib
import json
import math
from pathlib import Path
import random
import time

from style_data import training_prompts, instruction, surface_metrics, EVALUATION

ROOT = Path(__file__).resolve().parent
MODELS = json.loads((ROOT / 'models.json').read_text())


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2))


def setup(model_key, device):
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForImageTextToText
    spec = MODELS[model_key]
    tokenizer = AutoTokenizer.from_pretrained(spec['id'], revision=spec['revision'])
    tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    stop = (tokenizer.convert_tokens_to_ids(spec['end_of_turn_token'])
            if 'end_of_turn_token' in spec else tokenizer.eos_token_id)
    cls = AutoModelForImageTextToText if spec['multimodal'] else AutoModelForCausalLM
    dtype = torch.bfloat16 if device == 'cuda' and torch.cuda.is_bf16_supported() else torch.float32

    def load():
        return cls.from_pretrained(spec['id'], revision=spec['revision'], dtype=dtype,
                                   attn_implementation='sdpa').to(device)

    return tokenizer, stop, load, spec


def messages(prompt, system=None):
    return ([{'role': 'system', 'content': system}] if system else []) + [{'role': 'user', 'content': prompt}]


def generate(model, tokenizer, stop, prompts, device, system=None, sample=False, max_tokens=192,
             temperature=.8, top_p=.95, top_k=40):
    import torch
    from transformers import GenerationConfig
    text = [tokenizer.apply_chat_template(messages(p, system), tokenize=False,
                add_generation_prompt=True, enable_thinking=False) for p in prompts]
    inputs = tokenizer(text, add_special_tokens=False, padding=True, return_tensors='pt').to(device)
    config = GenerationConfig(max_new_tokens=max_tokens, do_sample=sample,
                              pad_token_id=tokenizer.pad_token_id, eos_token_id=stop)
    if sample:
        config.temperature, config.top_p, config.top_k = temperature, top_p, top_k
    model.eval()
    with torch.inference_mode():
        seq = model.generate(**inputs, generation_config=config)
    return tokenizer.batch_decode(seq[:, inputs.input_ids.shape[1]:], skip_special_tokens=True)


def make_data(output, style='poetry', model_key='gemma4-e2b', languages='both',
              max_seconds=300, device='cuda'):
    import torch
    if not 30 <= max_seconds <= 600:
        raise ValueError('Data-generation time budget must be 30–600 seconds')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    torch.manual_seed(42)
    tokenizer, stop, load, spec = setup(model_key, device)
    model = load()
    prompts = training_prompts(languages)
    random.Random(42).shuffle(prompts)
    accepted, rejected = [], []
    generation_start = time.monotonic()
    for start in range(0, len(prompts), 4):
        batch = prompts[start:start+4]
        answers = generate(model, tokenizer, stop, [r['prompt'] for r in batch], device,
                           system=instruction(style), sample=True)
        for row, answer in zip(batch, answers):
            metrics = surface_metrics(answer, style)
            result = {**row, 'answer': answer.strip(), 'metrics': metrics}
            valid = (metrics['four_lines'] and 12 <= metrics['words'] <= 120 if style == 'poetry'
                     else 5 <= metrics['words'] <= 80)
            (accepted if valid else rejected).append(result)
        print(f'{style}: {len(accepted)} accepted, {len(rejected)} rejected', flush=True)
        # Save incrementally so even an interrupted generation can be inspected.
        write_json(out / 'accepted.json', accepted)
        write_json(out / 'rejected.json', rejected)
        if time.monotonic() - generation_start >= max_seconds:
            break
    (out / 'train.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in accepted))
    result = dict(style=style, teacher=spec, languages=languages, examples=len(accepted),
                  rejected=len(rejected), seed=42, generation_seconds=time.monotonic()-generation_start,
                  total_seconds=time.monotonic()-started, instruction=instruction(style),
                  data_sha256=hashlib.sha256((out / 'train.jsonl').read_bytes()).hexdigest(),
                  quality_note='Only a surface filter was automated; inspect relevance, rhyme, truth and wit manually.')
    write_json(out / 'dataset.json', result)
    if len(accepted) < 24:
        raise RuntimeError('Fewer than 24 valid examples: inspect teacher outputs before training')
    return result


def train(data_dir, output, model_key='qwen3.5-4b', epochs=4, max_seconds=300, device='cuda', lr=1e-4):
    import torch
    from peft import LoraConfig, get_peft_model, PeftModel
    if not 1 <= epochs <= 20 or not 60 <= max_seconds <= 600:
        raise ValueError('Use 1–20 epochs and a 60–600-second training budget')
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    data_dir = Path(data_dir)
    manifest = json.loads((data_dir / 'dataset.json').read_text())
    style = manifest['style']
    rows = [json.loads(line) for line in (data_dir / 'train.jsonl').read_text().splitlines()]
    if len(rows) < 24:
        raise ValueError('Need at least 24 reviewed examples')
    expected = manifest['data_sha256']
    if hashlib.sha256((data_dir / 'train.jsonl').read_bytes()).hexdigest() != expected:
        raise ValueError('Dataset hash mismatch; update manifest explicitly after reviewing edits')
    torch.manual_seed(42)
    rng = random.Random(42)
    started = time.monotonic()
    tokenizer, stop, load, spec = setup(model_key, device)
    encoded = []
    for row in rows:
        prefix = tokenizer.apply_chat_template(messages(row['prompt']), tokenize=True,
                     add_generation_prompt=True, return_dict=False, enable_thinking=False)
        response = tokenizer.encode(row['answer'], add_special_tokens=False) + [stop]
        if len(prefix)+len(response) > 512:
            raise ValueError(f'Example {row["id"]} exceeds 512 tokens; refusing silent truncation')
        encoded.append((prefix+response, [-100]*len(prefix)+response))
    eval_rows = [r for r in EVALUATION if manifest['languages'] in ('both', r['language'])]
    if set(r['prompt'] for r in rows) & set(r['prompt'] for r in eval_rows):
        raise ValueError('Train/evaluation leakage')
    (out / 'train.jsonl').write_bytes((data_dir / 'train.jsonl').read_bytes())
    write_json(out / 'dataset.json', manifest)

    def evaluate(model, label, system=None):
        results = []
        for start in range(0, len(eval_rows), 4):
            batch = eval_rows[start:start+4]
            answers = generate(model, tokenizer, stop, [r['prompt'] for r in batch], device, system)
            results.extend({**r, 'answer': a, **surface_metrics(a, style)} for r, a in zip(batch, answers))
        write_json(out / f'{label}.json', results)
        print(f'{label} sample: {results[0]["answer"]}', flush=True)
        return results

    model = load()
    before = evaluate(model, 'base')
    prompted = evaluate(model, 'prompted', instruction(style))
    targets = [name for name, module in model.named_modules()
               if isinstance(module, torch.nn.Linear)
               and name.rsplit('.', 1)[-1] in ('q_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj')
               and not any(part in name for part in ('vision', 'visual', 'audio'))]
    if not targets:
        raise ValueError('No LoRA target modules found')
    model = get_peft_model(model, LoraConfig(r=16, lora_alpha=32, lora_dropout=.05,
                                           target_modules=targets, task_type='CAUSAL_LM'))
    model.train()
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.AdamW(params, lr=lr, weight_decay=.01)
    schedule = []
    for _ in range(epochs):
        epoch = list(range(len(encoded)))
        rng.shuffle(epoch)
        schedule.extend(epoch)
    history = []
    training_start = time.monotonic()
    for start in range(0, len(schedule), 4):
        indices = schedule[start:start+4]
        optimizer.zero_grad(set_to_none=True)
        avg = 0.
        for index in indices:
            ids, labels = encoded[index]
            loss = model(input_ids=torch.tensor([ids], device=device),
                         labels=torch.tensor([labels], device=device), use_cache=False).loss
            if not torch.isfinite(loss):
                raise RuntimeError('Non-finite training loss')
            (loss/len(indices)).backward()
            avg += loss.item()/len(indices)
        torch.nn.utils.clip_grad_norm_(params, 1.)
        optimizer.step()
        history.append(dict(step=len(history)+1, loss=avg, examples_seen=start+len(indices),
                            seconds=time.monotonic()-training_start))
        if len(history) % 10 == 1:
            print(history[-1], flush=True)
        if time.monotonic()-training_start >= max_seconds:
            break
    training_seconds = time.monotonic()-training_start
    adapter_nonzero = any(p.detach().abs().sum().item() > 0 for n,p in model.named_parameters() if 'lora_B' in n)
    if not adapter_nonzero:
        raise RuntimeError('LoRA B remained zero')
    model.save_pretrained(out / 'adapter')
    tokenizer.save_pretrained(out / 'tokenizer')
    after = evaluate(model, 'finetuned')
    write_json(out / 'loss.json', history)
    del optimizer, params, loss, model
    gc.collect()
    if device == 'cuda':
        torch.cuda.empty_cache()
    model = PeftModel.from_pretrained(load(), out / 'adapter')
    # Preserve evaluation batch size for an exact deterministic reload check.
    reloaded = generate(model, tokenizer, stop, [r['prompt'] for r in eval_rows[:4]], device)
    reload_matches = reloaded == [r['answer'] for r in after[:4]]
    write_json(out / 'reload_probes.json', reloaded)
    result = dict(model=model_key, model_spec=spec, style=style, examples=len(rows), epochs_requested=epochs,
                  steps=len(history), learning_rate=lr, training_seconds=training_seconds,
                  total_seconds=time.monotonic()-started, data_sha256=expected,
                  teacher=manifest['teacher'], adapter_nonzero=adapter_nonzero, reload_matches=reload_matches,
                  peak_vram_gb=torch.cuda.max_memory_allocated()/1e9 if device=='cuda' else None,
                  surface_shape_rates={label: sum(r['style_shape'] for r in values)/len(values)
                    for label,values in [('base',before),('prompted',prompted),('finetuned',after)]},
                  evaluation_note='Shape is not quality: read every held-out answer; no factual or rhyme score is claimed.')
    write_json(out / 'style_result.json', result)
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    return result


def chat(adapter_dir, output, prompt, device='cuda'):
    from peft import PeftModel
    run = Path(adapter_dir)
    spec = json.loads((run / 'style_result.json').read_text())
    tokenizer, stop, load, _ = setup(spec['model'], device)
    model = load()
    before = generate(model, tokenizer, stop, [prompt], device)[0]
    model = PeftModel.from_pretrained(model, run / 'adapter')
    after = generate(model, tokenizer, stop, [prompt], device)[0]
    result = {'prompt': prompt, 'base': before, 'finetuned': after,
              'adapter_run': run.name, 'style': spec['style']}
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    write_json(out / 'chat.json', result)
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    return result


def sample_saved(adapter_dir, output, device='cuda'):
    """Evaluate an existing adapter with a fixed sampled decoding recipe; no training."""
    import torch
    from peft import PeftModel
    run, out = Path(adapter_dir), Path(output)
    out.mkdir(parents=True, exist_ok=False)
    result = json.loads((run / 'style_result.json').read_text())
    manifest = json.loads((run / 'dataset.json').read_text())
    eval_rows = [r for r in EVALUATION if manifest['languages'] in ('both', r['language'])]
    tokenizer, stop, load, _ = setup(result['model'], device)
    model = load()

    def evaluate(label, system=None):
        torch.manual_seed(42)
        answers = []
        for start in range(0, len(eval_rows), 4):
            batch = eval_rows[start:start+4]
            texts = generate(model, tokenizer, stop, [r['prompt'] for r in batch], device,
                             system, sample=True, temperature=.7, top_p=.8, top_k=20)
            answers.extend({**r, 'answer': text, **surface_metrics(text, result['style'])}
                           for r, text in zip(batch, texts))
        write_json(out / f'{label}.json', answers)
        return sum(r['style_shape'] for r in answers)/len(answers)

    rates = {'base': evaluate('base'), 'prompted': evaluate('prompted', instruction(result['style']))}
    model = PeftModel.from_pretrained(model, run / 'adapter')
    rates['finetuned'] = evaluate('finetuned')
    result.update(source_run=run.name, evaluation_only=True, surface_shape_rates=rates,
                  decoding={'sample': True, 'temperature': .7, 'top_p': .8, 'top_k': 20,
                            'presence_penalty': 0, 'seed': 42, 'max_new_tokens': 192})
    write_json(out / 'style_result.json', result)
    write_json(out / 'dataset.json', manifest)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('stage', choices=['data', 'train', 'chat', 'sample'])
    p.add_argument('--style', choices=['poetry','wit'], default='poetry')
    p.add_argument('--model', choices=MODELS, default='qwen3.5-4b')
    p.add_argument('--languages', choices=['both','pl','en'], default='both')
    p.add_argument('--data-dir')
    p.add_argument('--adapter-dir', help='Training run directory containing adapter/ and style_result.json')
    p.add_argument('--prompt', default='Why should I write tests?')
    p.add_argument('--output', required=True)
    p.add_argument('--epochs', type=int, default=4)
    p.add_argument('--max-seconds', type=int, default=300)
    p.add_argument('--device', choices=['cpu','cuda','mps'], default='cpu')
    a=p.parse_args()
    if a.stage=='data':
        make_data(a.output,a.style,a.model,a.languages,a.max_seconds,a.device)
    elif a.stage=='train':
        if not a.data_dir:
            p.error('--data-dir is required for training')
        train(a.data_dir,a.output,a.model,a.epochs,a.max_seconds,a.device)
    else:
        if not a.adapter_dir:
            p.error('--adapter-dir is required for chat/sample')
        if a.stage=='chat':
            chat(a.adapter_dir,a.output,a.prompt,a.device)
        else:
            sample_saved(a.adapter_dir,a.output,a.device)
