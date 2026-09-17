# /// script
# requires-python = ">=3.14"
# dependencies = ["mwparserfromhell==0.7.2", "tokenizers==0.23.2"]
# ///
"""Create title-to-definition QA from existing Wikipedia leads, preserving source splits."""
import hashlib
import heapq
import json
from pathlib import Path
import re
import mwparserfromhell
from tokenizers import Tokenizer

ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'datasets/local/wiki-leads-v1'
out=ROOT/'datasets/local/wiki-qa-research';out.mkdir(parents=True,exist_ok=True)
tok=Tokenizer.from_file(str(ROOT/'datasets/wiki-tokenizer.json'))
data={};manifest={}
for split,n in [('train',5000),('dev',200),('test',200)]:
    selected=[]
    with (source/f'{split}.jsonl').open() as f:
        for line in f:
            row=json.loads(line)
            rank=int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
            if len(selected)>=n and rank>=-selected[0][0]:continue
            text=re.sub(r'<ref\b[^>]*>.*?</ref>|<ref\b[^>]*/>', '',row['text'],flags=re.S)
            plain=str(mwparserfromhell.parse(text).strip_code()).strip().split('\n\n')[0]
            plain=' '.join(plain.split())
            if not 100<=len(plain)<=1000:continue
            prompt=f"Co to jest: {row['title']}? Opisz krótko."
            if len(tok.encode('Pytanie: '+prompt+'\nOdpowiedź:\n'+plain).ids)>490:continue
            record=dict(id=row['id'],prompt=prompt,answer=plain,url=row['url'],title=row['title'])
            rank=int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
            if len(selected)<n:heapq.heappush(selected,(-rank,row['id'],record))
            elif rank < -selected[0][0]:heapq.heapreplace(selected,(-rank,row['id'],record))
    data[split]=[r for _,_,r in sorted(selected,reverse=True)]
    manifest[split]={'n':len(data[split]),'source':f'wiki-leads-v1/{split}.jsonl'}
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'manifest.json').write_text(json.dumps(dict(splits=manifest,source='Polish Wikipedia September 2026',
    license='CC BY-SA; per-article revision links retained',selection='Lowest SHA256 article IDs after plain first-paragraph and length filtering',
    purpose='Title-to-definition SFT. Held-out entities use original pretraining dev/test splits; this does not test arbitrary chat.'),indent=2))
print(manifest)
