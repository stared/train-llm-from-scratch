# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Make an offline curve and before/after report from a scratch, poetry or Prawko run."""
import argparse
from html import escape
import json
from pathlib import Path


def chart(series, xlabel, ylabel):
    points = [p for _, rows in series for p in rows]
    if not points:
        return '<p>No curve recorded.</p>'
    xmax = max(1, max(x for x, y in points))
    ymin = min(0, min(y for x, y in points))
    ymax = max(y for x, y in points)
    if ymax <= ymin or any(word in ylabel.lower() for word in ('accuracy','success','reward')):
        ymax = max(1., ymax)
    x = lambda v: 65 + 760 * v / xmax
    y = lambda v: 260 - 220 * (v - ymin) / (ymax - ymin)
    parts = ['<svg viewBox="0 0 860 315" role="img" aria-label="Training curve">']
    for i in range(5):
        v = ymin + (ymax-ymin)*i/4
        parts.append(f'<path d="M65 {y(v)} H825" stroke="#ddd"/><text x="5" y="{y(v)}">{v:.2f}</text>')
        t = xmax*i/4
        parts.append(f'<text x="{x(t)}" y="280" text-anchor="middle">{t:g}</text>')
    for (name, rows), color in zip(series, ['#2067b0', '#d04b16']):
        coords = ' '.join(f'{x(a)},{y(b)}' for a,b in rows)
        parts.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="2"/>')
        for a,b in rows:
            parts.append(f'<circle cx="{x(a)}" cy="{y(b)}" r="2" fill="{color}"><title>{escape(name)}: {b:.4f} at {a:.1f}</title></circle>')
    parts.append(f'<text x="65" y="20">{escape(ylabel)}</text><text x="420" y="310">{escape(xlabel)}</text></svg>')
    legend = ''.join(f'<li style="color:{color}">{escape(name)}</li>' for (name,_),color in zip(series,['#2067b0','#d04b16']))
    return ''.join(parts) + '<ul>' + legend + '</ul>'


def render(folder):
    folder = Path(folder)
    def read(name):
        return json.loads((folder/name).read_text())
    def pairs(before, after, key):
        by_key = {r[key]: r for r in after}
        if set(by_key) != {r[key] for r in before}:
            raise ValueError('Before/after examples do not match')
        return [(b, by_key[b[key]]) for b in before]
    if (folder/'samples_before.json').exists():
        r = read('result.json')
        title = r['model'] + ' — random weights → pretrained'
        source = r['source']
        h, c = read('history.json'), read('checkpoints.json')
        curve = chart([('Training batch loss', [(v['elapsed_seconds'],v['loss']) for v in h]),
            ('Development loss', [(0,r['before']['dev']['loss_nats'])] + [(v['elapsed_seconds'],v['loss_nats']) for v in c] + [(r['training_seconds'],r['final']['dev']['loss_nats'])])], 'Seconds', 'Cross entropy (lower is better)')
        examples = [(b['prompt'], b['continuation'], a['continuation']) for b,a in pairs(read('samples_before.json'),read('samples_selected.json'),'prompt')]
        note = f"After: checkpoint selected by development loss, step {r['best_step']}. Test loss: {r['before']['test']['loss_nats']:.3f} → {r['selected']['test']['loss_nats']:.3f}."
    elif (folder/'style_result.json').exists():
        r = read('style_result.json')
        title = r['model'] + ' — original → SFT'
        d = read('dataset.json')
        source = f"{d.get('examples', r['examples'])} training pairs; {json.dumps(d.get('teacher', r['teacher']), ensure_ascii=False)}"
        curve = chart([('Training batch loss', [(v['step'],v['loss']) for v in read('loss.json')])], 'Updates', 'Answer cross entropy (lower is better)')
        examples = [(b['prompt'], b['answer'], a['answer']) for b,a in pairs(read('base.json'),read('finetuned.json'),'prompt')]
        note = 'After: final adapter. This curve is training loss, not held-out quality; read the answers for meaning and meter.'
    elif (folder/'rollouts.json').exists():
        r = read('result.json')
        title = r['model_spec']['id'] + ' — original → RLVR / ' + r['task']
        source = r['training_data']
        checkpoints = read('checkpoint_selection.json')['checkpoints'] if (folder/'checkpoint_selection.json').exists() else []
        start = r['before']['dev']
        points = [(0, start['successes']/start['n'])] + [(v['step'],v['successes']/v['n']) for v in checkpoints]
        if not checkpoints:
            end = r['after']['dev']
            points.append((r['steps'],end['successes']/end['n']))
        curve = chart([('Development constraint success', points)], 'Updates', 'Success fraction (higher is better)')
        examples = [(b['prompt'], b['text'], a['text']) for b,a in pairs(read('before_test.json'),read('after_test.json'),'id')]
        note = f"Test constraints: {r['before']['test']['successes']}/{r['before']['test']['n']} → {r['after']['test']['successes']}/{r['after']['test']['n']}. Checkpoint selection uses development data. Constraint success does not measure story quality."
    elif (folder/'before_test.json').exists():
        r = read('result.json')
        title = r['model_spec']['id'] + ' — original → ' + r['method'].upper()
        source = r['training_data']
        c = read('checkpoints.json') if (folder/'checkpoints.json').exists() else []
        curve = chart([('Development accuracy', [(0,r['before']['dev']['accuracy'])] + [(v['epoch'],v['accuracy']) for v in c])], 'Epochs', 'Accuracy (higher is better)')
        after = read('after_test.json') if (folder/'after_test.json').exists() else read('before_test.json')
        examples = [(b['question']+'\n'+'\n'.join(f'{letter}. {option}' for letter,option in zip('ABC',b['options']))+'\nKey: '+b['answer'],b['prediction'],a['prediction']) for b,a in pairs(read('before_test.json'),after,'id')]
        score = r.get('after', r['before'])['test']
        note = f"After: development-selected adapter (or unchanged baseline for screen). Test: {r['before']['test']['correct']}/{score['n']} → {score['correct']}/{score['n']}."
    else:
        raise ValueError('Expected a completed scratch, poetry or Prawko run directory')
    body = f'<h1>{escape(title)}</h1><p>Data: {escape(source)}</p><p>{escape(note)}</p>{curve}<h2>Same inputs, before and after</h2>'
    for prompt,before,after in examples:
        body += f'<h3>{escape(prompt)}</h3><div class="pair"><section><b>Before</b><pre>{escape(before)}</pre></section><section><b>After</b><pre>{escape(after)}</pre></section></div>'
    output = folder/'report.html'
    output.write_text('<!doctype html><meta charset="utf-8"><title>Training report</title><style>body{font:16px system-ui;max-width:1100px;margin:32px auto;padding:0 16px}svg{max-width:860px;width:100%}text{font:13px system-ui}pre{white-space:pre-wrap;overflow-wrap:anywhere}h3{white-space:pre-wrap}.pair{display:grid;grid-template-columns:1fr 1fr;gap:24px}section{min-width:0;background:#f4f6f8;padding:16px}@media(max-width:650px){.pair{grid-template-columns:1fr}}</style>'+body, encoding='utf-8')
    return output


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('run', type=Path, help='The Saved runs/... directory printed by training')
    print('Open in your browser:', render(p.parse_args().run))
