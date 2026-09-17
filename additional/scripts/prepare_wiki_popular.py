# /// script
# requires-python = ">=3.14"
# dependencies = ["tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Select top-linked Wikipedia openings using training-only link popularity."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import time

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[\[([^\[\]\n|]+)(?:\||\]\])")


def normalize_title(title):
    title = title.replace('_', ' ').split('#', 1)[0].strip()
    if not title or ':' in title:
        return None
    return title[0].upper() + title[1:]


def prepare(full, leads, out, limit):
    import numpy as np
    from tokenizers import Tokenizer
    started = time.monotonic()
    if out.exists():
        raise FileExistsError(out)
    out.mkdir(parents=True)
    candidates, lead_hashes = set(), {}
    for split in ('train', 'dev', 'test'):
        digest = hashlib.sha256()
        with (leads / f'{split}.jsonl').open('rb') as handle:
            for line in handle:
                digest.update(line)
                title = normalize_title(json.loads(line)['title'])
                if title:
                    candidates.add(title)
        lead_hashes[split] = digest.hexdigest()
    print('Eligible titles', len(candidates), flush=True)
    counts, digest = Counter(), hashlib.sha256()
    with (full / 'train.jsonl').open('rb') as handle:
        for articles, line in enumerate(handle, 1):
            digest.update(line)
            row = json.loads(line)
            # Count at most one vote per source article for each eligible title.
            targets = {normalize_title(m.group(1)) for m in LINK.finditer(row['text'])}
            counts.update(targets & candidates)
            if articles % 100000 == 0:
                print('Counted links in', articles, 'training articles;', round(time.monotonic()-started, 1), 'seconds', flush=True)
    ranking = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]
    selected = dict(ranking)
    if len(selected) != limit:
        raise ValueError(f'Only {len(selected)} ranked titles, expected {limit}')
    print('Selected', len(selected), 'titles', flush=True)
    meta = json.loads((leads / 'tokens.json').read_text())
    tokenizer_bytes = (leads / 'tokenizer.json').read_bytes()
    tokenizer_hash = hashlib.sha256(tokenizer_bytes).hexdigest()
    if tokenizer_hash != meta['tokenizer_sha256']:
        raise ValueError('Tokenizer source hash mismatch')
    tok = Tokenizer.from_file(str(leads / 'tokenizer.json'))
    eod = tok.token_to_id('<|endoftext|>')
    if eod is None or tok.get_vocab_size() > 65536:
        raise ValueError('Expected EOD and uint16 vocabulary')
    shutil.copyfile(leads / 'tokenizer.json', out / 'tokenizer.json')
    stats, overlap, seen_hashes, found_titles = {}, Counter(), {}, set()
    for split in ('dev', 'test', 'train'):
        count = dict(articles=0, tokens=0, utf8_bytes=0)
        token_digest, json_digest = hashlib.sha256(), hashlib.sha256()
        with (leads / f'{split}.jsonl').open('rb') as inp, (out / f'{split}.jsonl').open('wb') as rows, (out / f'{split}.bin').open('wb') as tokens:
            batch = []
            def flush():
                if not batch:
                    return
                encodings = tok.encode_batch([row['text'] for row in batch], add_special_tokens=False)
                for row, encoded in zip(batch, encodings):
                    if tok.decode(encoded.ids, skip_special_tokens=False) != row['text']:
                        raise ValueError('Tokenizer roundtrip mismatch')
                    body_hash = hashlib.sha256(row['text'].encode()).hexdigest()
                    if body_hash != row['text_sha256'] or row['split'] != split:
                        raise ValueError('Source text hash or split mismatch')
                    previous = seen_hashes.setdefault(body_hash, split)
                    if previous != split:
                        overlap[f'{previous}/{split}'] += 1
                    blob = np.asarray(encoded.ids + [eod], dtype='<u2').tobytes()
                    tokens.write(blob); token_digest.update(blob)
                    record = (json.dumps(row, ensure_ascii=False) + '\n').encode()
                    rows.write(record); json_digest.update(record)
                    count['articles'] += 1
                    count['tokens'] += len(encoded.ids) + 1
                    count['utf8_bytes'] += len(row['text'].encode())
                batch.clear()
            for line in inp:
                row = json.loads(line)
                title = normalize_title(row['title'])
                if title in selected:
                    found_titles.add(title)
                    row['training_articles_linking_title'] = selected[title]
                    batch.append(row)
                    if len(batch) == 256:
                        flush()
            flush()
        if count['tokens'] < 257:
            raise ValueError(f'{split} too small')
        count.update(sha256=token_digest.hexdigest(), jsonl_sha256=json_digest.hexdigest(), tokens_per_utf8_byte=count['tokens']/count['utf8_bytes'])
        stats[split] = count
        print(split, json.dumps(count), flush=True)
    if found_titles != set(selected):
        raise ValueError('Some selected titles were not emitted')
    ranking_bytes = (json.dumps([dict(rank=i, title=title, training_articles_linking=count) for i, (title, count) in enumerate(ranking, 1)], ensure_ascii=False, indent=2) + '\n').encode()
    (out / 'ranking.json').write_bytes(ranking_bytes)
    extraction = dict(
        source_full_directory=str(full.relative_to(ROOT)), source_leads_directory=str(leads.relative_to(ROOT)),
        full_training_jsonl_sha256=digest.hexdigest(), full_training_articles=articles,
        source_lead_jsonl_sha256=lead_hashes, source_lead_extraction=meta['extraction'],
        ranking_sha256=hashlib.sha256(ranking_bytes).hexdigest(), eligible_titles=len(candidates), selected_titles=len(selected),
        ranking_policy='Top titles by distinct full-Wikipedia TRAIN articles containing an internal [[target]] or [[target|label]] link. Count eligible retained lead titles only, which gives the same eligible ranking as counting every title first. Underscores become spaces, anchors are removed, surrounding whitespace stripped, first character capitalized; empty targets and targets containing colon excluded. No redirect resolution. Ties sorted lexicographically. Regex scans literal wikitext including comments/templates.',
        split_policy='Original full-Wikipedia split retained; dev/test text never contributes popularity votes. Held-out titles can be selected from links in training articles.',
        text_policy='Exact previously filtered opening text, unchanged. Same Wiki8k tokenizer. One EOD per document.',
        verification=dict(every_text_hash=True, every_tokenizer_roundtrip=True, original_split=True, all_selected_titles_emitted=True, minimum_split_tokens=257),
        identical_texts_across_splits=dict(overlap), counts=stats,
        no_factual_probe_selection=True,
        limitations=['Generic popularity curriculum; not the full Wikipedia corpus.', 'Popularity uses link mentions rather than human pageviews.', 'Dev/test has only the small original held-out share of selected titles.'])
    manifest = dict(vocab_size=tok.get_vocab_size(), eod_id=eod, dtype='little-endian uint16',
        source_label=f'top{limit//1000}k linked Wikipedia openings (Polish 20260901), selected by training-only incoming link counts; filtered original wikitext, not full Wikipedia',
        tokenizer_origin='Wiki20260901 8k BPE reused unchanged', tokenizer_sha256=tokenizer_hash,
        extraction=extraction, splits=stats, packing='Original lead plus EOD; causal windows may cross EOD.', seconds=time.monotonic()-started)
    for name, value in [('tokens.json', manifest), ('extraction.json', extraction)]:
        (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2))
    print('Completed in', round(manifest['seconds'], 1), 'seconds; local CPU only; GPU cost $0', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', type=Path, default=ROOT/'datasets/local/wiki-scratch-v1')
    parser.add_argument('--leads', type=Path, default=ROOT/'datasets/local/wiki-leads-v1')
    parser.add_argument('--output', type=Path, default=ROOT/'datasets/local/wiki-popular-v1')
    parser.add_argument('--limit', type=int, default=10000)
    args = parser.parse_args()
    prepare(args.full, args.leads, args.output, args.limit)
