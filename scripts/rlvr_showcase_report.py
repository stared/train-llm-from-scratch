"""Render all saved first attempts; no GPU, API or answer cherry-picking."""
import argparse
import json
from pathlib import Path


def read(path):
    return json.loads(path.read_text())


def build(paths, output='results/rlvr-results'):
    bundles = []
    md = ['# RLVR: actual before/after results', '',
          'Every answer below is a saved model generation. Before: the original checkpoint. '
          'After: a fresh LoRA trained only with programmatic rewards on synthetic prompts from a pool of 256; '
          'no workshop SFT, supplied answer targets, teacher API, or best-of-N selection. '
          'Both receive identical task instructions.', '',
          'Strict success measures the task rules. For microfiction it does **not** measure storytelling quality. '
          'Greedy first attempts are the main comparison; fixed-seed sampling is shown separately. '
          'Small single-seed experiments demonstrate behavior, not a general model ranking.', '',
          '| Task | Model | Dev before → after | Test before → after | Training | Estimated compute |',
          '|---|---|---:|---:|---:|---:|']
    for path in paths:
        run = read(path / 'execution.json')
        data = read(path / 'data.json')
        history = read(path / 'rollouts.json')
        selected = run.get('selected_step', run['steps'])
        used = len({i for batch in history[:selected] for i in batch['ids']})
        bundle = dict(run=run, name=path.name, splits={}, selected_training_prompts=used)
        before, after = run['before'], run['after']
        md.append(f"| {run['task']} | {run['model_spec']['id']} | {before['dev']['successes']}/{before['dev']['n']} → {after['dev']['successes']}/{after['dev']['n']} | "
                  f"{before['test']['successes']}/{before['test']['n']} → {after['test']['successes']}/{after['test']['n']} | {run['training_seconds']:.1f} s | ${run['estimated_compute_usd']:.4f} |")
        for split in ('dev', 'test', 'sampled_dev'):
            raw = {r['id']: r for r in data['dev' if split == 'sampled_dev' else split]}
            a, b = read(path / f'before_{split}.json'), read(path / f'after_{split}.json')
            assert len(a) == len(b)
            bundle['splits'][split] = []
            for old, new in zip(a, b):
                assert old['id'] == new['id'] and old['prompt'] == new['prompt']
                bundle['splits'][split].append(dict(input=raw[old['id']], before=old, after=new))
        bundles.append(bundle)
    md.extend(['', 'Compute estimates cover completed workers including evaluation and reload, excluding startup/storage. '
               'Screening and any follow-up runs are additional; see LAB_NOTEBOOK.md.', ''])
    for bundle in bundles:
        run = bundle['run']
        md.extend([f"## {run['task']}: {bundle['name']}", '',
                   f"Model: **{run['model_spec']['id']}**, revision `{run['model_spec']['revision']}`. "
                   f"After: RLVR on this task only, {run['steps']} batches / {run['updates']} updates, "
                   f"rank-{run['lora_rank']} LoRA, LR {run['learning_rate']}, beta {run.get('beta', 0)}. "
                   f"Selected batch {run.get('selected_step', run['steps'])}; checkpoint selection "
                   f"{'uses development prompts only' if run.get('dev_interval') else 'disabled (final batch)'}. "
                   f"Selected adapter saw {bundle['selected_training_prompts']} distinct training prompts. "
                   f"Data SHA-256 `{run['data_sha256']}`. "
                   f"Fresh-base adapter reload matches: {run['reload_matches']}.", '',
                   'Sampling uses temperature 1, top-k 0, top-p 1; evaluation seed 2026. '
                   'Greedy evaluation uses batches of eight. No decoding repair or retry.', ''])
        for split, rows in bundle['splits'].items():
            md.extend([f'### {split}', ''])
            for i, row in enumerate(rows):
                old, new = row['before'], row['after']
                md.extend([f"#### {old['id']} / {i+1}", '', old['prompt'], '',
                           f"Before — original {run['model_spec']['id']}; success={old['success']}; reward={old['reward']:.3f}:",
                           '', '```text', old['text'], '```', '',
                           f"After — {run['model_spec']['id']} + {run['task']} RLVR; success={new['success']}; reward={new['reward']:.3f}:",
                           '', '```text', new['text'], '```', ''])
    Path(output + '.md').write_text('\n'.join(md))
    payload = json.dumps(bundles, ensure_ascii=False).replace('<', '\\u003c')
    page = r'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>RLVR lab — before / after</title><style>
:root{font:17px/1.5 system-ui;color:#e7edf5;background:#101820}body{max-width:1150px;margin:40px auto;padding:0 24px}
h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.05;margin-bottom:16px}h2{margin:8px 0}p{max-width:850px;color:#bdcbdc}
select,button{font:inherit;padding:8px 12px;background:#233142;color:white;border:1px solid #51637c;border-radius:7px}
nav{display:flex;gap:12px;flex-wrap:wrap;position:sticky;top:0;background:#101820ee;padding:12px 0;z-index:1}
.card{margin:24px 0;padding:22px;background:#192532;border:1px solid #344459;border-radius:12px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.answer{padding:15px;background:#111d29;border-radius:8px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;margin:8px 0}.prompt{color:#dfd1a6}
.pass{color:#7ae9a9}.fail{color:#ffb29b}.muted,small{color:#a7b8cd}small{display:block}.tag{font:13px ui-monospace,monospace}
.maze{display:grid;grid-template-columns:repeat(4,38px);gap:3px;margin:12px 0}.cell{height:38px;display:grid;place-items:center;background:#35475e;border-radius:3px}.wall{background:#070c11}.route{background:#2e7557}.hit{background:#af4e45}.word{display:inline-block;border-bottom:2px solid #62789a;margin:3px 6px 3px 0;padding:2px;font-size:14px}.word b{font-size:10px;color:#a7b8cd;padding-right:3px}.anchor{border-color:#7ae9a9}.repeat{border-color:#ffb29b}.stats{color:#a6f5c8;font-size:1.1rem}
@media(max-width:700px){.cols{grid-template-columns:1fr}body{padding:0 14px}.card{padding:14px}}
</style><h1>Can a checker teach a model?</h1>
<p>Three small RLVR experiments. Real, unedited first attempts, with identical instructions before and after training.
Before: original checkpoint. After: a fresh LoRA trained with rewards only. No teacher answers or best-of-N selection.</p>
<nav><select id="task"></select><select id="split"><option value="test">Held-out test</option><option value="dev">Development</option><option value="sampled_dev">Sampled development</option></select>
<label><input id="changed" type="checkbox"> Only failures → successes</label></nav><div id="summary"></div><div id="cards"></div>
<script>const DATA=__DATA__;
const $=id=>document.getElementById(id), esc=x=>String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
DATA.forEach((b,i)=>{let o=document.createElement('option');o.value=i;o.textContent=b.run.task+' · '+b.run.model+' · beta '+(b.run.beta||0);$('task').append(o)});
function maze(row,text){if(!row.grid)return '';let [r,c]=row.start, visits=new Set([r+','+c]),hit='';let valid=/^[UDLR]{1,12}$/.test(text.trim());
if(valid)for(let m of text.trim()){let [dr,dc]={U:[-1,0],D:[1,0],L:[0,-1],R:[0,1]}[m];r+=dr;c+=dc;if(r<0||r>3||c<0||c>3||row.grid[r][c]==='#'){hit=r+','+c;break}visits.add(r+','+c)}
return '<div class="maze">'+row.grid.flatMap((line,i)=>[...line].map((cell,j)=>'<div class="cell '+(cell==='#'?'wall ':'')+(visits.has(i+','+j)?'route ':'')+(hit===i+','+j?'hit':'')+'">'+(cell==='.'?'':cell)+'</div>')).join('')+'</div><small>Green: visited. Red: wall collision. Off-grid moves also fail.</small>'}
function wordchips(row,obj){if(!row.anchors)return '';let words=obj.text.toLowerCase().match(/[a-z]+(?:'[a-z]+)?/g)||[];return '<div aria-label="Counted words">'+words.map((w,i)=>'<span class="word '+(row.anchors.includes(w)?'anchor ':'')+(words.indexOf(w)<i?'repeat':'')+'"><b>'+(i+1)+'</b>'+esc(w)+'</span>').join('')+'</div>'}
function answer(label,obj,row,model){let detail=('word_count'in obj)?obj.word_count+' words · '+Math.round(obj.anchors*2)+'/2 required words':('uses_numbers'in obj)?'Uses given numbers: '+obj.uses_numbers+(obj.value?' · Value: '+obj.value:''):('collision'in obj)?'Collision: '+obj.collision:'';
return '<div class="answer"><strong>'+label+'</strong><small>'+esc(model)+'</small><div class="'+(obj.success?'pass':'fail')+'">'+(obj.success?'✓ Pass':'✗ Fail')+' · reward '+obj.reward.toFixed(3)+'</div><pre>'+esc(obj.text)+'</pre>'+wordchips(row,obj)+'<small>'+esc(detail)+' · EOS: '+obj.terminated+'</small>'+maze(row,obj.text)+'</div>'}
function render(){let b=DATA[+$('task').value],split=$('split').value,all=b.splits[split],rows=all.filter(x=>!$('changed').checked||(!x.before.success&&x.after.success));
let count=k=>all.filter(r=>r[k].success).length; $('summary').innerHTML='<h2>'+esc(b.run.task)+'</h2><div class="stats">'+count('before')+'/'+all.length+' → '+count('after')+'/'+all.length+' strict successes</div><p>'+esc(b.run.model_spec.id)+' · '+(b.run.training_seconds/60).toFixed(1)+' minutes training · $'+b.run.estimated_compute_usd.toFixed(3)+' completed-worker compute. '+b.run.updates+' updates. Reload verified: '+b.run.reload_matches+'.</p><small>Model revision '+esc(b.run.model_spec.revision)+' · '+esc(b.name)+'</small>'+(b.run.task==='six_words'?'<p>Passing the word checker does not prove a good story. Judge meaning, novelty and grammar yourself.</p>':'');
$('cards').innerHTML=rows.map(x=>'<article class="card"><div class="tag">'+esc(x.input.id)+'</div><pre class="prompt">'+esc(x.input.prompt)+'</pre><div class="cols">'+answer('Before',x.before,x.input,b.run.model_spec.id+' · original')+answer('After RLVR',x.after,x.input,b.run.model_spec.id+' · '+b.run.task+' rewards')+'</div></article>').join('')||'<p>No examples match this filter.</p>'}
['task','split','changed'].forEach(id=>$(id).addEventListener('change',render));render();</script></html>'''
    Path(output + '.html').write_text(page.replace('__DATA__', payload))
    print(f'Saved {output}.md and {output}.html')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs', nargs='+', type=Path)
    p.add_argument('--output', default='results/rlvr-results')
    a = p.parse_args()
    build(a.runs, a.output)
