# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Extract original article wikitext, train BPE, tokenize the full corpus.

XML decoding only: links/templates/ref tags/tables remain in article text.
Corpus preparation is CPU work, separate from GPU rental.
"""
import argparse
import bz2
import hashlib
import heapq
import json
from pathlib import Path
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def save(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2))


def article_split(text):
    # Identical article texts are assigned together, including duplicate redirects.
    digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
    bucket = int(digest[:16], 16) % 1000
    return ('test' if bucket < 5 else 'dev' if bucket < 10 else 'train'), digest


def iter_articles(path):
    """Main namespace only, original wikitext including redirects; bounded memory."""
    opener = bz2.open if str(path).endswith('.bz2') else open
    with opener(path, 'rb') as stream:
        events = ET.iterparse(stream, events=('start', 'end'))
        _, root = next(events)
        namespace = root.tag.split('}')[0] + '}' if '}' in root.tag else ''
        for event, page in events:
            if event != 'end' or page.tag != namespace + 'page':
                continue
            if page.findtext(namespace+'ns') == '0':
                revision = page.find(namespace+'revision')
                text = revision.findtext(namespace+'text') if revision is not None else None
                model = revision.findtext(namespace+'model') if revision is not None else None
                if text and model in (None, 'wikitext'):
                    revision_id = revision.findtext(namespace+'id')
                    page_id = page.findtext(namespace+'id')
                    yield dict(id=page.findtext(namespace+'id'), title=page.findtext(namespace+'title'),
                               revision_id=revision_id,
                               url='https://pl.wikipedia.org/w/index.php?'+('oldid='+revision_id if revision_id else 'curid='+page_id),
                               redirect=page.find(namespace+'redirect') is not None, text=text)
            root.clear()


def extract(source, output, verify=True):
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    if verify:
        item = json.loads((ROOT/'research/scratch/sources.json').read_text())['sources']['wikipedia-pl-20260901']['files'][0]
        from download_scratch_corpus import verify as verify_file
        verify_file(Path(source), item)
    counts = {s: dict(articles=0, utf8_bytes=0, redirects=0) for s in ('train','dev','test')}
    files = {s: (out/f'{s}.jsonl').open('w') for s in counts}
    sample = []
    try:
        for i, row in enumerate(iter_articles(source), 1):
            split, digest = article_split(row['text'])
            row['text_sha256'] = digest
            files[split].write(json.dumps(row,ensure_ascii=False)+'\n')
            counts[split]['articles'] += 1
            counts[split]['utf8_bytes'] += len(row['text'].encode('utf-8'))
            counts[split]['redirects'] += int(row['redirect'])
            if split == 'train':
                # Uniform hash sample of article IDs, capped text per article.
                rank = int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
                entry = (-rank, row['id'], row['text'][:8192])
                if len(sample) < 2048:
                    heapq.heappush(sample,entry)
                elif rank < -sample[0][0]:
                    heapq.heapreplace(sample,entry)
            if i % 100000 == 0:
                print('Extracted',i,'articles;',round(time.monotonic()-started,1),'seconds',flush=True)
    finally:
        for file in files.values():
            file.close()
    with (out/'tokenizer_sample.jsonl').open('w') as f:
        for _, qid, text in sorted(sample,reverse=True):
            f.write(json.dumps(dict(id=qid,text=text),ensure_ascii=False)+'\n')
    manifest = dict(source=str(source), snapshot='20260901', counts=counts,
        source_url=item['url'] if verify else None, source_sha1=item['checksum'] if verify else None,
        extraction='Namespace0 nonempty wikitext; XML decoded once; original text retained including redirects and markup',
        split='SHA256 of exact article text modulo1000; test0-4, dev5-9, train10-999; duplicate texts stay together',
        tokenizer_sample='2048 training article IDs with smallest SHA256 rank, first8192 characters each',
        tokenizer_sample_articles=len(sample), seconds=time.monotonic()-started)
    save(out/'extraction.json',manifest)
    print(json.dumps(manifest),flush=True)


def tokenize(output):
    import numpy as np
    from tokenizers import Tokenizer, models, trainers, pre_tokenizers, decoders
    out = Path(output)
    if not (out/'extraction.json').exists():
        raise ValueError('Extraction must finish before tokenization')
    if (out/'tokens.json').exists():
        raise FileExistsError('Token files already prepared')
    started = time.monotonic()
    tok = Tokenizer(models.BPE())
    tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tok.decoder = decoders.ByteLevel()
    trainer = trainers.BpeTrainer(vocab_size=8192, min_frequency=2,
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet(), special_tokens=['<|endoftext|>'], show_progress=True)
    def sample_texts():
        with (out/'tokenizer_sample.jsonl').open() as f:
            for line in f:
                yield json.loads(line)['text']
    tok.train_from_iterator(sample_texts(),trainer=trainer)
    tok.save(str(out/'tokenizer.json'))
    end = tok.token_to_id('<|endoftext|>')
    counts = {}
    for split in ('dev','test','train'):
        size = docs = raw_bytes = 0
        digest = hashlib.sha256()
        with (out/f'{split}.jsonl').open() as source, (out/f'{split}.bin').open('wb') as target:
            batch = []
            def flush(rows):
                nonlocal size, docs, raw_bytes
                texts = [r['text'] for r in rows]
                encoded = tok.encode_batch(texts,add_special_tokens=False)
                for row, text, encoding in zip(rows,texts,encoded):
                    # Verify no normalization, dropped markup or altered whitespace.
                    if tok.decode(encoding.ids,skip_special_tokens=False) != text:
                        raise ValueError(f"Tokenizer does not round-trip article {row['id']}")
                    arr = np.asarray(encoding.ids+[end],dtype='<u2')
                    blob = arr.tobytes();target.write(blob);digest.update(blob)
                    size += len(arr);docs += 1;raw_bytes += len(text.encode('utf-8'))
            for line in source:
                batch.append(json.loads(line))
                if len(batch) == 256:
                    flush(batch);batch=[]
                    if docs % 100096 == 0:
                        print('Tokenized',split,docs,'articles;',size,'tokens',flush=True)
            if batch:
                flush(batch)
        counts[split]=dict(tokens=size,articles=docs,utf8_bytes=raw_bytes,sha256=digest.hexdigest(),
                           tokens_per_utf8_byte=size/raw_bytes)
        print(split,json.dumps(counts[split]),flush=True)
    save(out/'tokens.json',dict(vocab_size=tok.get_vocab_size(),eod_id=end,dtype='little-endian uint16',
        extraction=json.loads((out/'extraction.json').read_text()),
        tokenizer_sha256=hashlib.sha256((out/'tokenizer.json').read_bytes()).hexdigest(),splits=counts,
        packing='Original wikitext + one EOD token per article; causal windows may cross EOD boundaries',
        seconds=time.monotonic()-started))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--stage',choices=['extract','tokenize'],required=True)
    p.add_argument('--source',default=ROOT / 'data/scratch-corpora/wikipedia-pl-20260901/plwiki-20260901-pages-articles.xml.bz2')
    p.add_argument('--output',default=ROOT / 'data/wiki-scratch-v1')
    a=p.parse_args()
    if a.stage=='extract':extract(a.source,a.output)
    else:tokenize(a.output)
