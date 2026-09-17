"""Strip markup from the existing lead corpus remotely, preserving every split."""
from pathlib import Path
import modal

app=modal.App('workshop-wiki-plain-preparation')
volume=modal.Volume.from_name('model-training-workshop')
image=modal.Image.debian_slim(python_version='3.14').pip_install('numpy==2.5.3','tokenizers==0.23.2','mwparserfromhell==0.7.2')

@app.function(image=image,cpu=(4,4),memory=(8192,8192),timeout=3600,retries=0,volumes={'/persist':volume})
def prepare():
    import hashlib,json,re,time
    import numpy as np
    import mwparserfromhell
    from tokenizers import Tokenizer
    start=time.monotonic()
    source=Path('/persist/datasets/wiki-leads-v1');out=Path('/persist/datasets/wiki-plain-leads-v1')
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
        boundaries=np.flatnonzero(array==eod);begin=0;tokens=0;articles=0;excluded=0;digest=hashlib.sha256();batch=[]
        with (out/f'{split}.bin').open('wb') as f:
            def flush():
                nonlocal tokens
                for enc in tok.encode_batch(batch):
                    blob=np.asarray(enc.ids+[eod],dtype='<u2').tobytes();f.write(blob);digest.update(blob);tokens+=len(enc.ids)+1
                batch.clear()
            for end in boundaries:
                original=tok.decode(array[begin:int(end)].tolist(),skip_special_tokens=False);begin=int(end)+1
                text=re.sub(r'<ref\b[^>]*>.*?</ref>|<ref\b[^>]*/>','',original,flags=re.S)
                text=str(mwparserfromhell.parse(text).strip_code(normalize=True,collapse=True))
                text=' '.join(text.split())
                key=hashlib.sha256(text.encode()).digest()
                if len(text)<150 or sum(c.isalpha() for c in text)/len(text)<.5 or key in seen:
                    excluded+=1;continue
                seen.add(key);batch.append(text);articles+=1
                if len(samples)<5:samples.append({'split':split,'before':original,'after':text})
                if len(batch)>=256:flush()
                if articles%10000==0:print(split,articles,round(time.monotonic()-start),flush=True)
            flush()
        counts[split]=dict(tokens=tokens,articles=articles,excluded=excluded,sha256=digest.hexdigest())
        print(split,counts[split],flush=True)
    (out/'tokenizer.json').write_bytes((source/'tokenizer.json').read_bytes())
    result=dict(vocab_size=tok.get_vocab_size(),eod_id=eod,dtype='little-endian uint16',
        tokenizer_sha256=metadata['tokenizer_sha256'],splits=counts,source_label='Polish Wikipedia plain leads, September 2026',
        source='wiki-leads-v1',generation_prompts=['Warszawa –','Polska –','Język polski','Samochód'],
        preparation='mwparserfromhell strip_code after ref removal; whitespace normalization; >=150 chars and >=50% alphabetic; exact cleaned-text deduplication across splits, priority test/dev/train',
        limitations='Filtered leads from >=4000-character articles, not full Wikipedia. Different evaluation distribution from raw markup. Templates are removed with their content; parser is not MediaWiki rendering.',
        seconds=time.monotonic()-start)
    (out/'audit_sample.json').write_text(json.dumps(samples,ensure_ascii=False,indent=2))
    (out/'tokens.json').write_text(json.dumps(result,indent=2));volume.commit();return result

@app.local_entrypoint()
def main():
    import json
    result=prepare.remote();out=Path('datasets/local/wiki-plain-leads-v1');out.mkdir(exist_ok=True)
    (out/'tokens.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
