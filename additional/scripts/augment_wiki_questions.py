# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Vary question wording while retaining the exact short Wikipedia answers and splits."""
import argparse
import hashlib
import json
from pathlib import Path

TEMPLATES=[
    'Co wiesz o {title}?',
    'Napisz krótko o {title}.',
    'Wyjaśnij hasło „{title}”.',
    'Przedstaw {title} w kilku słowach.',
    'Jak zdefiniować „{title}”?',
    'Interesuje mnie {title}. Opisz to krótko.',
    'Potrzebuję krótkiej definicji: {title}.',
]


def augment(source,output):
    raw=source.read_bytes();data=json.loads(raw);originals=data['train'];rows=[]
    for row in originals:
        prompts=[row['prompt']]+[t.format(title=row['title']) for t in TEMPLATES]
        assert len(set(prompts))==8
        for i,prompt in enumerate(prompts):
            rows.append(dict(row,id=f"{row['id']}:wording-{i}",fact_id=row['id'],prompt=prompt))
    data['train']=rows
    output.mkdir(parents=True,exist_ok=True)
    (output/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    manifest=dict(source=source.parent.name,source_sha256=hashlib.sha256(raw).hexdigest(),
        facts=len(originals),variants_per_fact=8,train_rows=len(rows),
        dev=len(data['dev']),test=len(data['test']),additional_templates=TEMPLATES,
        comparison='3.75 passes of this dataset equals 30 mean presentations per fact, matching the original 30-pass budget. Held-out article rows are unchanged. Frozen known-fact probes are evaluated separately; their exact templates are not added.')
    (output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(manifest,ensure_ascii=False,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=Path('datasets/local/wiki-short-qa/data.json'))
    p.add_argument('--output',type=Path,default=Path('datasets/local/wiki-short-qa-varied'))
    a=p.parse_args();augment(a.source,a.output)
