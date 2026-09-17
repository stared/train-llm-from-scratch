# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Add text-only road-licence categories while retaining the original exam holdouts."""
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from prepare_prawko import normalize,NS
source=ROOT/'datasets/local/prawko/source.xlsx'
original_manifest=json.loads((ROOT/'datasets/prawko-v2/manifest.json').read_text())
assert hashlib.sha256(source.read_bytes()).hexdigest()==original_manifest['source_sha256'], 'Unexpected source spreadsheet'
z=zipfile.ZipFile(source)
strings=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS)]
rows=[]
for row in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//m:row',NS)[1:]:
    d={re.sub(r'\d','',c.get('r')):strings[int(c.find('m:v',NS).text)] if c.get('t')=='s'
       else c.findtext('m:v',default='',namespaces=NS) for c in row}
    if d.get('H','').strip() or d.get('G') not in ('A','B','C') or d.get('K')=='PT':continue
    if not all(d.get(k,'').strip() for k in 'CDEF'):continue
    rows.append(dict(id=d['B'],question=d['C'],options=[d[k] for k in 'DEF'],answer='ABC'.index(d['G']),
                     categories=d.get('K','')))
original=json.loads((ROOT/'datasets/prawko-v2/data.json').read_text())
held={r['id'] for split in ('dev','test') for r in original[split]}
parents=list(range(len(rows)));normalized=[normalize(r['question']) for r in rows]
def root(i):
    while parents[i]!=i:
        parents[i]=parents[parents[i]];i=parents[i]
    return i
for i,a in enumerate(normalized):
    for j,b in enumerate(normalized[:i]):
        ab=SequenceMatcher(None,a,b)
        if ab.quick_ratio()<.72:continue
        if max(ab.ratio(),SequenceMatcher(None,b,a).ratio())>=.72:parents[root(i)]=root(j)
excluded_roots={root(i) for i,r in enumerate(rows) if r['id'] in held}
training=[r for i,r in enumerate(rows) if root(i) not in excluded_roots]
data=dict(train=training,dev=original['dev'],test=original['test'])
assert not held.intersection(r['id'] for r in training)
out=ROOT/'datasets/local/prawko-expanded';out.mkdir(parents=True,exist_ok=True)
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
manifest=dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              train=len(training),dev=len(original['dev']),test=len(original['test']),
              filter='All road-licence categories; exclude tram-only PT, all media and non-three-choice rows',
              isolation='Connected components of bidirectional stem similarity >= .72; remove every component touching original dev/test',
              original_training_retained=len({r['id'] for r in training}&{r['id'] for r in original['train']}))
manifest.update({key:original_manifest[key] for key in ('source_url','source_page','catalogue')})
(out/'manifest.json').write_text(json.dumps(manifest,indent=2));print(manifest)
