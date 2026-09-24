# /// script
# requires-python = ">=3.14"
# dependencies = ["tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Tokenize the plain-text Sejm corpus with the existing Wiki BPE.

The source is either sejm.txt or the published sejm.zip that contains it.

The text is used exactly as supplied: no cleaning, normalization or
deduplication. The file is only cut into chunks of roughly CHUNK_CHARS
characters at blank lines, so that whole chunks can be assigned to the
train, development and test splits. Every chunk ends with one EOD token.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import time
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path.home() / 'corpora/sejm.txt'
ARCHIVE_MEMBER = 'sejm.txt'
GENERATION_PROMPTS = ['Panie Marszałku! Wysoka Izbo!', 'Przystępujemy do', 'Proszę o zabranie głosu', 'Wicemarszałek']
CHUNK_CHARS = 64_000
# A chunk without any blank line is cut at the next line end past this size.
HARD_LIMIT_CHARS = 4 * CHUNK_CHARS
BATCH_CHUNKS = 64
MIN_EVAL_TOKENS = 2048  # Fixed evaluation windows need room inside each split.


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def split_for(text):
    bucket = int(digest(text)[:16], 16) % 1000
    return 'test' if bucket < 50 else 'dev' if bucket < 100 else 'train'


def open_text(path):
    # newline='' keeps the original line endings.
    if path.suffix == '.zip':
        archive = zipfile.ZipFile(path)
        return io.TextIOWrapper(archive.open(ARCHIVE_MEMBER), encoding='utf-8', newline='')
    return path.open(encoding='utf-8', newline='')


def chunks(path):
    """Yield consecutive text chunks; their concatenation is the whole text."""
    with open_text(path) as stream:
        lines, size = [], 0
        for line in stream:
            lines.append(line)
            size += len(line)
            if size >= HARD_LIMIT_CHARS or (size >= CHUNK_CHARS and not line.strip()):
                yield ''.join(lines)
                lines, size = [], 0
        if lines:
            yield ''.join(lines)


def prepare(source, tokenizer_path, output):
    import numpy as np
    from tokenizers import Tokenizer
    started = time.monotonic()
    source, tokenizer_path, out = map(Path, (source, tokenizer_path, output))
    if not source.is_file():
        raise FileNotFoundError(f'Sejm corpus not found: {source}')
    if out.exists():
        raise FileExistsError('Output exists; choose a new dataset directory')
    with source.open('rb') as f:
        source_hash = hashlib.file_digest(f, 'sha256').hexdigest()
    tok = Tokenizer.from_file(str(tokenizer_path))
    eod = tok.token_to_id('<|endoftext|>')
    if eod is None or tok.get_vocab_size() > 65536:
        raise ValueError('Expected uint16-compatible tokenizer with EOD')
    out.mkdir(parents=True)
    shutil.copyfile(tokenizer_path, out / 'tokenizer.json')
    splits = ('train', 'dev', 'test')
    binaries = {s: (out / f'{s}.bin').open('wb') for s in splits}
    hashes = {s: hashlib.sha256() for s in splits}
    counts = {s: dict(tokens=0, articles=0, utf8_bytes=0) for s in splits}
    total_chunks = 0

    def write(batch):
        for text, encoding in zip(batch, tok.encode_batch(batch, add_special_tokens=False)):
            ids = encoding.ids
            if tok.decode(ids, skip_special_tokens=False) != text:
                raise ValueError(f'Round-trip failure in chunk {digest(text)[:12]}')
            split = split_for(text)
            blob = np.asarray(ids + [eod], dtype='<u2').tobytes()
            binaries[split].write(blob)
            hashes[split].update(blob)
            counts[split]['tokens'] += len(ids) + 1
            counts[split]['articles'] += 1
            counts[split]['utf8_bytes'] += len(text.encode('utf-8'))

    try:
        batch = []
        for text in chunks(source):
            batch.append(text)
            total_chunks += 1
            if len(batch) == BATCH_CHUNKS:
                write(batch)
                batch = []
                print('Prepared', total_chunks, 'chunks;', round(time.monotonic() - started, 1), 'seconds', flush=True)
        if batch:
            write(batch)
    finally:
        for f in binaries.values():
            f.close()
    for split, stats in counts.items():
        if stats['tokens'] < MIN_EVAL_TOKENS:
            raise ValueError(f'The {split} split has only {stats["tokens"]} tokens; the corpus is too small to split')
        stats.update(sha256=hashes[split].hexdigest(), tokens_per_utf8_byte=stats['tokens'] / stats['utf8_bytes'])
    extraction = dict(
        source=str(source), source_sha256=source_hash, source_bytes=source.stat().st_size,
        archive_member=ARCHIVE_MEMBER if source.suffix == '.zip' else None,
        chunks=total_chunks,
        extraction='None: the text file is used verbatim, including line endings.',
        chunking=f'Consecutive chunks cut at the first blank line after {CHUNK_CHARS} characters, '
                 f'or at a line end after {HARD_LIMIT_CHARS} characters; one EOD after each chunk.',
        split='SHA256(chunk text) first16 hex modulo1000: test0-49, dev50-99, train100-999. Identical chunks share a split.',
        limitations=['Chunks are not sittings or speeches; neighbouring chunks of one sitting can fall into different splits.',
                     'No deduplication or language filtering.'],
        counts=counts)
    manifest = dict(vocab_size=tok.get_vocab_size(), eod_id=eod, dtype='little-endian uint16',
                    tokenizer_sha256=hashlib.sha256((out / 'tokenizer.json').read_bytes()).hexdigest(),
                    source_label='Sejm transcripts, terms I–III (1991–2001), plain text used verbatim',
                    tokenizer_origin='Wiki20260901 8k BPE reused, not trained on Sejm',
                    generation_prompts=GENERATION_PROMPTS,
                    quality_prompts=[*GENERATION_PROMPTS, 'Dziękuję bardzo.', 'Sprzeciwu nie słyszę.', 'Szanowni Państwo,', 'Poseł'],
                    quality_fact_probes=[],  # Wikipedia fact probes do not apply to transcripts.
                    extraction=extraction, splits=counts,
                    packing='Chunk text plus one EOD; training windows may cross EOD boundaries',
                    seconds=time.monotonic() - started)
    (out / 'extraction.json').write_text(json.dumps(extraction, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'tokens.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(dict(splits=counts, seconds=manifest['seconds']), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--tokenizer', type=Path, default=ROOT / 'datasets/wiki-tokenizer.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'datasets/local/sejm-scratch-v1')
    args = parser.parse_args()
    prepare(args.source, args.tokenizer, args.output)
