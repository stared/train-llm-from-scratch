"""Build a standalone, offline comparison from real saved model outputs."""
import argparse
from html import escape
import json
from pathlib import Path


def render(run):
    result = json.loads((run / 'style_result.json').read_text())
    outputs = {key: json.loads((run / f'{key}.json').read_text())
               for key in ('base', 'prompted', 'finetuned')}
    rows = []
    for index, row in enumerate(outputs['base']):
        cells = ''.join(f'<div><h3>{label}</h3><pre>{escape(outputs[key][index]["answer"])}</pre></div>'
                        for key, label in [('base', 'Before · ordinary question'),
                                           ('prompted', 'Baseline · explicit style prompt'),
                                           ('finetuned', 'After · ordinary question')])
        language = escape(row.get('language', 'unknown'), quote=True)
        rows.append(f'<article data-language="{language}"><h2>{escape(row["prompt"])}</h2><section>{cells}</section></article>')
    decoding = result.get('decoding', {'sample': False})
    mode = 'Sampled, seed 42' if decoding['sample'] else 'Greedy decoding'
    data_label = escape(result.get('teacher', {}).get('id', 'See dataset manifest'))
    training_seconds = result.get('cumulative_training_seconds', result['training_seconds'])
    step_label = 'updates in final segment' if result.get('continued_from') else 'updates'
    return (f'<h1>{escape(result["style"].title())} · {escape(result["model"])} · {mode}</h1>'
            f'<p>Before: untuned base. After: LoRA fine-tuned on <strong>{data_label}</strong>, '
            f'adapter strength {result.get("adapter_scale", 1.0):.0%}. '
            f'Dataset SHA-256: <code>{escape(result["data_sha256"])}</code>.</p>'
            f'<p>{result["examples"]} training examples · {result["steps"]} {step_label} · '
            f'{training_seconds/60:.1f} minutes total training · '
            f'original training reload matched: {result["reload_matches"]}</p>'
            f'<p class="source">Source: {escape(str(run))}. Every evaluation prompt is shown. '
            'Judge humor, relevance, language and originality separately; line count is not quality.</p>'
            + ''.join(rows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('runs', nargs='+', type=Path)
    parser.add_argument('--output', type=Path, default=Path('SHOWCASE.html'))
    args = parser.parse_args()
    body = ''.join(render(run) for run in args.runs)
    args.output.write_text('''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Teach a model a voice</title>
<style>
body{max-width:1500px;margin:40px auto;padding:0 24px;background:#f5f2ec;color:#202b32;font:17px/1.6 system-ui}
h1{font-size:2.5rem;margin-top:60px}h2{font-size:1.15rem}h3{font-size:.85rem;text-transform:uppercase;color:#476d65}
article{margin:32px 0;padding:24px;background:white;border-radius:12px;border:1px solid #dcded8}
section{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px}
pre{white-space:pre-wrap;overflow-wrap:anywhere;font:16px/1.7 Georgia,serif;margin:0}
.source{color:#647077;font-size:.85rem}section>div:last-child{border-top:3px solid #319b79}
button{font:inherit;padding:8px 18px;margin-right:8px;background:white;border:1px solid #99aaa3;border-radius:6px;cursor:pointer}
button:focus{outline:3px solid #319b79}
@media(max-width:900px){section{grid-template-columns:1fr}h1{font-size:1.8rem}}
@media print{article{break-inside:avoid}body{padding:0}.filters{display:none}}
</style><p>Warsaw Model Trainers · English workshop · Experimental results</p>
<p>Can a short fine-tune turn a style instruction into the model’s default voice?
Compare the same unseen questions with and without a style prompt, then with a saved adapter.</p>
<div class="filters" aria-label="Filter examples by language">
<button onclick="filterLanguage('all')">All examples</button>
<button onclick="filterLanguage('pl')">Polish</button>
<button onclick="filterLanguage('en')">English</button></div>
<script>function filterLanguage(language){document.querySelectorAll('article').forEach(function(card){
card.hidden=language!=='all'&&card.dataset.language!==language;});}</script>'''
        + body + '</html>')
    print(args.output)
