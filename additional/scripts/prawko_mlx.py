# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = ["mlx-lm==0.31.3"]
# ///
"""Local MLX LoRA experiment with the workshop's answer-only driving task."""
import argparse
import importlib.metadata
import json
from pathlib import Path
import random
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from prawko import question


def main():
    import mlx.core as mx
    import mlx.nn as nn
    import mlx.optimizers as optim
    from mlx.utils import tree_flatten, tree_map
    from mlx_lm import load
    from mlx_lm.tuner.utils import linear_to_lora_layers

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-seconds', type=int, default=180)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--microbatch-size', type=int, choices=(1, 4), default=4)
    args = parser.parse_args()
    if not 1 <= args.max_seconds <= 720:
        parser.error('Use a training budget of 1–720 seconds.')
    args.output.mkdir(parents=True, exist_ok=False)
    def save(name, value):
        (args.output / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2))
    started = time.monotonic()
    spec = json.loads((ROOT / 'scripts/models.json').read_text())['qwen3.5-0.8b']
    data = json.loads((ROOT / 'datasets/prawko-v2/data.json').read_text())
    save('data', data)
    model, tokenizer = load(spec['id'], revision=spec['revision'])
    mx.random.seed(args.seed)
    model.freeze()
    config = dict(rank=16, scale=2., dropout=0., keys=[
        'self_attn.q_proj', 'self_attn.k_proj', 'self_attn.v_proj', 'self_attn.o_proj',
        'mlp.gate_proj', 'mlp.up_proj', 'mlp.down_proj'])
    linear_to_lora_layers(model, len(model.layers), config)
    mx.eval(model.parameters())
    label_ids = mx.array([tokenizer.encode(c, add_special_tokens=False)[0] for c in 'ABC'])

    def encode(row, order=(0, 1, 2)):
        prompt, answer = question(row, order)
        ids = tokenizer.apply_chat_template([dict(role='user', content=prompt)], tokenize=True,
                                            add_generation_prompt=True, enable_thinking=False)
        if len(ids) > 768:
            raise ValueError('Unexpected long prompt')
        return mx.array([ids]), answer

    def logits(m, ids, lengths=None):
        text = m.language_model
        hidden = text.model(ids)
        last = hidden[:, -1, :] if lengths is None else hidden[mx.arange(ids.shape[0]), lengths-1]
        return (text.model.embed_tokens.as_linear(last) if text.args.tie_word_embeddings else text.lm_head(last)).astype(mx.float32)

    def evaluate(name, rows, rotated=False):
        model.eval()
        records = []
        for row in rows:
            ids, answer = encode(row, (1, 2, 0) if rotated else (0, 1, 2))
            values = logits(model, ids)[0]
            probabilities = mx.softmax(values[label_ids])
            mx.eval(probabilities)
            probs = probabilities.tolist()
            pred = max(range(3), key=probs.__getitem__)
            records.append(dict(id=row['id'], question=row['question'], options=[row['options'][i] for i in ((1,2,0) if rotated else (0,1,2))], answer='ABC'[answer], prediction='ABC'[pred], correct=pred==answer, probabilities=probs))
        save(name, records)
        metric = dict(n=len(rows), correct=sum(r['correct'] for r in records), accuracy=sum(r['correct'] for r in records)/len(rows), mean_correct_probability=sum(r['probabilities']['ABC'.index(r['answer'])] for r in records)/len(rows))
        print(name, metric, flush=True)
        return metric

    before = {split: evaluate('before_' + split, data[split]) for split in ('dev', 'test')}
    before['test_rotated'] = evaluate('before_test_rotated', data['test'], True)
    best = dict(tree_flatten(model.trainable_parameters()))
    best_score = (before['dev']['correct'], before['dev']['mean_correct_probability'])
    best_epoch = 0
    optimizer = optim.AdamW(learning_rate=5e-5, weight_decay=0.)
    def loss_fn(m, ids, answers, lengths):
        return nn.losses.cross_entropy(logits(m, ids, lengths), label_ids[answers]).mean()
    gradient = nn.value_and_grad(model, loss_fn)
    rng = random.Random(args.seed)
    history, checkpoints = [], []
    train_started = time.monotonic()
    for epoch in range(10):
        order = list(range(len(data['train'])))
        rng.shuffle(order)
        model.train()
        for offset in range(0, len(order), 4):
            gradients, losses = None, []
            batch = order[offset:offset+4]
            for micro_offset in range(0, len(batch), args.microbatch_size):
                encoded = [encode(data['train'][i], rng.sample(range(3), 3)) for i in batch[micro_offset:micro_offset+args.microbatch_size]]
                lengths = mx.array([ids.shape[1] for ids,_ in encoded])
                width = max(ids.shape[1] for ids,_ in encoded)
                padded = mx.concatenate([mx.pad(ids, ((0,0),(0,width-ids.shape[1])), constant_values=tokenizer.pad_token_id or 0) for ids,_ in encoded])
                answers = mx.array([answer for _,answer in encoded])
                loss, grad = gradient(model, padded, answers, lengths)
                mx.eval(loss, grad)
                if not bool(mx.isfinite(loss).item()):
                    raise RuntimeError('Nonfinite training loss')
                losses.append(loss.item())
                gradients = grad if gradients is None else tree_map(lambda a,b:a+b, gradients, grad)
            gradients = tree_map(lambda g:g/len(losses), gradients)
            norm = mx.sqrt(sum(mx.sum(g*g) for _,g in tree_flatten(gradients)))
            gradients = tree_map(lambda g:g*mx.minimum(1.,1./(norm+1e-6)), gradients)
            optimizer.update(model, gradients)
            mx.eval(model.trainable_parameters(), optimizer.state)
            history.append(dict(step=len(history)+1, epoch=epoch+1, loss=sum(losses)/len(losses)))
            if len(history)%10 == 0:
                print('step',len(history),'seconds',time.monotonic()-train_started,flush=True)
            if time.monotonic()-train_started >= args.max_seconds:
                break
        metric = evaluate('dev_epoch_' + str(epoch+1), data['dev'])
        checkpoints.append(dict(epoch=epoch+1,steps=len(history),**metric))
        score = (metric['correct'], metric['mean_correct_probability'])
        if score > best_score:
            best_score, best_epoch = score, epoch+1
            best = dict(tree_flatten(model.trainable_parameters()))
        model.train()
        if time.monotonic()-train_started >= args.max_seconds:
            break
    training_seconds = time.monotonic()-train_started
    final = {split:evaluate('final_'+split,data[split]) for split in ('dev','test')}
    model.load_weights(list(best.items()), strict=False)
    after = {split:evaluate('after_'+split,data[split]) for split in ('dev','test')}
    after['test_rotated'] = evaluate('after_test_rotated',data['test'],True)
    adapter = args.output/'adapter'
    adapter.mkdir()
    mx.save_safetensors(str(adapter/'adapters.safetensors'),best)
    (adapter/'adapter_config.json').write_text(json.dumps(dict(fine_tune_type='lora',num_layers=len(model.layers),lora_parameters=config)))
    peak_memory = mx.get_peak_memory()/1e9
    del model
    mx.clear_cache()
    model, tokenizer = load(spec['id'],revision=spec['revision'],adapter_path=str(adapter))
    evaluate('reload',data['test'][:8])
    selected = json.loads((args.output/'after_test.json').read_text())[:8]
    reloaded = json.loads((args.output/'reload.json').read_text())
    reload_matches = all(a['prediction']==b['prediction'] for a,b in zip(selected,reloaded))
    if not reload_matches:
        raise RuntimeError('Reload changed predictions')
    save('history',history);save('checkpoints',checkpoints)
    save('result',dict(model_spec=spec,method='sft',training_data='100 Polish driving questions',backend='mlx',seed=args.seed,before=before,after=after,final=final,
                      training_seconds=training_seconds,total_seconds=time.monotonic()-started,steps=len(history),
                      selected_epoch=best_epoch,peak_memory_gb=peak_memory,reload_matches=reload_matches,
                      mlx=importlib.metadata.version('mlx'),mlx_lm=importlib.metadata.version('mlx-lm'),
                      batch_size=4,microbatch_size=args.microbatch_size,learning_rate=5e-5,lora=config))


if __name__ == '__main__':
    main()
