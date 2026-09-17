# /// script
# requires-python = ">=3.14"
# dependencies = ["mwparserfromhell==0.7.2", "tokenizers==0.23.2"]
# ///
"""Create title-to-definition QA from existing Wikipedia leads, preserving source splits."""
import argparse
import hashlib
import heapq
import json
from pathlib import Path
import re
import sys
import mwparserfromhell
from tokenizers import Tokenizer

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from prepare_wiki_scratch import strip_reference_tags
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--popular',action='store_true')
args=parser.parse_args()
source=ROOT/('datasets/local/wiki-popular-v1' if args.popular else 'datasets/local/wiki-leads-v1')
out=ROOT/('datasets/local/wiki-popular-qa' if args.popular else 'datasets/local/wiki-qa-research');out.mkdir(parents=True,exist_ok=True)
tok=Tokenizer.from_file(str(ROOT/'datasets/wiki-tokenizer.json'))
data={};manifest={}
for split,n in [('train',10000 if args.popular else 5000),('dev',200),('test',200)]:
    selected=[]
    with (source/f'{split}.jsonl').open() as f:
        for line in f:
            row=json.loads(line)
            rank=int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
            if len(selected)>=n and rank>=-selected[0][0]:continue
            text=strip_reference_tags(row['text'])
            plain=str(mwparserfromhell.parse(text).strip_code()).strip().split('\n\n')[0]
            plain=' '.join(plain.split())
            prompt=f"Co to jest: {row['title']}? Opisz krótko."
            if args.popular:
                templates=['Wyjaśnij hasło: {title}.','Przedstaw krótko hasło: {title}.','Opisz: {title}.']
                prompt=templates[rank%len(templates)].format(title=row['title'])
                budget=490-len(tok.encode('Pytanie: '+prompt+'\nOdpowiedź:\n').ids)
                ids=tok.encode(plain).ids
                if len(ids)>budget:
                    candidate=tok.decode(ids[:budget]);boundaries=list(re.finditer(r'[.!?][”»)]?\s+',candidate))
                    if not boundaries:continue
                    plain=candidate[:boundaries[-1].end()].strip()
                if len(plain)<100:continue
            elif not 100<=len(plain)<=1000:continue
            if len(tok.encode('Pytanie: '+prompt+'\nOdpowiedź:\n'+plain).ids)>490:continue
            record=dict(id=row['id'],prompt=prompt,answer=plain,url=row['url'],title=row['title'])
            rank=int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
            if len(selected)<n:heapq.heappush(selected,(-rank,row['id'],record))
            elif rank < -selected[0][0]:heapq.heapreplace(selected,(-rank,row['id'],record))
    data[split]=[r for _,_,r in sorted(selected,reverse=True)]
    manifest[split]={'n':len(data[split]),'source':f'{source.name}/{split}.jsonl'}
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'manifest.json').write_text(json.dumps(dict(splits=manifest,source='Polish Wikipedia September 2026',
    license='CC BY-SA; per-article revision links retained',selection=('Training-link-ranked top10000 source articles; first plain paragraph, shortened at last sentence-like boundary if over context; three fixed prompt templates selected by article hash' if args.popular else 'Lowest SHA256 article IDs after plain first-paragraph and length filtering'),
    purpose='Title-to-definition SFT. Held-out entities use original pretraining dev/test splits; this does not test arbitrary chat. Familiar-entity diagnostics may be present in training and measure recall, not unseen knowledge.'),indent=2))
print(manifest)
