# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Prepare the historical Falenty Wolne Lektury archive with the existing Wiki BPE.

The archive is a concatenated snapshot, not a current complete library. Paragraphs
inside retained bodies are unchanged. Canonical URLs and exact duplicate bodies
stay in one split. Semantic overlaps between anthologies and parts are not removed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import time
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE_SHA256 = '1a25be256ee13a4a39c9a1c549d4a3f363bf2e4ad673f8e1c34e25473c43e15b'
MARKER = 'Ta lektura, podobnie jak tysiące innych, dostępna jest na stronie wolnelektury.pl.'
URL = re.compile(r'https?://(?:www\.)?wolnelektury\.pl/katalog/lektura/([^\s/.]+)')
# These occur only at the start of a known footer, consumed consecutively. Never
# search globally for them in a literary body. Unknown paragraphs stop removal.
FOOTER_PREFIXES = (
    'Wersja lektury w opracowaniu merytorycznym i krytycznym',
    'Utwór opracowany został w ramach projektu Wolne Lektury',
    'Wszystkie zasoby Wolnych Lektur możesz swobodnie',
    'Ten utwór jest udostępniony na licencji',
    'Tekst opracowany na podstawie:', 'Wydawca:',
    'Publikacja', 'Publikację wsparli i wsparły:',
    'Opracowanie redakcyjne i przypisy:', 'ISBN-', 'ISBN ',
    'Dofinansowano ze środków', 'Sfinansowano ze środków',
    'Utwór powstał w ramach konkursu', 'Wiersz nagrodzony w konkursie poetyckim',
)


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def records(text):
    markers = list(re.finditer(re.escape(MARKER), text))
    body_start = 0
    for i, marker in enumerate(markers):
        next_marker = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        segment = text[marker.end():next_marker]
        url_prefix = segment[:1000].replace('/katalog/lekturaborowski-pewien-zolnierz/', '/katalog/lektura/borowski-pewien-zolnierz/')
        match = URL.search(url_prefix)
        if match is None:
            raise ValueError(f'Footer {i} lacks canonical URL')
        end = 0
        # Separators and body whitespace are retained; footer paragraphs alone
        # are consumed until the first unrecognized paragraph.
        for paragraph in re.finditer(r'.*?(?:\n\n+|\Z)', segment, re.DOTALL):
            value = paragraph.group().strip()
            if not value or value.startswith(FOOTER_PREFIXES):
                end = paragraph.end()
            else:
                break
        body = text[body_start:marker.start()]
        # Exact generator separator immediately preceding this footer.
        if body.endswith('-----\n'):
            body = body[:-6]
        yield dict(index=i, url='https://wolnelektury.pl/katalog/lektura/' + match.group(1) + '/',
                   text=body, text_sha256=digest(body), footer_chars=len(MARKER) + end)
        body_start = marker.end() + end
    if text[body_start:].strip():
        raise ValueError('Trailing text after final footer cannot be assigned to a work')


def prepare(archive, tokenizer_path, output):
    import numpy as np
    from tokenizers import Tokenizer
    started = time.monotonic()
    archive, tokenizer_path, out = map(Path, (archive, tokenizer_path, output))
    with archive.open('rb') as f:
        source_hash = hashlib.file_digest(f, 'sha256').hexdigest()
    if source_hash != ARCHIVE_SHA256:
        raise ValueError('Archive does not match the audited historical snapshot')
    if out.exists():
        raise FileExistsError('Output exists; choose a new dataset directory')
    with zipfile.ZipFile(archive) as z:
        raw = z.read('wolnelektury.txt')
    rows = list(records(raw.decode('utf-8')))
    # Union URLs that contain exactly identical nonempty body strings.
    parents = {r['url']: r['url'] for r in rows}
    def root(url):
        while parents[url] != url:
            parents[url] = parents[parents[url]]
            url = parents[url]
        return url
    seen = {}
    for row in rows:
        if not row['text'].strip():
            continue
        key = row['text_sha256']
        if key in seen:
            a, b = sorted((root(row['url']), root(seen[key])))
            parents[b] = a
        seen[key] = row['url']
    for row in rows:
        row['group'] = root(row['url'])
        bucket = int(digest(row['group'])[:16], 16) % 1000
        row['split'] = 'test' if bucket < 50 else 'dev' if bucket < 100 else 'train'
    tok = Tokenizer.from_file(str(tokenizer_path))
    eod = tok.token_to_id('<|endoftext|>')
    if eod is None or tok.get_vocab_size() > 65536:
        raise ValueError('Expected uint16-compatible tokenizer with EOD')
    out.mkdir(parents=True)
    shutil.copyfile(tokenizer_path, out / 'tokenizer.json')
    counts = {}
    handles = {s: (out / f'{s}.jsonl').open('w', encoding='utf-8') for s in ('train', 'dev', 'test')}
    binaries = {s: (out / f'{s}.bin').open('wb') for s in handles}
    hashes = {s: hashlib.sha256() for s in handles}
    counts = {s: dict(tokens=0, articles=0, utf8_bytes=0) for s in handles}
    excluded = []
    try:
        for i, row in enumerate(rows):
            if not row['text'].strip() or row['text'].strip() == 'None':
                excluded.append(dict(index=row['index'], url=row['url'], reason='empty or literal None body'))
                continue
            split = row['split']
            ids = tok.encode(row['text'], add_special_tokens=False).ids
            if tok.decode(ids, skip_special_tokens=False) != row['text']:
                raise ValueError(f"Round-trip failure at {row['url']}")
            blob = np.asarray(ids + [eod], dtype='<u2').tobytes()
            binaries[split].write(blob)
            hashes[split].update(blob)
            handles[split].write(json.dumps(row, ensure_ascii=False) + '\n')
            counts[split]['tokens'] += len(ids) + 1
            counts[split]['articles'] += 1
            counts[split]['utf8_bytes'] += len(row['text'].encode('utf-8'))
            if (i + 1) % 250 == 0:
                print('Prepared', i + 1, '/', len(rows), 'records;', round(time.monotonic() - started, 1), 'seconds', flush=True)
    finally:
        for f in [*handles.values(), *binaries.values()]:
            f.close()
    for split, stats in counts.items():
        stats.update(sha256=hashes[split].hexdigest(), tokens_per_utf8_byte=stats['tokens'] / stats['utf8_bytes'],
                     canonical_urls=len({r['url'] for r in rows if r['split'] == split and r['text'].strip() not in ('', 'None')}))
    extraction = dict(
        source=str(archive.relative_to(ROOT)) if archive.is_relative_to(ROOT) else str(archive),
        source_sha256=source_hash, source_bytes=archive.stat().st_size,
        archive_member='wolnelektury.txt', archive_member_sha256=hashlib.sha256(raw).hexdigest(),
        historical_snapshot=True, snapshot_date='not recorded in archive',
        records=len(rows), canonical_urls=len(parents), kept_records=sum(s['articles'] for s in counts.values()),
        url_normalization='https scheme, remove www, trailing slash; repair one source typo lekturaborowski-pewien-zolnierz to lektura/borowski-pewien-zolnierz',
        excluded=excluded, footer_chars_removed=sum(r['footer_chars'] for r in rows),
        extraction='Consecutive recognized footer paragraphs removed at exact footer markers; original body paragraphs retained; exact trailing five-dash footer separator removed.',
        split='SHA256(canonical URL group) first16 hex modulo1000: test0-49, dev50-99, train100-999. Repeated canonical URLs and exact-body duplicates unioned before splitting.',
        limitations=['Historical concatenated archive, not the current complete catalogue.',
                     'Includes non-Polish works present in this snapshot; no language filter.',
                     'Some source entries have no body and are excluded, not reconstructed.',
                     'No semantic deduplication of overlapping anthology/chapter texts under different URLs.',
                     'Unknown trailing footer material is conservatively retained with the following body.'],
        counts=counts)
    manifest = dict(vocab_size=tok.get_vocab_size(), eod_id=eod, dtype='little-endian uint16',
                    tokenizer_sha256=hashlib.sha256((out / 'tokenizer.json').read_bytes()).hexdigest(),
                    source_label='Historical Falenty Wolne Lektury archive; original literary bodies, not the current complete catalogue',
                    tokenizer_origin='Wiki20260901 8k BPE reused, not trained on WL',
                    generation_prompts=['— Nie wiem,', 'Był piękny', 'W tej chwili', 'Na brzegu rzeki'],
                    quality_prompts=['— Nie wiem,', 'Był piękny', 'W tej chwili', 'Na brzegu rzeki',
                                     'Kiedy wrócił do domu,', 'Nagle usłyszała', 'W ciemnym lesie', 'Nie mogłem zrozumieć,'],
                    extraction=extraction, splits=counts,
                    packing='Retained whole-work body plus one EOD; training windows may cross EOD boundaries',
                    seconds=time.monotonic() - started)
    (out / 'extraction.json').write_text(json.dumps(extraction, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'tokens.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(dict(splits=counts, seconds=manifest['seconds'], excluded=len(excluded)), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT / 'data/scratch-corpora/falenty-wl/wolnelektury.zip')
    parser.add_argument('--tokenizer', type=Path, default=ROOT / 'data/wiki-scratch-v1/tokenizer.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'data/wl-scratch-v1')
    args = parser.parse_args()
    prepare(args.archive, args.tokenizer, args.output)
