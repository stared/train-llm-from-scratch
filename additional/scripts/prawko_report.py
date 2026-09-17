# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Render every actual held-out A/B/C selection; preserve corrections AND regressions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
import json
from pathlib import Path


def render(paths, output):
    lines = ['# LLM robi prawko — actual results', '',
             'Official July 2026 Polish driving-question catalogue; category B, text-only A/B/C subset.',
             'All outputs below are constrained next-token A/B/C selections, not generated explanations.',
             'Correct answer text comes from the official catalogue. The model outputs only the selected letter.',
             'This is a 40-question held-out subset, not the complete official examination.', '',
             '| Model / training | Train before → after | Test before → after | Rotated test before → after | Training time | Worker estimate |',
             '|---|---:|---:|---:|---:|---:|']
    runs = []
    for path in paths:
        path = Path(path)
        r = json.loads((path/'execution.json').read_text())
        label = f"{r['model_spec']['id']} + {r['method'].upper()} on 100 official questions"
        def counts(split):
            return f"{r['before'][split]['correct']}/{r['before'][split]['n']} → {r['after'][split]['correct']}/{r['after'][split]['n']}"
        lines.append(f"| {label} | {counts('train')} | {counts('test')} | {counts('test_rotated')} | {r['training_seconds']:.1f}s | ${r['estimated_compute_usd']:.4f} |")
        runs.append((path, r, label))
    for path, r, label in runs:
        lines.extend(['', f'## {label}', '', f"Run: `{path.name}`. Base revision: `{r['model_spec']['revision']}`.",
            f"Development-selected epoch {r['selected_epoch']}; {r['selected_steps']} selected updates of {r['steps']} explored updates. Reload matches: {r['reload_matches']}.",
            'Before = original pretrained/instruction model, no workshop adapter. After = fresh adapter trained only on the 100 training questions; no Pan Tadeusz or film training.', ''])
        if 'final' in r:
            lines.extend(['| Checkpoint | Train | Dev | Test | Rotated test |',
                          '|---|---:|---:|---:|---:|'])
            for phase, title in [('before', 'Original'), ('after', 'Development-selected'), ('final', 'Final')]:
                values = [f"{r[phase][s]['correct']}/{r[phase][s]['n']}" for s in ('train', 'dev', 'test', 'test_rotated')]
                lines.append('| ' + title + ' | ' + ' | '.join(values) + ' |')
            lines.append('')
        comparisons = [('after', s) for s in ('test', 'test_rotated')]
        if 'final' in r:
            comparisons.extend(('final', s) for s in ('test', 'test_rotated'))
        for phase, split in comparisons:
            before = json.loads((path/f'before_{split}.json').read_text())
            after = json.loads((path/f'{phase}_{split}.json').read_text())
            improved = sum(not a['correct'] and b['correct'] for a,b in zip(before,after))
            regressed = sum(a['correct'] and not b['correct'] for a,b in zip(before,after))
            checkpoint = 'development-selected' if phase == 'after' else 'final'
            lines.extend([f'### {split}, {checkpoint}: {improved} corrections, {regressed} regressions', ''])
            for a,b in zip(before,after):
                assert a['id']==b['id'] and a['answer']==b['answer']
                lines.extend([f"**Question {a['id']}: {a['question']}**", '',
                    *[f"- {letter}. {text}" for letter,text in zip('ABC',a['options'])], '',
                    f"Original {r['model_spec']['id']}: **{a['prediction']}** {'✓' if a['correct'] else '✗'} → {label} ({checkpoint}): **{b['prediction']}** {'✓' if b['correct'] else '✗'}. Official key: **{a['answer']}**.", ''])
    lines.extend(['## Interpretation', '',
        'Test questions were excluded from adapter training and checkpoint selection. Similar stems were grouped before splitting, using a lexical heuristic; related concepts and unknown base-pretraining exposure remain possible.',
        'Rotated choices are the same questions, not an additional independent test set. One seed and 40 test questions are insufficient for a strong general claim.',
        'Compute estimates exclude startup, builds, storage and any failed workers; they are not billing receipts.', ''])
    Path(output).write_text('\n'.join(lines))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs', nargs='+')
    p.add_argument('--output', default='results/prawko-example-results.md')
    a = p.parse_args()
    render(a.runs,a.output)
