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
parser.add_argument('--train-size',type=int,default=5000)
parser.add_argument('--output',type=Path)
parser.add_argument('--short-answers',action='store_true',help='For popular articles, teach a short definition rather than a full paragraph')
args=parser.parse_args()
if not 1<=args.train_size<=200000:parser.error('Training size must be 1–200000')
if args.train_size!=5000 and args.output is None:parser.error('Use a separate --output for a new training size')
if args.short_answers and (not args.popular or args.output is None):parser.error('Short answers require --popular and a separate --output')
source=ROOT/('datasets/local/wiki-popular-v1' if args.popular else 'datasets/local/wiki-leads-v1')
out=args.output or ROOT/('datasets/local/wiki-popular-qa' if args.popular else 'datasets/local/wiki-qa-research');out.mkdir(parents=True,exist_ok=True)
tok=Tokenizer.from_file(str(ROOT/'datasets/wiki-tokenizer.json'))
data={};manifest={}
for split,n in [('train',10000 if args.popular else args.train_size),('dev',200),('test',200)]:
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
            if args.popular or args.train_size!=5000:
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
            if args.short_answers:
                definition=next((m for m in re.finditer(r'\s[–—]\s(?=[a-ząćęłńóśźż])',plain)
                                 if plain[:m.start()].count('(')==plain[:m.start()].count(')')),None)
                if not definition:continue
                prefix=plain[:definition.start()]
                short=re.split(r'[,;]|(?<=[.!?])\s',plain[definition.end():],maxsplit=1)[0].strip()
                if len(short)<8 or len(tok.encode(short).ids)>48 or re.search(r'[{}\[\]|]',short) or short.count('(')!=short.count(')'):continue
                plain=short[0].upper()+short[1:].rstrip('.')+'.'
                person=bool(re.search(r'\b(?:ur|zm)\.',prefix))
                natural=(('Kim był ' if 'zm.' in prefix else 'Kim jest ')+row['title']+'?') if person else 'Czym jest '+row['title']+'?'
                prompt=[f"Wyjaśnij krótko: {row['title']}.",f"Podaj krótką definicję: {row['title']}.",natural][rank%3]
            if len(tok.encode('Pytanie: '+prompt+'\nOdpowiedź:\n'+plain).ids)>490:continue
            record=dict(id=row['id'],prompt=prompt,answer=plain,url=row['url'],title=row['title'])
            rank=int(hashlib.sha256(row['id'].encode()).hexdigest(),16)
            if len(selected)<n:heapq.heappush(selected,(-rank,row['id'],record))
            elif rank < -selected[0][0]:heapq.heapreplace(selected,(-rank,row['id'],record))
    data[split]=[r for _,_,r in sorted(selected,reverse=True)]
    manifest[split]={'n':len(data[split]),'source':f'{source.name}/{split}.jsonl'}
if args.train_size!=5000:
    seen=set()
    for split in ('test','dev','train'):
        kept=[]
        for row in data[split]:
            key=' '.join(row['answer'].casefold().split())
            if key not in seen:kept.append(row);seen.add(key)
        manifest[split]['removed_exact_answer_duplicates']=len(data[split])-len(kept)
        data[split]=kept;manifest[split]['n']=len(kept)
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
if args.short_answers:
    ranked=sorted(data['train'],key=lambda r:hashlib.sha256(('known-question-v1:'+r['id']).encode()).hexdigest())
    templates=['Co oznacza nazwa «{title}»?','Podaj zwięzły opis hasła «{title}».','Jak krótko opisać «{title}»?','Wyjaśnij w jednym zdaniu, co oznacza «{title}».']
    probes={split:[dict(id=r['id']+':known-'+split,title=r['title'],prompt=templates[i%4].format(title=r['title']),answer=r['answer'],source_url=r['url'])
                   for i,r in enumerate(rows)] for split,rows in [('dev',ranked[:100]),('test',ranked[100:200])]}
    (out/'known-probes.json').write_text(json.dumps(probes,ensure_ascii=False,indent=2)+'\n')
    (out/'known-probes-note.txt').write_text('Known training facts with unseen prompt templates; not unseen-entity or unseen-knowledge evaluation. Fixed before AP training. Exact-answer matching is a strict format-and-recall diagnostic.\n')
(out/'manifest.json').write_text(json.dumps(dict(splits=manifest,source='Polish Wikipedia September 2026',
    license='CC BY-SA; per-article revision links retained',selection=('Training-link-ranked top10000 source articles; first plain paragraph, shortened at last sentence-like boundary if over context; three fixed prompt templates selected by article hash' if args.popular else 'Lowest SHA256 article IDs after plain first-paragraph and length filtering'),
    requested_training_size=10000 if args.popular else args.train_size,
    prompt_templates=3 if args.popular or args.train_size!=5000 else 1,
    exact_answer_deduplication=args.train_size!=5000,
    answer_style='First definition clause after the title/date prefix' if args.short_answers else 'First plain paragraph, bounded by context',
    purpose='Title-to-definition SFT. Held-out entities use original pretraining dev/test splits; this does not test arbitrary chat. Familiar-entity diagnostics may be present in training and measure recall, not unseen knowledge.'),indent=2))
print(manifest)
