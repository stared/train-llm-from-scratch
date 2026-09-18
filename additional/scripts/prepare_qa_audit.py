# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Freeze a fresh wording audit of known facts; never add these prompts to training."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = [
    'Nie znam hasła „{title}”. Wyjaśnisz je krótko?',
    'Poproszę jednozdaniową definicję: {title}.',
    'Hasło do objaśnienia: {title}.',
    'Pomóż mi zrozumieć hasło „{title}”.',
    'Co mogę powiedzieć komuś, kto pyta o „{title}”?',
    'Chcę wiedzieć, co kryje się pod hasłem „{title}”.',
    'Dokończ krótką definicję hasła „{title}”: ',
    'Krótko: {title}.',
    'Jak objaśnić hasło „{title}” w encyklopedii?',
    'Przygotuj fiszkę z definicją hasła „{title}”.',
]


def prepare():
    folder = ROOT / 'datasets/local/wiki-short-qa'
    raw = (folder / 'data.json').read_bytes()
    old_raw = (folder / 'known-probes.json').read_bytes()
    data = json.loads(raw)
    old = json.loads(old_raw)
    excluded = {r['id'].split(':known-')[0] for rows in old.values() for r in rows}
    available = sorted((r for r in data['train'] if r['id'] not in excluded),
                       key=lambda r: hashlib.sha256(r['id'].encode()).hexdigest())[:200]
    assert len(available) == 200
    training_prompts = {r['prompt'] for r in json.loads(
        (ROOT / 'datasets/local/wiki-short-qa-varied/data.json').read_text())['train']}
    probes = {}
    for split, rows in [('dev', available[:100]), ('test', available[100:])]:
        probes[split] = [dict(id=r['id']+':known-audit-'+split, title=r['title'],
            prompt=TEMPLATES[i % len(TEMPLATES)].format(title=r['title']),
            answer=r['answer'], source_url=r['url']) for i, r in enumerate(rows)]
    assert all(r['prompt'] not in training_prompts for rows in probes.values() for r in rows)
    output = json.dumps(probes, ensure_ascii=False, indent=2)+'\n'
    path = folder / 'known-audit.json'
    if path.exists() and path.read_text() != output:
        raise ValueError('Existing audit differs; preserve the frozen version')
    path.write_text(output)
    note = dict(source_sha256=hashlib.sha256(raw).hexdigest(),
        earlier_probes_sha256=hashlib.sha256(old_raw).hexdigest(),
        audit_sha256=hashlib.sha256(output.encode()).hexdigest(),
        templates=TEMPLATES, examples=200, disjoint_from_earlier_probe_facts=True,
        purpose='Fresh wording audit of known training facts, frozen before its inference. Both dev/test-labelled halves are audit-only; neither selects or tunes checkpoints. Not unseen-knowledge evaluation.')
    (folder / 'known-audit-manifest.json').write_text(json.dumps(note, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(note, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    prepare()
