# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Render actual scratch-training samples and learning curves without a GPU."""
import argparse
import json
from pathlib import Path

HTML='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Polish Wikipedia from random weights</title>
<style>body{font:17px/1.5 system-ui,sans-serif;max-width:1100px;margin:35px auto;padding:0 20px;background:#f5f8fc;color:#192637}h1{line-height:1.15}table{width:100%;border-collapse:collapse}td,th{padding:10px;border-bottom:1px solid #cdd7e3;text-align:left}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:white;border:1px solid #ccd9e5;padding:18px;font:15px/1.55 monospace}select{font:inherit;padding:6px;margin-right:12px}svg{width:100%;background:white;border:1px solid #ccd9e5}small{color:#526175}</style>
<h1>Polish Wikipedia from random weights</h1>
<p>Fresh10M/30M transformers and a new8k BPE tokenizer. Training text is original Polish Wikipedia wikitext: links, templates, tables and references are retained. No pretrained weights, fine-tuning or supplied answer targets.</p>
<div id="summary"></div><h2>Development loss during training</h2><svg id="chart" viewBox="0 0 1000 380" role="img" aria-label="Development loss over training time"></svg><p>Blue:10M. Orange:30M. Lower loss is better. Samples use fixed prompts and sampling seed; a loss decrease does not certify factual accuracy or valid markup.</p>
<h2>Actual generated continuations</h2><label>Model <select id="model"></select></label><label>Checkpoint <select id="checkpoint"></select></label><label>Prompt <select id="prompt"></select></label>
<p id="label"></p><pre id="sample"></pre><small>Displayed literally as wikitext. The supplied prompt is separated from the generated continuation. Both are preserved unedited in run JSON files. These are base language models, not chat assistants.</small>
<script>
const runs=DATA;
const el=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const color=r=>r.result.model.includes('10m')?'#086abd':'#b94e0a';
el('summary').innerHTML='<table><tr><th>Model</th><th>Parameters</th><th>Tokens processed</th><th>Dev loss before → selected</th><th>Test loss before → selected</th><th>Worker estimate</th></tr>'+runs.map(r=>`<tr><td>${r.result.model}</td><td>${r.result.parameters.toLocaleString()}</td><td>${r.result.tokens_seen.toLocaleString()}</td><td>${r.result.before.dev.loss_nats.toFixed(3)} → ${r.result.selected.dev.loss_nats.toFixed(3)}</td><td>${r.result.before.test.loss_nats.toFixed(3)} → ${r.result.selected.test.loss_nats.toFixed(3)}</td><td>$${r.result.estimated_compute_usd.toFixed(3)}</td></tr>`).join('')+'</table>';
const pts=r=>[{elapsed_seconds:0,loss_nats:r.result.before.dev.loss_nats},...r.checkpoints];
const maxX=Math.max(...runs.flatMap(r=>pts(r).map(p=>p.elapsed_seconds))),maxY=Math.ceil(Math.max(...runs.flatMap(r=>pts(r).map(p=>p.loss_nats))));
const x=v=>60+v/maxX*910,y=v=>325-v/maxY*285;
let svg='';for(let i=0;i<=5;i++){const v=i/5*maxY;svg+=`<line x1="60" x2="970" y1="${y(v)}" y2="${y(v)}" stroke="#dde5ee"/><text x="50" y="${y(v)+5}" text-anchor="end">${v.toFixed(1)}</text>`;}
for(let i=0;i<=5;i++){const v=i/5*maxX;svg+=`<text x="${x(v)}" y="350" text-anchor="middle">${(v/60).toFixed(1)}</text>`;}
for(const r of runs){svg+=`<polyline fill="none" stroke="${color(r)}" stroke-width="2.5" points="${pts(r).map(p=>x(p.elapsed_seconds)+','+y(p.loss_nats)).join(' ')}"/>`;for(const p of pts(r))svg+=`<circle cx="${x(p.elapsed_seconds)}" cy="${y(p.loss_nats)}" r="4" fill="${color(r)}"><title>${r.result.model}: ${p.loss_nats.toFixed(3)} nats/token at ${(p.elapsed_seconds/60).toFixed(2)}min</title></circle>`;}
svg+='<text x="510" y="377" text-anchor="middle">Minutes (including periodic evaluation and sampling)</text>';el('chart').innerHTML=svg;
el('model').innerHTML=runs.map((r,i)=>`<option value="${i}">${r.result.model}</option>`).join('');
function checkpoints(){const r=runs[Number(el('model').value)];el('checkpoint').innerHTML=r.samples.map((s,i)=>`<option value="${i}">${esc(s.name)}</option>`).join('');el('checkpoint').value=String(r.samples.length-1);el('prompt').innerHTML=r.samples[0].rows.map((s,i)=>`<option value="${i}">${esc(s.prompt)}</option>`).join('');show();}
function show(){const r=runs[Number(el('model').value)],s=r.samples[Number(el('checkpoint').value)],row=s.rows[Number(el('prompt').value)];el('label').textContent=`${r.result.model}, trained from random weights on Polish Wikipedia20260901 wikitext — ${s.name}. Run ${r.name}.`;el('sample').textContent='PROMPT\n'+row.prompt+'\n\nGENERATED CONTINUATION\n'+row.continuation;}
el('model').addEventListener('change',checkpoints);el('checkpoint').addEventListener('change',show);el('prompt').addEventListener('change',show);checkpoints();
</script></html>'''


def render(paths):
    runs=[]
    md=['# Wikipedia wikitext: actual scratch-model results','',
        'Both models start from random weights. The BPE tokenizer is trained only on training articles. Original wikitext is retained; no pretrained model, poetry/film adapter or instruction tuning is involved.','']
    for path in map(Path,paths):
        result=json.loads((path/'execution.json').read_text())
        stages=[('Initialization','samples_before.json')]
        stages.extend((p.stem,p.name) for p in sorted(path.glob('samples_step_*.json'),key=lambda p:int(p.stem.rsplit('_',1)[1])))
        stages.extend([('Final','samples_final.json'),('Development-selected','samples_selected.json')])
        records=[dict(name=title,rows=json.loads((path/filename).read_text())) for title,filename in stages]
        runs.append(dict(name=path.name,result=result,checkpoints=json.loads((path/'checkpoints.json').read_text()),samples=records))
        md.extend([f"## {result['model']}: {result['parameters']:,} parameters",'',f"Run `{path.name}`. Trained on original Polish Wikipedia20260901 article wikitext. {result['tokens_seen']:,} sampled training tokens in {result['training_seconds']:.1f}s; exposure ratio {result['exposure_ratio']:.4f} of the available training-pool token count, sampled with replacement (not a complete epoch).",'',
            f"Development loss {result['before']['dev']['loss_nats']:.3f} → {result['selected']['dev']['loss_nats']:.3f}; test loss {result['before']['test']['loss_nats']:.3f} → {result['selected']['test']['loss_nats']:.3f} nats/token. Estimated worker compute ${result['estimated_compute_usd']:.4f}. Fresh-process reload matches: {result['fresh_process_reload_matches']}.",''])
        for stage in records:
            md.extend([f"### {stage['name']} — {result['model']}",''])
            for row in stage['rows']:
                fence='`'*max(3,max((len(x) for x in row['continuation'].split() if set(x)=={'`'}),default=0)+1)
                md.extend(['Prompt:',fence,row['prompt'],fence,'','Generated continuation:',fence,row['continuation'],fence,''])
    Path('wiki_scratch_results.html').write_text(HTML.replace('const runs=DATA;','const runs='+json.dumps(runs,ensure_ascii=False).replace('<','\\u003c')+';'))
    Path('wiki_scratch_example_results.md').write_text('\n'.join(md))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('runs',nargs='+');a=p.parse_args();render(a.runs)
