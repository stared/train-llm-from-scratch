# /// script
# requires-python = ">=3.14"
# dependencies = ["tokenizers==0.23.2"]
# ///
"""Pinned Polish Alpaca baseline; prompt-group split, context filter, local data."""
import hashlib
import json
from pathlib import Path
import re
import urllib.request
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'datasets/local/polish-instructions'
REVISION = 'ac0f6728bc6e24895abbe432a3ba04a97d43d1f6'
URL = f'https://huggingface.co/datasets/emplocity/owca/resolve/{REVISION}/alpaca_data_cleaned_pl_emplocity.json'
OUT.mkdir(parents=True, exist_ok=True)
source = OUT / 'alpaca_data_cleaned_pl_emplocity.json'
if not source.exists():
    urllib.request.urlretrieve(URL, source)
tok = Tokenizer.from_file(str(ROOT / 'datasets/wiki-tokenizer.json'))
data = {'train': [], 'dev': [], 'test': []}
seen = set()
rejected = {'duplicate_prompt': 0, 'context_or_empty': 0, 'exam_overlap': 0}
exam = json.loads((ROOT / 'datasets/prawko-v2/extended.json').read_text())
def normalized(s):
    return ' '.join(re.findall(r'\w+', s.lower()))
held = [normalized(r['question']) for split in ('dev', 'test') for r in exam[split]]
for r in json.loads(source.read_text()):
    prompt = r['instruction'].strip() + ('\n' + r['input'].strip() if r['input'].strip() else '')
    answer = r['output'].strip()
    key = normalized(prompt)
    digest = hashlib.sha256(key.encode()).hexdigest()
    if key in seen:
        rejected['duplicate_prompt'] += 1
        continue
    seen.add(key)
    if any(q in normalized(prompt + ' ' + answer) for q in held):
        rejected['exam_overlap'] += 1
        continue
    if not prompt or not answer or len(tok.encode('Pytanie: ' + prompt + '\nOdpowiedź:\n' + answer).ids) > 500:
        rejected['context_or_empty'] += 1
        continue
    bucket = int(digest[:8], 16) % 100
    split = 'test' if bucket == 0 else 'dev' if bucket == 1 else 'train'
    data[split].append(dict(id=digest[:20], prompt=prompt, answer=answer))
for rows in data.values():
    rows.sort(key=lambda r: r['id'])
(OUT / 'data.json').write_text(json.dumps(data, ensure_ascii=False))
manifest = dict(source=URL, revision=REVISION, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    source_license='ODC-By database attribution; see upstream DATA_LICENSE and Alpaca provenance',
    split_sizes={k: len(v) for k, v in data.items()}, rejected=rejected,
    tokenizer_sha256=hashlib.sha256((ROOT / 'datasets/wiki-tokenizer.json').read_bytes()).hexdigest(),
    selection='Unique normalized prompts, SHA256 prompt-group split 98/1/1; <=500 tokens; exact held-out exam question exclusion',
    limitations='Synthetic translated Alpaca. Spot check found factual mistakes (including atom description). Format-learning baseline, not verified knowledge or a guarantee of no semantic exam overlap.')
(OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
print(json.dumps(manifest, ensure_ascii=False, indent=2))
