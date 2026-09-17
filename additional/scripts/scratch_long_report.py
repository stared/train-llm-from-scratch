# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Render completed scratch runs. All curves and continuations come from run JSON."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
STAGES = [('before', 'Initialization'), ('budget_1usd', 'First checkpoint after $1'), ('final', 'Final diagnostic'), ('selected', 'Development-selected')]


def read(path, default=None):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default


def load_run(path):
    result = read(path / 'execution.json')
    if result is None:
        raise ValueError(f'{path}: no execution.json; run is incomplete')
    quality = [(label, read(path / f'quality_{stage}.json')) for stage, label in STAGES]
    if not any(value for _, value in quality):
        quality = [('Development-selected', read(path / 'quality.json'))]
    stages = []
    for label, value in quality:
        if value:
            stages.append(dict(label=label, quality=value, rows=value['free_generations']))
    # Preserve periodic original four-prompt generations as another source, without
    # mixing their sampling seed with the independent quality diagnostics.
    files = [('samples_before.json', 'Initialization / original prompts')]
    files += [(p.name, f"Step {p.stem.rsplit('_', 1)[1]} / original prompts")
              for p in sorted(path.glob('samples_step_*.json'), key=lambda p: int(p.stem.rsplit('_', 1)[1]))]
    files += [('samples_final.json', 'Final / original prompts'), ('samples_selected.json', 'Development-selected / original prompts')]
    for name, label in files:
        rows = read(path / name)
        if rows:
            stages.append(dict(label=label, quality=None, rows=rows))
    checkpoints = read(path / 'checkpoints.json', [])
    before_quality = read(path / 'quality_before.json', {})
    # Initial quality evaluation occurs before the training clock. This measured
    # anchor approximates worker overhead; subsequent evaluation is in train time.
    overhead = before_quality.get('worker_elapsed')
    if overhead is None:
        overhead = max(0., result.get('remote_seconds', result['training_seconds']) - result['training_seconds'])
    rate = result.get('configured_hourly_usd', 0) / 3600
    if not rate:
        rate = result['estimated_compute_usd'] / result.get('remote_seconds', result['training_seconds'])
    points = [dict(elapsed_seconds=0, loss_nats=result['before']['dev']['loss_nats'])] + checkpoints
    if not points or points[-1]['elapsed_seconds'] < result['training_seconds']:
        points.append(dict(elapsed_seconds=result['training_seconds'], loss_nats=result['final']['dev']['loss_nats']))
    points = [dict(seconds=p['elapsed_seconds'], dollars=(p['elapsed_seconds'] + overhead) * rate,
                   loss=p['loss_nats'], step=p.get('step')) for p in points]
    selected = next((s['quality'] for s in stages if s['label'] == 'Development-selected' and s['quality']), None)
    source = result.get('source', '').casefold()
    corpus = 'wolne-lektury' if 'wolne lektury' in source or path.name.startswith('scratch-wl-') else 'wikipedia'
    if 'filtered' in source and 'lead' in source or path.name.startswith('scratch-leads-'):
        corpus = 'wikipedia-leads'
    if 'tinystories' in source or path.name.startswith('scratch-tiny-'):
        corpus = 'tinystories'
    if 'top10k linked' in source or path.name.startswith('scratch-popular-'):
        corpus='wikipedia-popular'
    return dict(name=path.name, result=result, stages=stages, points=points, corpus=corpus,
                common_wiki=read(path/'common_wiki_eval.json'),
                selected_quality=selected, initial_overhead_seconds=overhead,
                baseline=path.name.startswith('scratch-wikitext-'))


HTML = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Polish pre-training experiments</title>
<style>body{font:16px/1.5 system-ui,sans-serif;color:#222;max-width:1150px;margin:32px auto;padding:0 18px}h1{font-size:25px}h2{font-size:19px;margin-top:30px}p{max-width:100ch}.table{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:8px 10px;border-bottom:1px solid #ddd;text-align:left;white-space:nowrap}small,.note{color:#555;font-size:13px}select{font:inherit;max-width:100%;padding:4px;margin:4px 15px 4px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 monospace;background:#f6f6f6;padding:16px}svg{width:100%;height:auto}#legend span{display:inline-block;margin-right:20px}label{display:inline-block}details{margin:12px 0}#identity{overflow-wrap:anywhere}</style>
<h1>Polish pre-training experiments</h1>
<p>Randomly initialized models with 8k BPE tokenizers. Polish corpora reuse the Wikipedia tokenizer; English TinyStories uses a new training-only English tokenizer. No pre-trained weights or fine-tuning. Lower loss measures better token prediction; it does not certify factual accuracy.</p>
<label>Training corpus <select id="corpus"></select></label>
<p id="corpus-note" class="note"></p>
<div class="table" id="summary"></div>
<p class="note">Compute estimates include worker GPU, CPU and memory, excluding image builds, storage and failed jobs. Diagnostic facts are ten fixed, curated candidate preferences, not a benchmark; these facts may appear in training. Repetition is the fraction of repeated word 4-grams in sampled continuations, not a grammar score.</p>
<h2>Development loss</h2>
<label>Horizontal axis <select id="axis"><option value="dollars">Estimated worker dollars</option><option value="seconds">Training minutes</option></select></label>
<label><input type="checkbox" id="initial" checked> Include initialization</label>
<svg id="chart" viewBox="0 0 1000 330" role="img" aria-label="Development loss by training time or estimated cost"></svg><div id="legend"></div>
<p class="note">Dollar positions approximate (training elapsed + initial worker overhead) × worker rate. Quality-stage costs below are separately measured at those checkpoints. Training time includes periodic evaluation. Different GPUs and model sizes make this a practical budget comparison, not a controlled architecture ablation.</p>
<h2>Generated continuations</h2>
<label>Model <select id="model"></select></label><label>Stage <select id="stage"></select></label><br>
<label>Prompt <select id="prompt"></select></label>
<p class="note" id="identity"></p><pre id="sample"></pre><p class="note" id="diagnostic"></p>
<details><summary>Factual candidate preferences at this stage</summary><div class="table" id="facts"></div></details>
<script>
const allRuns=PAYLOAD;
let runs=[];
const el=id=>document.getElementById(id), esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const colors=['#1665a4','#ae4b14','#287843','#8254a1','#555','#c42454','#8d790e','#168080','#684330'];
const fmt=(v,n=2)=>typeof v==='number'?v.toFixed(n):'—';
const title=r=>r.result.model+' / '+(r.result.environment?.device||'GPU').replace('NVIDIA ','')+(r.baseline?' / 5 min baseline':'');
const qtext=q=>q?.factual_total?`${q.factual_correct}/${q.factual_total}`:'n/a';
function summary(){const common=runs.some(r=>r.common_wiki);el('summary').innerHTML='<table><tr><th>Model / parameters</th><th>GPU</th><th>Worker min / $</th><th>Tokens seen</th><th>Selected test loss</th><th>Facts</th><th>Repetition</th>'+(common?'<th>Full-Wiki test loss</th>':'')+'</tr>'+runs.map(r=>{const a=r.result,q=r.selected_quality;return `<tr><td title="${esc(a.source)}">${esc(title(r))}<br><small>${a.parameters.toLocaleString()} · context ${a.config.context}</small></td><td>${esc(a.environment?.device||'Unknown')}</td><td>${fmt((a.remote_seconds??a.training_seconds)/60)} / $${fmt(a.estimated_compute_usd,3)}</td><td>${(a.tokens_seen/1e6).toFixed(1)}M</td><td>${fmt(a.before.test.loss_nats,3)} → ${fmt(a.selected.test.loss_nats,3)}</td><td>${qtext(q)}</td><td>${q?fmt(q.mean_repeated_word_4gram_fraction*100,1)+'%':'—'}</td>${common?'<td>'+fmt(r.common_wiki?.test.loss_nats,3)+'</td>':''}</tr>`}).join('')+'</table>'+(common?'<p class="note">Full-Wiki test loss evaluates the selected model on the same separate 16,384 held-out Wikipedia tokens as the original runs. The main test-loss column and curve remain specific to the selected training corpus.</p>':'');}
function chart(){const axis=el('axis').value, include=el('initial').checked, values=runs.map(r=>r.points.filter((p,i)=>include||i>0)),flat=values.flat();if(!flat.length){el('chart').innerHTML='';return;}const mx=Math.max(...flat.map(p=>p[axis]),.01),low=Math.max(0,Math.min(...flat.map(p=>p.loss))-.1),high=Math.max(...flat.map(p=>p.loss))+.1;const x=v=>65+v/mx*900,y=v=>275-(v-low)/(high-low)*245;let svg='';for(let i=0;i<=5;i++){const v=low+(high-low)*i/5;svg+=`<line x1="65" x2="965" y1="${y(v)}" y2="${y(v)}" stroke="#ddd"/><text x="55" y="${y(v)+5}" text-anchor="end" font-size="13">${v.toFixed(2)}</text>`;const h=mx*i/5;svg+=`<text x="${x(h)}" y="301" text-anchor="middle" font-size="13">${axis==='dollars'?'$'+h.toFixed(2):(h/60).toFixed(0)}</text>`;}values.forEach((pts,i)=>{const color=colors[i%colors.length];svg+=`<polyline fill="none" stroke="${color}" stroke-width="2" ${runs[i].baseline?'stroke-dasharray="5 4"':''} points="${pts.map(p=>x(p[axis])+','+y(p.loss)).join(' ')}"/>`;for(const p of pts)svg+=`<circle cx="${x(p[axis])}" cy="${y(p.loss)}" r="3" fill="${color}"><title>${esc(title(runs[i]))}: ${p.loss.toFixed(3)} nats/token, ${(p.seconds/60).toFixed(1)} min, ~$${p.dollars.toFixed(3)}</title></circle>`;});el('chart').innerHTML=svg;el('legend').innerHTML=runs.map((r,i)=>`<span style="color:${colors[i%colors.length]}">${esc(title(r))}</span>`).join('');}
el('axis').onchange=chart;el('initial').onchange=chart;
const corpusLabels={'wikipedia-popular':'Popular Wikipedia openings','wikipedia':'Polish Wikipedia wikitext','wolne-lektury':'Historical Wolne Lektury archive','wikipedia-leads':'Filtered Wikipedia openings','tinystories':'English TinyStories subset'};
const corpusNotes={'wikipedia-popular':'Top 10,000 eligible opening passages ranked by incoming links from training articles only. Original splits retained, but held-out set is small. Original Wiki tokenizer. This is a restricted corpus, not full Wikipedia.','wikipedia':'Original Polish Wikipedia September 2026 wikitext, including redirects.','wolne-lektury':'Historical Falenty Wolne Lektury literary bodies, including non-Polish texts; not the current complete catalogue. The Wikipedia BPE is reused. No Wikipedia factual diagnostic is applied to literature.','wikipedia-leads':'FILTERED original Wikipedia lead substrings from nonredirect pages of at least 4,000 characters. This is not the full Wikipedia corpus. Original splits and the original Wiki BPE are retained.','tinystories':'English TinyStories positive control: first of four official training shards, existing synthetic GPT-3.5/GPT-4 stories under CDLA-Sharing-1.0. New English BPE trained only on this training subset. Simpler corpus, not evidence of Polish knowledge; no factual diagnostic.'};
el('corpus').innerHTML=[...new Set(allRuns.map(r=>r.corpus))].map(c=>`<option value="${c}">${corpusLabels[c]}</option>`).join('');
function corpus(){runs=allRuns.filter(r=>r.corpus===el('corpus').value);el('corpus-note').textContent=corpusNotes[el('corpus').value]+' Table, curve and samples show only this corpus: losses across different corpora are different tasks and are not plotted together.';summary();el('model').innerHTML=runs.map((r,i)=>`<option value="${i}">${esc(title(r))}</option>`).join('');chart();stages();}
function stages(){const r=runs[+el('model').value];el('stage').innerHTML=r.stages.map((s,i)=>`<option value="${i}">${esc(s.label)}</option>`).join('');const selected=r.stages.findIndex(s=>s.label==='Development-selected');if(selected>=0)el('stage').value=selected;prompts();}
function prompts(){const s=runs[+el('model').value].stages[+el('stage').value];el('prompt').innerHTML=s?s.rows.map((p,i)=>`<option value="${i}">${esc(p.prompt)}</option>`).join(''):'';show();}
function show(){const r=runs[+el('model').value],s=r.stages[+el('stage').value],row=s?.rows[+el('prompt').value],q=s?.quality;el('identity').textContent=`${r.result.model} · ${r.result.source} · ${s?.label||'No samples'} · run ${r.name}`;el('sample').textContent=row?'PROMPT\n'+row.prompt+'\n\nGENERATED CONTINUATION\n'+row.continuation:'No sample JSON available.';el('diagnostic').textContent=q?`Factual preference: ${qtext(q)}. Repetition: ${fmt(q.mean_repeated_word_4gram_fraction*100,1)}%. Stage worker estimate: $${fmt(q.estimated_compute_usd,3)}. Sampling temperature ${q.temperature}, top-k ${q.top_k}; fixed per-prompt seed.`:'Original four-prompt sampling recipe; these are separate from the eight-prompt quality diagnostics.';if(r.common_wiki&&s?.label.startsWith('Development-selected'))el('diagnostic').textContent+=` Separate full-Wikipedia test loss: ${fmt(r.common_wiki.test.loss_nats,3)} nats/token on ${r.common_wiki.test.tokens.toLocaleString()} fixed held-out tokens.`;el('facts').innerHTML=q?.factual_total?'<table><tr><th>Prompt</th><th>Preferred</th><th>Correct candidate</th></tr>'+q.facts.map(f=>`<tr><td>${esc(f.prompt)}</td><td>${esc(f.candidates[f.predicted])} ${f.is_correct?'✓':'✗'}</td><td>${esc(f.candidates[f.correct])}</td></tr>`).join('')+'</table>':'Not applicable: no factual diagnostic for this corpus or sample stage.';}
el('model').onchange=stages;el('stage').onchange=prompts;el('prompt').onchange=show;el('corpus').onchange=corpus;corpus();
</script></html>'''


def fenced(text):
    fence = '`' * max(3, max((len(m.group()) for m in re.finditer(r'`+', text)), default=0) + 1)
    return [fence, text, fence, '']


def render(paths, output_dir=ROOT / 'results'):
    runs = [load_run(Path(path)) for path in paths]
    if not runs:
        raise ValueError('No completed runs found')
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(runs, ensure_ascii=False).replace('<', '\\u003c')
    (out / 'pretraining-results.html').write_text(HTML.replace('const allRuns=PAYLOAD;', 'const allRuns=' + payload + ';'), encoding='utf-8')
    md = ['# Polish pre-training: actual experimental results', '',
          'All models start from random weights. Training corpus is labeled per run. Polish corpora reuse the Wikipedia-trained 8k tokenizer; English TinyStories uses a new training-only English BPE. No fine-tuning. Samples below are literal outputs, not edited examples. Different corpora/tokenizers define different prediction tasks; their losses should not be ranked together.', '',
          'Factual preference uses ten fixed candidate-choice diagnostics; it is not a benchmark or a held-out knowledge test. Repetition counts repeated word 4-grams and does not assess grammar. Worker estimates exclude builds, storage and failed jobs.', '']
    for run in runs:
        r = run['result']
        md += [f"## {r['model']} — {run['name']}", '', f"Source: {r['source']}", '',
               f"Parameters: {r['parameters']:,}; GPU: {r.get('environment', {}).get('device', 'unknown')}; context: {r['config']['context']} tokens. Random initialization, no fine-tuning.", '',
               f"Training: {r['training_seconds']/60:.2f} minutes; worker: {r.get('remote_seconds', r['training_seconds'])/60:.2f} minutes; estimated worker compute: ${r['estimated_compute_usd']:.4f}. Tokens presented: {r['tokens_seen']:,}, sampled with replacement.", '',
               f"Selected development loss: {r['selected']['dev']['loss_nats']:.4f}; selected test loss: {r['selected']['test']['loss_nats']:.4f} nats/token. Fresh-process reload matches: {r.get('fresh_process_reload_matches', 'not recorded')}.", '']
        if run['common_wiki']:
            common=run['common_wiki']
            md += [f"Separate common full-Wikipedia evaluation of the selected checkpoint: dev {common['dev']['loss_nats']:.4f}, test {common['test']['loss_nats']:.4f} nats/token on {common['test']['tokens']:,} fixed held-out test tokens. These are separate from this run's own corpus metrics.", '']
        for stage in run['stages']:
            md += [f"### {r['model']} — {stage['label']}", '']
            q = stage['quality']
            if q:
                fact_label = f"{q['factual_correct']}/{q['factual_total']}" if q['factual_total'] else 'n/a (not evaluated for this corpus)'
                md += [f"Factual preference: {fact_label}. Mean repeated word 4-gram fraction: {q['mean_repeated_word_4gram_fraction']:.4f}. Stage worker compute estimate: " + (f"${q['estimated_compute_usd']:.4f}." if 'estimated_compute_usd' in q else 'not recorded.'), '']
                if q['facts']:
                    md += ['| Prompt | Preferred candidate | Correct candidate |', '|---|---|---|']
                for f in q['facts']:
                    cells = [f['prompt'], f['candidates'][f['predicted']], f['candidates'][f['correct']]]
                    md.append('| ' + ' | '.join(c.replace('|', '\\|').replace('\n', ' ') for c in cells) + ' |')
                md.append('')
            for row in stage['rows']:
                md += ['Prompt:'] + fenced(row['prompt']) + ['Generated continuation:'] + fenced(row['continuation'])
    (out / 'pretraining-example-results.md').write_text('\n'.join(md), encoding='utf-8')
    return runs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('runs', nargs='*', type=Path)
    parser.add_argument('--include-baselines', action='store_true')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'results')
    args = parser.parse_args()
    paths = args.runs or sorted(p.parent for p in (ROOT / 'runs').glob('scratch-*/execution.json') if not p.parent.name.startswith('scratch-wikitext-'))
    if args.include_baselines:
        paths += sorted(p.parent for p in (ROOT / 'runs').glob('scratch-wikitext-*/execution.json'))
    render(paths, args.output_dir)
    print(f'Wrote pretraining-results.html and pretraining-example-results.md in {args.output_dir}')
