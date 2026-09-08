"""Select original verse passages and build audited Polish prompt/verse SFT data.

Run with uv run --no-project prepare_pan_tadeusz_qa.py select|build.
The build step uses the committed, individually authored prompts; no model/API call.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import re

SOURCE=Path('datasets/pan-tadeusz-full/train.txt')
OUT=Path('datasets/pan-tadeusz-qa-v1')
BOOK=re.compile(r'Księga (pierwsza|druga|trzecia|czwarta|piąta|szósta|siódma|ósma|dziewiąta|dziesiąta|jedenasta|dwunasta)')

def dump(path,value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def select():
    OUT.mkdir(parents=True,exist_ok=False)
    lines=SOURCE.read_text().splitlines()
    book=0;skip=0;paragraphs=[];paragraph=[]
    for number,line in enumerate(lines,1):
        if BOOK.fullmatch(line):
            if paragraph:paragraphs.append((book,paragraph));paragraph=[]
            book+=1;skip=2;continue
        if line=='Epilog':
            if paragraph:paragraphs.append((book,paragraph));paragraph=[]
            break
        if skip:
            if line:skip-=1
            continue
        if not line:
            if paragraph:paragraphs.append((book,paragraph));paragraph=[]
        elif book:paragraph.append((number,line))
    rng=random.Random(2026)
    candidates=[]
    def sentence_end(line):return bool(re.search(r'[.!?…][»”*\s—–-]*$',line))
    for paragraph_id,(book,paragraph) in enumerate(paragraphs):
        if len(paragraph)<4:continue
        preferred=rng.choices([4,6,8,10,12],[4,3,2,1,1])[0]
        options=[]
        for start in range(0,len(paragraph)-3):
            for length in range(4,13):
                if start+length>len(paragraph):continue
                score=(9*sentence_end(paragraph[start+length-1][1])
                       +3*(start==0 or sentence_end(paragraph[start-1][1]))
                       +1*(start==0)+1*(start+length==len(paragraph))
                       -.35*abs(length-preferred))
                options.append((score,-start,length,start))
        _,_,length,start=max(options)
        chosen=paragraph[start:start+length]
        candidates.append(dict(book=book,paragraph_id=paragraph_id,
                               source_lines=[n for n,_ in chosen],
                               answer='\n'.join(s for _,s in chosen),line_count=length))
    # One passage per paragraph; all twelve books represented. Epilogue omitted:
    # its predominantly eleven-syllable meter differs from the workshop target.
    selected=rng.sample(candidates,500)
    if candidates[0] not in selected:selected[-1]=candidates[0]
    selected.sort(key=lambda r:r['source_lines'][0])
    for i,row in enumerate(selected,1):row['id']=f'pt-{i:04d}'
    dump(OUT/'passages.json',selected)
    dump(OUT/'selection.json',dict(seed=2026,source=str(SOURCE),
        source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        eligible_paragraphs=len(candidates),examples=500,
        by_book=dict(Counter(r['book'] for r in selected)),
        by_lines=dict(Counter(r['line_count'] for r in selected)),
        epilogue_included=False,selection='One nonoverlapping passage per selected paragraph; prefer sentence boundaries, retain original lines exactly.'))
    print(OUT/'passages.json')

def validation_split(rows):
    """Keep repeated verse lines together, even at different source positions."""
    parent=list(range(len(rows)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]];i=parent[i]
        return i
    seen={}
    for i,row in enumerate(rows):
        for line in row['answer'].splitlines():
            key=' '.join(re.sub(r'[^\w\s]','',line.casefold()).split())
            if len(key)<20:continue
            if key in seen:parent[root(i)]=root(seen[key])
            seen[key]=i
    groups={}
    for i,row in enumerate(rows):groups.setdefault(root(i),[]).append(row['id'])
    groups=list(groups.values());random.Random(2026).shuffle(groups)
    choices={0:[]}
    for group in groups:
        for size,chosen in list(choices.items()):
            total=size+len(group)
            if total<=50 and total not in choices:choices[total]=chosen+group
        if 50 in choices:return set(choices[50])
    raise ValueError('Cannot make a 50-example validation split without shared verse lines')

def build():
    passages=json.loads((OUT/'passages.json').read_text())
    selection=json.loads((OUT/'selection.json').read_text())
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==selection['source_sha256'], 'Source changed'
    prompts=json.loads((OUT/'literal_prompts.json').read_text())
    revised=set()
    for line in (OUT/'everyday_overrides.txt').read_text().splitlines():
        key,prompt=line.split('|',1);key='pt-'+key
        assert key in prompts and key not in revised,key
        revised.add(key);prompts[key]=prompt
    dump(OUT/'prompts.json',prompts)
    assert len(passages)==500 and set(prompts)=={r['id'] for r in passages}
    lines=SOURCE.read_text().splitlines();used=set();rows=[]
    for row in passages:
        prompt=prompts[row['id']].strip()
        assert prompt and '\n' not in prompt and 10<=len(prompt)<=250
        assert 4<=row['line_count']<=12
        assert row['answer']=='\n'.join(lines[n-1] for n in row['source_lines'])
        assert not used.intersection(row['source_lines']);used.update(row['source_lines'])
        assert not any(term in prompt.casefold() for term in ('mickiewicz','pan tadeusz','wierszem','zacytuj','fragment','trzynasto'))
        rows.append(dict(**row,prompt=prompt,language='pl',
            prompt_kind='question' if prompt.endswith('?') else 'statement',
            messages=[dict(role='user',content=prompt),dict(role='assistant',content=row['answer'])]))
    assert len({r['prompt'].casefold() for r in rows})==500
    assert len({r['answer'] for r in rows})==500
    validation_ids=validation_split(rows)
    for name,subset in [('examples',rows),('train',[r for r in rows if r['id'] not in validation_ids]),('validation',[r for r in rows if r['id'] in validation_ids])]:
        (OUT/f'{name}.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in subset))
    manifest=dict(style='poetry',languages='pl',examples=450,total_examples=500,validation_examples=50,
        data_sha256=hashlib.sha256((OUT/'train.jsonl').read_bytes()).hexdigest(),
        all_examples_sha256=hashlib.sha256((OUT/'examples.jsonl').read_bytes()).hexdigest(),
        teacher=dict(id='Codex assistant in this session: individually authored Polish prompts; answers verbatim Adam Mickiewicz',revision='pan-tadeusz-qa-v1'),
        source=selection,
        expected_line_range=[4,12],
        prompt_revision=dict(everyday_overrides=len(revised),purpose='Humorous modern setups and relevant ordinary Polish prompts; intentional anachronism and disproportionate literary replies.'),
        recipe='Ordinary Polish question or statement -> exact 4–12 source verse lines. 450 train / 50 validation, disjoint paragraphs and source positions; shared normalized verse lines of 20+ characters grouped into the same split. No style instruction.',
        quality_note='Prompts individually authored after reading passages. Original historical spelling/typographic markers retained. Humorous analogies are intentional, not factual advice. No claim that every source line has exactly 13 syllables. Validation is not held out from earlier full-book adapters; related topics remain across splits.')
    dump(OUT/'dataset.json',manifest)
    evaluation=[dict(id=r['id'],language='pl',prompt=r['prompt']) for r in rows if r['id'] in validation_ids][:12]
    dump(OUT/'evaluation.json',evaluation)
    report='# Pan Tadeusz: 500 ordinary Polish prompts and original verse replies\n\n'
    report+='Prompts authored by the Codex assistant; answers are verbatim source passages, not model-generated poetry. Dataset targets, not generated model results. 450 train / 50 validation.\n\n'
    for row in rows:
        split='validation' if row['id'] in validation_ids else 'train'
        report+=f'## {row["id"]} · book {row["book"]} · {row["line_count"]} lines · {split}\n\n**User:** {row["prompt"]}\n\n**Assistant target — original Pan Tadeusz:**\n\n'+ '  \n'.join('> '+s for s in row['answer'].splitlines())+f'\n\nSource: `{SOURCE}`, lines {row["source_lines"][0]}–{row["source_lines"][-1]}.\n\n'
    (OUT/'REVIEW.md').write_text(report)
    print(json.dumps(dict(examples=500,train=450,validation=50,prompt_kinds=dict(Counter(r['prompt_kind'] for r in rows)),line_counts=dict(Counter(r['line_count'] for r in rows))),ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('stage',choices=['select','build'])
    a=p.parse_args();select() if a.stage=='select' else build()
