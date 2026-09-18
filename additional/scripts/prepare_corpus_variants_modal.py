"""Prepare corpus comparisons remotely, preserving existing source splits."""
from pathlib import Path
import modal

app=modal.App('workshop-polish-corpus-variants')
volume=modal.Volume.from_name('model-training-workshop')
ROOT=Path(__file__).resolve().parents[2] if modal.is_local() else Path('/work')
image=(modal.Image.debian_slim(python_version='3.14').pip_install('numpy==2.5.3','tokenizers==0.23.2','mwparserfromhell==0.7.2')
       .add_local_file(str(ROOT/'scripts/prepare_wiki_scratch.py'),'/work/scripts/prepare_wiki_scratch.py')
       .add_local_file(str(ROOT/'additional/scripts/wiki_plain_text.py'),'/work/scripts/wiki_plain_text.py'))

@app.function(image=image,cpu=(8,8),memory=(16384,16384),timeout=7200,retries=0,nonpreemptible=True,volumes={'/persist':volume})
def prepare(variant='plain-leads'):
    import hashlib,json,time
    import numpy as np
    from tokenizers import Tokenizer
    import sys
    sys.path.insert(0,'/work/scripts')
    from wiki_plain_text import clean_wiki_text
    from concurrent.futures import ProcessPoolExecutor
    from contextlib import nullcontext
    from itertools import tee
    if variant=='wolne-lektury-wiki-bpe':return retokenize_literature()
    if variant not in ('plain-leads','plain-full'):raise ValueError('Unknown corpus variant')
    start=time.monotonic()
    full=variant=='plain-full'
    source=Path('/persist/datasets')/('wiki-scratch-v1' if full else 'wiki-leads-v1')
    out=Path('/persist/datasets')/('wiki-plain-full-v1' if full else 'wiki-plain-leads-v2')
    if (out/'tokens.json').exists():return json.loads((out/'tokens.json').read_text())
    out.mkdir(exist_ok=True)
    metadata=json.loads((source/'tokens.json').read_text());tok=Tokenizer.from_file(str(source/'tokenizer.json'))
    eod=metadata['eod_id'];counts={};seen=set();samples=[]
    # Held-out splits first: exact duplicates in later splits are excluded.
    for split in ('test','dev','train'):
        array=np.memmap(source/f'{split}.bin',dtype='<u2',mode='r')
        if len(array)!=metadata['splits'][split]['tokens']:raise ValueError('Token count mismatch')
        with (source/f'{split}.bin').open('rb') as f:
            if hashlib.file_digest(f,'sha256').hexdigest()!=metadata['splits'][split]['sha256']:raise ValueError('Checksum mismatch')
        boundaries=np.flatnonzero(array==eod);tokens=0;articles=0;excluded=0;digest=hashlib.sha256();batch=[]
        def originals():
            begin=0
            for end in boundaries:
                yield tok.decode(array[begin:int(end)].tolist(),skip_special_tokens=False)
                begin=int(end)+1
        with (out/f'{split}.bin').open('wb') as f, (ProcessPoolExecutor(max_workers=6) if full else nullcontext()) as pool:
            def flush():
                nonlocal tokens
                for enc in tok.encode_batch(batch):
                    blob=np.asarray(enc.ids+[eod],dtype='<u2').tobytes();f.write(blob);digest.update(blob);tokens+=len(enc.ids)+1
                batch.clear()
            source_rows,parse_rows=tee(originals())
            cleaned=pool.map(clean_wiki_text,parse_rows,chunksize=32,buffersize=8) if pool else map(clean_wiki_text,parse_rows)
            for original,text in zip(source_rows,cleaned):
                key=hashlib.sha256(text.encode()).digest()
                if len(text)<150 or sum(c.isalpha() for c in text)/len(text)<.5 or key in seen:
                    excluded+=1;continue
                seen.add(key);batch.append(text);articles+=1
                if len(samples)<5:samples.append({'split':split,'before':original,'after':text})
                if len(batch)>=256:flush()
                if articles%10000==0:print(split,articles,'tokens',tokens,'seconds',round(time.monotonic()-start),flush=True)
            flush()
        counts[split]=dict(tokens=tokens,articles=articles,excluded=excluded,sha256=digest.hexdigest())
        print(split,counts[split],flush=True)
    (out/'tokenizer.json').write_bytes((source/'tokenizer.json').read_bytes())
    result=dict(vocab_size=tok.get_vocab_size(),eod_id=eod,dtype='little-endian uint16',
        tokenizer_sha256=metadata['tokenizer_sha256'],splits=counts,source_label='Polish Wikipedia plain '+('full articles' if full else 'leads')+', September 2026',
        source=source.name,generation_prompts=['Warszawa –','Polska –','Język polski','Samochód'],
        preparation='v2: self-closing refs removed before paired refs; mwparserfromhell strip_code; whitespace normalization; >=150 chars and >=50% alphabetic; exact cleaned-text deduplication across splits, priority test/dev/train',
        limitations=('Filtered full article bodies, preserving original train/dev/test assignments. ' if full else 'Filtered leads from >=4000-character articles, not full Wikipedia. ')+
            'Different evaluation distribution from raw markup. Templates are removed with their content; parser is not MediaWiki rendering.',
        seconds=time.monotonic()-start)
    (out/'audit_sample.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2))
    (out/'tokens.json').write_text(json.dumps(result,indent=2));volume.commit();return result

@app.local_entrypoint()
def main(variant: str = 'plain-leads'):
    import json
    result=prepare.remote(variant)
    name={'wolne-lektury-wiki-bpe':'wl-wiki-bpe-v1','plain-leads':'wiki-plain-leads-v2','plain-full':'wiki-plain-full-v1'}[variant]
    out=Path('datasets/local')/name;out.mkdir(exist_ok=True)
    (out/'tokens.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

def retokenize_literature():
    import hashlib,json,time
    import numpy as np
    from tokenizers import Tokenizer
    start=time.monotonic();source=Path('/persist/datasets/wl-scratch-v1');out=Path('/persist/datasets/wl-wiki-bpe-v1')
    if (out/'tokens.json').exists():return json.loads((out/'tokens.json').read_text())
    out.mkdir(exist_ok=True)
    original=json.loads((source/'tokens.json').read_text())
    tokenizer_bytes=Path('/persist/datasets/wiki-scratch-v1/tokenizer.json').read_bytes()
    (out/'tokenizer.json').write_bytes(tokenizer_bytes)
    tok=Tokenizer.from_file(str(out/'tokenizer.json'));eod=tok.token_to_id('<|endoftext|>');splits={}
    for split in ('train','dev','test'):
        tokens=0;documents=0;digest=hashlib.sha256();source_digest=hashlib.sha256()
        with (source/f'{split}.jsonl').open('rb') as rows,(out/f'{split}.bin').open('wb') as target:
            for line in rows:
                source_digest.update(line);row=json.loads(line);text=row['text']
                if hashlib.sha256(text.encode()).hexdigest()!=row['text_sha256']:raise ValueError('Source text hash mismatch')
                ids=tok.encode(text).ids
                if tok.decode(ids,skip_special_tokens=False)!=text:raise ValueError('Tokenizer round-trip mismatch')
                blob=np.asarray(ids+[eod],dtype='<u2').tobytes();target.write(blob);digest.update(blob)
                tokens+=len(ids)+1;documents+=1
                if documents%100==0:print(split,documents,tokens,flush=True)
        splits[split]=dict(tokens=tokens,documents=documents,sha256=digest.hexdigest(),source_jsonl_sha256=source_digest.hexdigest())
    result=dict(vocab_size=tok.get_vocab_size(),eod_id=eod,dtype='little-endian uint16',
        source_label='Wolne Lektury, unchanged source texts and splits, retokenized with Wikipedia BPE',
        tokenizer_origin='Existing Wikipedia 8192-entry BPE',tokenizer_sha256=hashlib.sha256(tokenizer_bytes).hexdigest(),
        source='wl-scratch-v1',splits=splits,generation_prompts=original.get('generation_prompts',[]),
        preparation='Original JSONL rows, content SHA256 and exact tokenizer round-trip verified for every text; one EOD after each source document',
        source_metadata=original,seconds=time.monotonic()-start)
    (out/'tokens.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));volume.commit();return result
