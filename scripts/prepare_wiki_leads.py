# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Prepare explicitly FILTERED Wikipedia lead substrings with the existing Wiki BPE.

Rules are fixed before training: no redirects; original page >=4,000 characters;
first line beginning triple-apostrophe bold text; stop before a section heading or
at 4,096 characters; keep >=200 characters with >=40% alphabetic characters.
No markup stripping, rewriting, factual-probe filtering, or tokenizer retraining.
"""
import argparse
from collections import Counter
import hashlib
import heapq
import json
from pathlib import Path
import re
import shutil
import time

ROOT = Path(__file__).resolve().parents[1]
BOLD = re.compile(r"^'''", re.MULTILINE)
HEADING = re.compile(r'^={2,}[^\n]*', re.MULTILINE)


def lead_substring(row):
    if row.get('redirect'):
        return None, 'redirect'
    text = row['text']
    if len(text) < 4000:
        return None, 'page_below_4000_chars'
    match = BOLD.search(text)
    if match is None:
        return None, 'no_bold_line_start'
    start = match.start()
    # Opening passages only: a bold line after a section is a body paragraph.
    if HEADING.search(text, 0, start):
        return None, 'section_heading_before_bold_start'
    stop = min(start + 4096, len(text))
    heading = HEADING.search(text, start)
    if heading:
        stop = min(stop, heading.start())
    selected = text[start:stop]
    if len(selected) < 200:
        return None, 'lead_below_200_chars'
    alpha = sum(c.isalpha() for c in selected) / len(selected)
    if alpha < .4:
        return None, 'alphabetic_fraction_below_0.4'
    if selected not in text:
        raise AssertionError('Selected lead must be an unchanged source substring')
    return dict(text=selected, start_char=start, end_char=stop,
                source_chars=len(text), alphabetic_fraction=alpha,
                prior_section_heading=bool(HEADING.search(text, 0, start))), 'kept'


def prepare(source, output):
    import numpy as np
    from tokenizers import Tokenizer
    source, out = Path(source), Path(output)
    if out.exists():
        raise FileExistsError('Output exists; choose a fresh output directory')
    started = time.monotonic()
    metadata = json.loads((source / 'tokens.json').read_text())
    tokenizer_bytes = (source / 'tokenizer.json').read_bytes()
    token_hash = hashlib.sha256(tokenizer_bytes).hexdigest()
    if token_hash != metadata['tokenizer_sha256']:
        raise ValueError('Source tokenizer hash mismatch')
    tok = Tokenizer.from_file(str(source / 'tokenizer.json'))
    eod = tok.token_to_id('<|endoftext|>')
    if eod is None or tok.get_vocab_size() > 65536:
        raise ValueError('Expected uint16 tokenizer with EOD')
    out.mkdir(parents=True)
    shutil.copyfile(source / 'tokenizer.json', out / 'tokenizer.json')
    counts, filters, source_hashes, sample = {}, {}, {}, []
    text_splits = {}
    overlap = Counter()
    for split in ('dev', 'test', 'train'):
        stats = dict(tokens=0, articles=0, utf8_bytes=0, prior_section_heading=0)
        reasons, source_digest, token_digest = Counter(), hashlib.sha256(), hashlib.sha256()
        with (source / f'{split}.jsonl').open('rb') as input_file, (out / f'{split}.jsonl').open('w', encoding='utf-8') as rows_file, (out / f'{split}.bin').open('wb') as bin_file:
            batch = []
            def flush():
                if not batch:
                    return
                encoded = tok.encode_batch([r['text'] for r in batch], add_special_tokens=False)
                for row, encoding in zip(batch, encoded):
                    if tok.decode(encoding.ids, skip_special_tokens=False) != row['text']:
                        raise ValueError('Tokenizer round-trip failed')
                    blob = np.asarray(encoding.ids + [eod], dtype='<u2').tobytes()
                    bin_file.write(blob); token_digest.update(blob)
                    rows_file.write(json.dumps(row, ensure_ascii=False) + '\n')
                    stats['tokens'] += len(encoding.ids) + 1
                    stats['articles'] += 1
                    stats['utf8_bytes'] += len(row['text'].encode('utf-8'))
                    stats['prior_section_heading'] += row['prior_section_heading']
                batch.clear()
            for index, line in enumerate(input_file, 1):
                source_digest.update(line)
                row = json.loads(line)
                lead, reason = lead_substring(row)
                reasons[reason] += 1
                if lead is not None:
                    row_hash = hashlib.sha256(lead['text'].encode('utf-8')).hexdigest()
                    previous = text_splits.setdefault(row_hash, split)
                    if previous != split:
                        overlap[f'{previous}/{split}'] += 1
                    record = dict(id=row['id'], title=row['title'], url=row['url'],
                                  revision_id=row.get('revision_id'), split=split,
                                  source_text_sha256=row['text_sha256'], text_sha256=row_hash, **lead)
                    batch.append(record)
                    rank = int(hashlib.sha256(row['id'].encode()).hexdigest(), 16)
                    entry = (-rank, row['id'], record)
                    if len(sample) < 10:
                        heapq.heappush(sample, entry)
                    elif rank < -sample[0][0]:
                        heapq.heapreplace(sample, entry)
                    if len(batch) == 256:
                        flush()
                if index % 100000 == 0:
                    print(split, 'read', index, 'kept', reasons['kept'], 'elapsed', round(time.monotonic() - started, 1), flush=True)
            flush()
        stats.update(sha256=token_digest.hexdigest(), tokens_per_utf8_byte=stats['tokens'] / stats['utf8_bytes'])
        counts[split], filters[split], source_hashes[split] = stats, dict(reasons), source_digest.hexdigest()
        print(split, json.dumps(stats), flush=True)
    extraction = dict(
        source_directory=str(source.relative_to(ROOT)) if source.is_relative_to(ROOT) else str(source),
        source_jsonl_sha256=source_hashes, source_extraction=metadata.get('extraction'),
        filter='Skip redirects and source pages shorter than4000 characters. First line starting triple apostrophe; reject if a section heading occurs before this line. Exact substring until first following section heading (line starting two or more equals) or4096 chars. Require200+ chars and40%+ alphabetic.',
        no_rewriting=True, substring_verified_every_row=True,
        tokenizer_roundtrip_verified_every_row=True,
        split='Original full-Wikipedia train/dev/test assignment retained unchanged.',
        sample='Ten retained article IDs with smallest SHA256 rank, independent of title/content and diagnostic probes.',
        filters=filters, counts=counts,
        identical_leads_across_splits=dict(overlap),
        limitations=['FILTERED lead-like paragraphs, not the full Wikipedia corpus.',
                     'No manual entity selection or factual-probe-driven filtering.',
                     'A character cap can end mid-sentence or mid-markup.',
                     'Distinct full articles can share identical leads; original split assignments are retained and exact overlap counts are reported.'])
    manifest = dict(vocab_size=tok.get_vocab_size(), eod_id=eod, dtype='little-endian uint16',
                    source_label='FILTERED Polish Wikipedia20260901 lead substrings from nonredirect pages >=4000 characters; not the full Wikipedia corpus',
                    tokenizer_origin='Wiki20260901 8k BPE reused, not retrained on filtered leads',
                    tokenizer_sha256=token_hash, extraction=extraction, splits=counts,
                    packing='Unchanged selected lead substring plus one EOD; causal training windows may cross EOD.',
                    seconds=time.monotonic() - started)
    for filename, value in [('tokens.json', manifest), ('extraction.json', extraction),
                            ('audit_sample.json', [r for _, _, r in sorted(sample, reverse=True)])]:
        (out / filename).write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(dict(seconds=manifest['seconds'], counts=counts, overlap=dict(overlap))), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT / 'data/wiki-scratch-v1')
    parser.add_argument('--output', type=Path, default=ROOT / 'data/wiki-leads-v1')
    args = parser.parse_args()
    prepare(args.source, args.output)
