# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Fixed, small diagnostics for scratch models; not a factuality benchmark.

Candidate scoring measures preference among supplied continuations, not whether
free generation supplies a correct fact. Repetition counts do not assess grammar.
"""
from collections import Counter
from contextlib import nullcontext
import json
from pathlib import Path
import re
import time

import torch

# Freeze before inspecting the longer experiments. Correct answers are deliberately
# not always first. These common facts are stable; article exposure is not excluded.
FACT_PROBES = [
    dict(prompt="'''Warszawa''' –", candidates=['miasto', 'wieś', 'rzeka', 'jezioro'], correct=0),
    dict(prompt="'''Polska''' –", candidates=['wieś', 'jezioro', 'państwo', 'rzeka'], correct=2),
    dict(prompt="'''Warszawa''' – stolica", candidates=['Niemiec', 'Polski', 'Francji', 'Włoch'], correct=1),
    dict(prompt="'''Kraków''' – miasto w", candidates=['Hiszpanii', 'Japonii', 'Polsce', 'Kanadzie'], correct=2),
    dict(prompt="'''Wisła''' – najdłuższa rzeka w", candidates=['Polsce', 'Egipcie', 'Chinach', 'Brazylii'], correct=0),
    dict(prompt="'''Adam Mickiewicz''' – polski", candidates=['chemik', 'astronauta', 'piłkarz', 'poeta'], correct=3),
    dict(prompt="'''Fryderyk Chopin''' – polski", candidates=['geolog', 'kompozytor', 'astronauta', 'kolarz'], correct=1),
    dict(prompt="'''Ziemia''' – trzecia planeta od", candidates=['Księżyca', 'Jowisza', 'Słońca', 'Marsa'], correct=2),
    dict(prompt="'''Bałtyk''' – morze w", candidates=['Europie', 'Afryce', 'Australii', 'Antarktydzie'], correct=0),
    dict(prompt="'''Paryż''' – stolica", candidates=['Polski', 'Niemiec', 'Hiszpanii', 'Francji'], correct=3),
]
FREE_PROMPTS = [
    "'''Warszawa''' –",
    "'''Kraków''' –",
    "'''Wisła''' –",
    "'''Adam Mickiewicz''' –",
    "'''Fryderyk Chopin''' –",
    "'''Ziemia''' –",
    '== Historia ==\n',
    '{{Infobox',
]


def repetition_stats(text):
    """Case-folded word 4-grams; punctuation and markup symbols are ignored."""
    words = re.findall(r'\w+', text.casefold(), flags=re.UNICODE)
    grams = [tuple(words[i:i + 4]) for i in range(max(0, len(words) - 3))]
    counts = Counter(grams)
    return dict(words=len(words), word_4grams=len(grams),
                repeated_word_4gram_fraction=(len(grams) - len(counts)) / len(grams) if grams else 0.,
                most_common_word_4gram_count=max(counts.values(), default=0))


def evaluate_quality(model, tokenizer, device, outpath, *, max_new_tokens=128, free_prompts=None, fact_probes=None):
    """Evaluate current weights, preserving mode and RNG; write JSON to outpath.

    Requires ScratchGPT-compatible forward(ids, targets), generate(), and config.
    Caller supplies model/data labels separately (the report records architecture).
    On CUDA, BF16 autocast matches the training experiment's inference precision.
    """
    started = time.monotonic()
    device = torch.device(device)
    was_training = model.training
    def precision():
        return torch.autocast('cuda', dtype=torch.bfloat16) if device.type == 'cuda' else nullcontext()
    cuda_devices = [device.index if device.index is not None else torch.cuda.current_device()] if device.type == 'cuda' else []
    facts, generations = [], []
    try:
        model.eval()
        with torch.no_grad(), torch.random.fork_rng(devices=cuda_devices):
            for probe in (FACT_PROBES if fact_probes is None else fact_probes):
                prefix_ids = tokenizer.encode(probe['prompt']).ids
                scores = []
                for candidate in probe['candidates']:
                    # Separate tokenization fixes the prefix across candidates.
                    # Byte-level decoding still gives prompt + space + candidate.
                    suffix_ids = tokenizer.encode(' ' + candidate).ids
                    ids = prefix_ids + suffix_ids
                    if len(ids) - 1 > model.config.context:
                        raise ValueError('Fact probe exceeds model context')
                    x = torch.tensor([ids[:-1]], dtype=torch.long, device=device)
                    targets = torch.tensor([ids[1:]], dtype=torch.long, device=device)
                    targets[:, :len(prefix_ids) - 1] = -100
                    with precision():
                        mean_nll = float(model(x, targets).item())
                    scores.append(dict(candidate=candidate, tokens=len(suffix_ids),
                                       mean_log_probability=-mean_nll,
                                       sum_log_probability=-mean_nll * len(suffix_ids)))
                predicted = max(range(len(scores)), key=lambda i: scores[i]['mean_log_probability'])
                facts.append(dict(**probe, scores=scores, predicted=predicted,
                                  is_correct=predicted == probe['correct']))
            for index, prompt in enumerate(FREE_PROMPTS if free_prompts is None else free_prompts):
                # Stable independent seeds: changing probe order does not consume
                # arbitrary quantities of random numbers for later generations.
                torch.manual_seed(20260908 + index)
                ids = torch.tensor([tokenizer.encode(prompt).ids], dtype=torch.long, device=device)
                with precision():
                    output = model.generate(ids, new_tokens=max_new_tokens, temperature=.8, top_k=50)
                continuation_ids = output[0, ids.shape[1]:].tolist()
                continuation = tokenizer.decode(continuation_ids, skip_special_tokens=False)
                generations.append(dict(prompt=prompt, continuation=continuation,
                                        generated_tokens=len(continuation_ids), seed=20260908 + index,
                                        **repetition_stats(continuation)))
    finally:
        model.train(was_training)
    result = dict(
        diagnostic_version='wiki-quality-v1',
        description='Fixed candidate preferences and free continuations; not a benchmark.',
        limitations=[
            'Facts may occur in the training corpus; no held-out knowledge claim.',
            'Mean candidate token log-probability is length-normalized but still sensitive to tokenization and wording.',
            'Candidate correctness does not establish factual correctness of free continuations.',
            'Word repetition is a loop diagnostic, not a grammar or factuality score.',
            'One sampling seed per prompt; generations have substantial sampling variance.',
        ],
        model_parameters=sum(p.numel() for p in model.parameters()),
        context=model.config.context,
        scoring='Teacher-forced candidate mean log-probability; prompt excluded; no end-of-text probability.',
        factual_correct=sum(row['is_correct'] for row in facts), factual_total=len(facts),
        facts=facts, temperature=.8, top_k=50, max_new_tokens=max_new_tokens,
        free_generations=generations,
        mean_repeated_word_4gram_fraction=sum(row['repeated_word_4gram_fraction'] for row in generations) / len(generations),
        evaluation_seconds=time.monotonic() - started,
    )
    if outpath is not None:
        Path(outpath).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    return result


if __name__ == '__main__':
    import argparse
    from tokenizers import Tokenizer
    from scratch_model import Config, ScratchGPT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir', type=Path)
    parser.add_argument('--device', choices=['cpu', 'cuda'], default='cpu')
    parser.add_argument('--checkpoint', default='best.pt')
    args = parser.parse_args()
    metadata = json.loads((args.run_dir / 'result.json').read_text(encoding='utf-8'))
    model = ScratchGPT(Config(**metadata['config'])).to(args.device)
    state = torch.load(args.run_dir / args.checkpoint, map_location=args.device, weights_only=True)
    model.load_state_dict(state['model'] if 'model' in state else state)
    tokenizer = Tokenizer.from_file(str(args.run_dir / 'tokenizer.json'))
    result = evaluate_quality(model, tokenizer, args.device, args.run_dir / 'quality.json')
    result['model'] = metadata['model']
    result['source'] = metadata['source']
    result['checkpoint'] = args.checkpoint
    (args.run_dir / 'quality.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    print(json.dumps({key: result[key] for key in ('factual_correct', 'factual_total', 'evaluation_seconds')}, indent=2))


def evaluate_fixed_pool(model, device, data_dir, batch_count=8, batch_size=8, seed=20260908):
    """Defaults preserve the original 16k-token pool; explicit settings allow larger audits."""
    import hashlib
    import numpy as np
    folder=Path(data_dir)
    metadata=json.loads((folder/'tokens.json').read_text(encoding='utf-8'))
    if batch_count<1 or batch_size<1:raise ValueError('Positive evaluation batch dimensions required')
    rng=np.random.default_rng(seed)
    result={}
    was_training=model.training;model.eval()
    try:
        with torch.no_grad():
            for split in ('train','dev','test'):
                size=metadata['splits'][split]['tokens']
                starts=rng.integers(0,size-257,size=(batch_count,batch_size))
                if split=='train':continue
                path=folder/f'{split}.bin'
                with path.open('rb') as file:
                    if hashlib.file_digest(file,'sha256').hexdigest()!=metadata['splits'][split]['sha256']:
                        raise ValueError('Evaluation pool checksum mismatch')
                arr=np.memmap(path,dtype='<u2',mode='r');losses=[]
                for offsets in starts:
                    block=np.stack([arr[int(i):int(i)+257] for i in offsets]).astype(np.int64)
                    batch=torch.from_numpy(block).to(device)
                    with torch.autocast('cuda',dtype=torch.bfloat16) if str(device).startswith('cuda') else nullcontext():
                        losses.append(model(batch[:,:-1],batch[:,1:]).item())
                result[split]=dict(loss_nats=sum(losses)/len(losses),tokens=batch_count*batch_size*256)
    finally:model.train(was_training)
    return dict(source=metadata.get('source_label',folder.name),
                tokenizer_sha256=metadata['tokenizer_sha256'],seed=seed,batch_count=batch_count,batch_size=batch_size,**result)
