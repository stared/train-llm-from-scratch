# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Standalone interactive learning curves for the longer SFT/RLVR comparison."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
import json
from pathlib import Path

TEMPLATE = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LLM robi prawko — longer training</title>
<style>
body{font:17px/1.5 system-ui,sans-serif;max-width:1100px;margin:35px auto;padding:0 22px;color:#182433;background:#f8fafc}h1{line-height:1.1}h2{margin-top:2em}table{border-collapse:collapse;width:100%;background:white}td,th{text-align:left;padding:9px;border-bottom:1px solid #d8e0e8}select{padding:7px;font:inherit}svg{width:100%;height:auto;background:white;border:1px solid #d8e0e8;margin-top:12px}small,.muted{color:#506174}.good{color:#08734e}.bad{color:#aa273d}details{background:white;margin:12px 0;padding:14px;border:1px solid #d8e0e8}summary{cursor:pointer;font-weight:600}.legend span{margin-right:22px}.sft{color:#0066c0}.rlvr{color:#b24500}code{font-size:.85em;overflow-wrap:anywhere}.scroll{overflow:auto}
</style>
<h1>LLM robi prawko: does longer training help?</h1>
<p>Qwen3.5-0.8B, two fresh adapters trained on the same <strong>100 official Polish driving-theory questions</strong>. Separate 25-question development and 40-question test sets. Constrained A/B/C answers, no generated reasoning.</p>
<p>Checkpoints are selected using development results only. “Final” means training to the budget limit; it is evaluated separately. Reordered choices reuse the same test questions. This is not the full driving examination.</p>
<h2>Development learning curves</h2>
<label>Metric <select id="metric"><option value="accuracy">Accuracy</option><option value="mean_correct_probability">Mean correct-answer probability</option></select></label>
<label>Horizontal axis <select id="axis"><option value="epoch">Epoch</option><option value="elapsed_seconds">Training minutes</option></select></label>
<p class="legend"><span class="sft">● SFT</span><span class="rlvr">● RLVR</span>Large circles mark selected checkpoints. Hover a point for its score.</p>
<svg id="chart" viewBox="0 0 1000 430" role="img" aria-label="Development learning curves for SFT and RLVR"></svg>
<h2>Original, selected, and final checkpoints</h2>
<div class="scroll"><table><thead><tr><th>Model / adapter</th><th>Train /100</th><th>Dev /25</th><th>Test /40</th><th>Reordered /40</th></tr></thead><tbody id="scores"></tbody></table></div>
<p id="cost"></p><div id="metadata"></div>
<h2>Actual held-out choices</h2>
<label>Adapter <select id="method"><option value="sft">SFT</option><option value="rlvr">RLVR</option></select></label>
<label>Checkpoint <select id="phase"><option value="after">Development-selected</option><option value="final">Final</option></select></label>
<label>Show <select id="filter"><option value="all">All questions</option><option value="fix">Corrections</option><option value="regression">Regressions</option><option value="disagree">SFT / RLVR disagree</option></select></label>
<p id="count"></p><div id="examples"></div>
<p class="muted">Option text and correct keys come from the Ministry of Infrastructure July 2026 catalogue. Model outputs are letters only. No Pan Tadeusz or film dialogue was used. One seed and a small grouped test set: do not treat a small score difference as conclusive evidence of a generally superior method.</p>
<script>
const runs = DATA;
const colors={sft:'#0066c0',rlvr:'#b24500'};
const el=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function chart(){
 const metric=el('metric').value, axis=el('axis').value;
 const points=r=>[{epoch:0,elapsed_seconds:0,...r.result.before.dev},...r.checkpoints];
 const xx=p=>axis==='epoch'?p.epoch:p.elapsed_seconds/60;
 const maxX=Math.max(...runs.flatMap(r=>points(r).map(xx)),1);
 const x=v=>65+v/maxX*905,y=v=>365-v*310;
 let svg='';
 for(let j=0;j<=5;j++){const v=j/5;svg+=`<line x1="65" x2="970" y1="${y(v)}" y2="${y(v)}" stroke="#d8e0e8"/><text x="52" y="${y(v)+5}" text-anchor="end" font-size="14">${Math.round(v*100)}%</text>`;}
 for(let j=0;j<=5;j++){const v=j/5*maxX;svg+=`<text x="${x(v)}" y="394" text-anchor="middle" font-size="14">${v.toFixed(axis==='epoch'?0:1)}</text>`;}
 for(const r of runs){const pts=points(r),color=colors[r.result.method];svg+=`<polyline fill="none" stroke="${color}" stroke-width="2.5" points="${pts.map(p=>x(xx(p))+','+y(p[metric])).join(' ')}"/>`;
 for(const p of pts){const selected=p.epoch===r.result.selected_epoch;svg+=`<circle cx="${x(xx(p))}" cy="${y(p[metric])}" r="${selected?7:3.5}" fill="${color}" stroke="white" stroke-width="1.5"><title>${r.result.method.toUpperCase()}, epoch ${p.epoch}: ${p.correct}/${p.n}; ${(p[metric]*100).toFixed(1)}%${selected?' — selected':''}</title></circle>`;}}
 svg+=`<text x="520" y="420" text-anchor="middle" font-size="14">${axis==='epoch'?'Epoch (last epoch may be partial)':'Training minutes, including development checks'}</text>`;
 el('chart').innerHTML=svg;
}
function overview(){
 const rows=[['Original Qwen3.5-0.8B; no workshop adapter',runs[0].result.before]];
 for(const r of runs){rows.push([`${r.result.method.toUpperCase()} / selected epoch ${r.result.selected_epoch}`,r.result.after]);rows.push([`${r.result.method.toUpperCase()} / final, ${r.result.steps} updates`,r.result.final]);}
 el('scores').innerHTML=rows.map(([name,m])=>`<tr><td>${esc(name)}</td>${['train','dev','test','test_rotated'].map(k=>`<td>${m[k].correct}</td>`).join('')}</tr>`).join('');
 el('cost').textContent=`Long-run worker estimate: $${runs.reduce((s,r)=>s+r.result.estimated_compute_usd,0).toFixed(4)}, excluding startup/builds/storage. Training: ${runs.map(r=>r.result.method.toUpperCase()+' '+(r.result.training_seconds/60).toFixed(1)+' min').join('; ')}.`;
 el('metadata').innerHTML=runs.map(r=>`<details><summary>${r.result.method.toUpperCase()} run details</summary><p>Run <code>${esc(r.name)}</code>. Revision <code>${esc(r.result.model_spec.revision)}</code>.</p><p>${r.result.selected_steps} selected updates of ${r.result.steps} explored; learning rate ${r.result.learning_rate}; LoRA rank ${r.result.lora_rank}; seed ${r.result.seed}.</p><p>${esc(r.result.algorithm)}. Selected adapter reload matches: ${r.result.reload_matches}.</p></details>`).join('');
}
function examples(){
 const method=el('method').value,phase=el('phase').value,filter=el('filter').value;
 const r=runs.find(r=>r.result.method===method),other=runs.find(r=>r.result.method!==method);
 let count=0;
 el('examples').innerHTML=r.before_test.map((b,i)=>{
 const a=r[phase+'_test'][i],o=other[phase+'_test'][i];
 if(filter==='fix'&&(b.correct||!a.correct)||filter==='regression'&&(!b.correct||a.correct)||filter==='disagree'&&a.prediction===o.prediction)return '';
 count++;return `<details><summary>${esc(b.id)} · ${esc(b.question)}</summary><p>${b.options.map((s,i)=>'ABC'[i]+'. '+esc(s)).join('<br>')}</p><p>Original Qwen3.5-0.8B: <strong class="${b.correct?'good':'bad'}">${b.prediction}</strong> → Qwen3.5-0.8B + ${method.toUpperCase()} on 100 official questions (${phase==='after'?'development-selected':'final'}): <strong class="${a.correct?'good':'bad'}">${a.prediction}</strong>. Official key: <strong>${b.answer}</strong>.</p><p>Other method (${other.result.method.toUpperCase()}, same checkpoint rule): ${o.prediction}.</p></details>`;
 }).join('');el('count').textContent=`Showing ${count} of 40 held-out questions.`;
}
for(const id of ['metric','axis'])el(id).addEventListener('change',chart);
for(const id of ['method','phase','filter'])el(id).addEventListener('change',examples);
overview();chart();examples();
</script></html>'''


def render(paths, output):
    records = []
    for path in paths:
        path = Path(path)
        record = dict(name=path.name)
        for key, filename in [('result','execution.json'),('checkpoints','checkpoints.json'),
                              ('before_test','before_test.json'),('after_test','after_test.json'),('final_test','final_test.json')]:
            record[key] = json.loads((path/filename).read_text())
        records.append(record)
    assert sorted(r['result']['method'] for r in records)==['rlvr','sft']
    assert records[0]['result']['data_sha256']==records[1]['result']['data_sha256']
    assert records[0]['result']['model_spec']==records[1]['result']['model_spec']
    assert [(r['id'],r['prediction']) for r in records[0]['before_test']]==[(r['id'],r['prediction']) for r in records[1]['before_test']]
    payload=json.dumps(records,ensure_ascii=False).replace('<','\\u003c')
    Path(output).write_text(TEMPLATE.replace('const runs = DATA;', 'const runs = '+payload+';'))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs',nargs=2)
    p.add_argument('--output',default='results/prawko-training.html')
    a=p.parse_args()
    render(a.runs,a.output)
