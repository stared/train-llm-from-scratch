# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Build a reproducible, text-only category-B subset of the official catalogue."""
import argparse
from collections import Counter
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import random
import re
import xml.etree.ElementTree as ET
import zipfile

SOURCE = 'https://www.gov.pl/attachment/a5c6c329-28a5-4274-a1a8-e2813f0a51bd'
PAGE = 'https://www.gov.pl/web/infrastruktura/jak-uzyskac-prawo-jazdy'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def normalize(s):
    return ' '.join(re.findall(r'\w+', s.casefold()))


def build(source, output):
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    raw = Path(source).read_bytes()
    z = zipfile.ZipFile(source)
    strings = [''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', NS)]
    rows = []
    for row in ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//m:row', NS)[1:]:
        d = {re.sub(r'\d', '', c.get('r')): strings[int(c.find('m:v', NS).text)] if c.get('t') == 's'
             else c.findtext('m:v', default='', namespaces=NS) for c in row}
        if 'B' not in d.get('K', '').split(',') or d.get('H', '').strip() or d.get('G') not in ('A', 'B', 'C'):
            continue
        if not all(d.get(k, '').strip() for k in ('C', 'D', 'E', 'F')):
            continue
        rows.append(dict(id=d['B'], question=d['C'], options=[d[k] for k in 'DEF'],
                         answer='ABC'.index(d['G']), points=int(d['J']),
                         english_question=d.get('P'), english_options=[d.get(k) for k in 'QRS']))
    # Group similar question stems BEFORE splitting, including transitive matches.
    # Heuristic, not a guarantee of semantic independence; retain groups for review.
    parents = list(range(len(rows)))
    def root(i):
        while parents[i] != i:
            i = parents[i]
        return i
    for i, a in enumerate(rows):
        for j, b in enumerate(rows[:i]):
            if max(SequenceMatcher(None, normalize(a['question']), normalize(b['question'])).ratio(),
                   SequenceMatcher(None, normalize(b['question']), normalize(a['question'])).ratio()) >= .72:
                parents[root(i)] = root(j)
    groups = {}
    for i, row in enumerate(rows):
        groups.setdefault(root(i), []).append(row)
    buckets = list(groups.values())
    random.Random(20260908).shuffle(buckets)
    splits = {'test': [], 'dev': [], 'train': []}
    for group in buckets:
        split = 'test' if len(splits['test']) < 40 else 'dev' if len(splits['dev']) < 24 else 'train'
        splits[split].extend(group)
    for split, entries in splits.items():
        for row in entries:
            row['split'] = split
    manifest = dict(source_url=SOURCE, source_page=PAGE, catalogue='July 2026',
                    source_sha256=hashlib.sha256(raw).hexdigest(), seed=20260908,
                    filter='Category B; empty Media field; three nonempty options; A/B/C answer key',
                    grouping='Connected components of normalized question-stem max bidirectional SequenceMatcher ratio >= 0.72',
                    counts={k: len(v) for k, v in splits.items()},
                    answer_counts={k: dict(Counter('ABC'[r['answer']] for r in v)) for k, v in splits.items()},
                    groups=[[r['id'] for r in g] for g in buckets])
    (out / 'data.json').write_text(json.dumps(splits, ensure_ascii=False, indent=2))
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    (out / 'source.xlsx').write_bytes(raw)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source')
    p.add_argument('--output', default='datasets/prawko-v2')
    a = p.parse_args()
    build(a.source, a.output)
