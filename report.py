"""Read saved results without torch, a GPU, Modal, or model downloads."""
import json
from pathlib import Path
import re
from examples import score


def content_accuracy(path, task):
    rows = json.loads(path.read_text())
    correct = 0
    for row in rows:
        text = row['prediction'].strip()
        if task == 'extraction':
            match = re.fullmatch(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL)
            if match:
                text = match.group(1)
        correct += score(task, text, row['answer'])['correct']
    return correct / len(rows)

print('| Model | Task | Steps | Strict before → after | Content before → after¹ | Train seconds | Remote seconds | Est. compute | Reload |')
print('|---|---|---:|---|---|---:|---:|---:|---|')
for path in sorted(Path('runs').glob('*/result.json')):
    r = json.loads(path.read_text())
    before = content_accuracy(path.parent / 'before.json', r['task'])
    after = content_accuracy(path.parent / 'after.json', r['task'])
    label = r['model']
    if label == 'gemma4-e2b' and 'end_of_turn_token' not in r['model_spec']:
        label += ' (superseded EOS recipe)'
    print(f"| {label} | {r['task']} | {r['completed_steps']} | "
          f"{r['baseline']['correct']:.0%} → {r['after']['correct']:.0%} | "
          f"{before:.0%} → {after:.0%} | {r['training_seconds']:.1f} | "
          f"{r.get('remote_seconds', r['total_seconds']):.1f} | "
          f"${r.get('estimated_compute_usd', 0):.3f} | {r['reload_matches']} |")
print('\n¹ Content scoring only removes a surrounding Markdown JSON fence; field values and types still must match exactly.')
