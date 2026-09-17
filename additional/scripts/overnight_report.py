# /// script
# requires-python = ">=3.14"
# dependencies = ["matplotlib==3.11.2"]
# ///
"""Curate the fetched overnight measurements, curves, and literal outputs."""
from html import escape
import json
import re
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from training_report import chart

def e(text):
    # Preserve literal generated whitespace without trailing whitespace in HTML source.
    return escape(text).replace(' \n','&#32;\n').replace('\t\n','&#9;\n')

def superseded(spec):
    return (spec.get('data')=='wiki-plain-leads-v1' or spec.get('mixture_data')=='wiki-plain-leads-v1'
            or 'wiki-plain-leads-v1' in spec.get('base','')
            or (spec.get('base','').startswith('night-1789682325149225000-') and 'continue-plain' in spec['base'])
            or (spec.get('task')=='wiki-qa' and spec.get('dataset')!='wiki-popular-qa'))

def render():
    records=[]
    for path in sorted((ROOT/'runs').glob('night-*/execution.json')):
        fetching=path.parent/'fetch-status.json'
        if fetching.exists() and json.loads(fetching.read_text())['state']!='complete':continue
        r=json.loads(path.read_text())
        if 'spec' not in r:continue
        records.append((path.parent,r))
    tables={'scratch':[], 'exam':[], 'posttrain':[], 'reasoning':[], 'evaluate':[]};details=[]
    total=0
    for folder,r in records:
        spec=r['spec'];cost=r['estimated_compute_usd'];total+=cost
        curves='';examples='';kind=spec['kind']
        if kind=='scratch':
            model=r['model']+(' (continued)' if r.get('initial_checkpoint_run') else '')+(' [superseded data]' if superseded(spec) else '');dataset=spec['data']+(' + '+spec['mixture_data'] if spec.get('mixture_data') else '')
            before=r['before']['test']['loss_nats'];after=r['selected']['test']['loss_nats']
            tokens=r['tokens_seen'];elapsed=r['training_seconds']
            tables[kind].append([model,dataset,str(spec.get('context',512)),spec['gpu'],f"{elapsed/60:.1f}",f"{before:.3f} → {after:.3f}",
                                f"{tokens/1e6:.1f}",' + '.join(f"{v['ratio']:.2f}" for v in r['source_exposures'].values()) if r.get('source_exposures') else f"{r['exposure_ratio']:.2f}",f"{tokens/cost/1e6:.1f}",f"${cost:.3f}"])
            h=json.loads((folder/'history.json').read_text());c=json.loads((folder/'checkpoints.json').read_text())
            curves=chart([('Training loss',[(v['elapsed_seconds'],v['loss']) for v in h]),
                          ('Development loss',[(v['elapsed_seconds'],v['loss_nats']) for v in c])],'Seconds','Cross entropy')
            a=json.loads((folder/'samples_before.json').read_text());b=json.loads((folder/'samples_selected.json').read_text())
            for x,y in zip(a,b):examples+=pair(x['prompt'],x['continuation'],y['continuation'])
        elif kind=='exam':
            for i,stage in enumerate(r['stages']):
                model=stage['model_spec']['id'];s=stage['after'];b=stage['before']
                tables[kind].append([model,' → '.join(spec['methods'][:i+1])+(' + answer text' if spec.get('answer_text') else ''),str(stage['before']['train']['n']),spec['gpu']+'/batch '+str(spec.get('train_batch_size',4)),f"{spec['lr']:g}",str(spec.get('seed',42)),
                    f"{b['test']['correct']} → {s['test']['correct']}",str(s['dev']['correct']),
                    str(s['test_rotated']['correct']),f"{stage['training_seconds']/60:.1f}",f"${cost:.3f}"])
                sub=folder/f"stage-{i}-{stage['method']}"
                c=json.loads((sub/'checkpoints.json').read_text())
                curves+=f"<h3>{e(stage['method'].upper())}</h3>"+chart([('Development accuracy',[(0,b['dev']['accuracy'])]+[(x['elapsed_seconds'],x['accuracy']) for x in c])],'Seconds','Accuracy')
                old=json.loads((sub/'before_test.json').read_text());new=json.loads((sub/'after_test.json').read_text())
                for x,y in selected_pairs(old,new):
                    prompt=x['question']+'\n'+'\n'.join(f"{letter}. {option}" for letter,option in zip('ABC',x['options']))+'\nKey: '+x['answer']
                    examples+=pair(prompt,x['prediction'],y['prediction'])
        elif kind=='reasoning':
            keys={x['id']:x['answer'] for x in json.loads((folder/'data.json').read_text())['test']}
            diagnostic=[]
            for phase in ('before','after'):
                rows=json.loads((folder/f'{phase}_test.json').read_text())
                answers=[re.findall(r'Odpowiedź:\s*([ABC])\b',x['text'],re.I) for x in rows]
                correct=sum(bool(a) and a[-1].upper()==keys[x['id']] for x,a in zip(rows,answers))
                bare=sum(bool(re.fullmatch(r'(?:Odpowiedź:\s*)?[ABC][.!]?\s*',x['text'],re.I)) for x in rows)
                diagnostic.append((correct,bare))
            tables[kind].append([r['model_spec']['id'],str(r['steps']),str(r['selected_step']),
                f"{r['before']['test']['successes']} → {r['after']['test']['successes']}",
                f"{diagnostic[0][0]} → {diagnostic[1][0]}",f"{diagnostic[0][1]} → {diagnostic[1][1]}",
                f"{r['training_seconds']/60:.1f}",f"$"+"{:.3f}".format(cost)])
            c=json.loads((folder/'checkpoint_selection.json').read_text())
            curves=chart([('Development success',[(0,r['before']['dev']['successes']/25)]+[(v['step'],v['successes']/25) for v in c['checkpoints']])],'Updates','Success')
            old=json.loads((folder/'before_test.json').read_text());new=json.loads((folder/'after_test.json').read_text())
            for x,y in selected_pairs(old,new):examples+=pair(x['prompt'],x['text'],y['text'])
        elif kind=='evaluate':
            common=r['common'];names=['wiki-scratch-v1','wiki-leads-v1','wiki-plain-leads-v1','wiki-plain-leads-v2']
            tables[kind].append([r['base_run'],r['base_task']]+[f"{common[n]['test']['loss_nats']:.3f}" if n in common else '—' for n in names]+[str(r['quality_raw']['correct'])+'/10',str(r['quality_plain']['correct'])+'/10',f"${cost:.3f}"])
            examples='<p>Greedy instruction diagnostics; no instruction fine-tuning unless explicitly labeled. References are illustrative, not an automatic score.</p>'
            for probe in r['instruction_probes']:
                examples+='<h4>'+e(probe['prompt'])+'</h4><pre>'+e(probe['text'])+'</pre>'
            for row in r.get('continuation_decoding',[]):
                examples+='<h4>'+e(row['prompt'])+('; new article' if row.get('document_start') else '')+'; temperature '+str(row['temperature'])+'</h4><pre>'+e(row['text'])+'</pre>'
            for suffix in ('raw','plain'):
                quality=json.loads((folder/('quality_'+suffix+'.json')).read_text())
                examples+='<h3>'+suffix.title()+' continuation prompts</h3>'
                for row in quality['free_generations']:
                    examples+='<h4>'+e(row['prompt'])+'</h4><pre>'+e(row['continuation'])+'</pre>'
        else:
            config=r['config'];w=config['width']
            params=config['vocab_size']*w+config['layers']*(2*w+4*w*w+3*w*config['hidden'])+w
            corpus='Wolne Lektury' if ('wolne' in str(r.get('base_data','')).lower() or '-wl-' in r['base_run'] or 'wolne-lektury' in r['base_run']) else 'Polish Wikipedia'
            base_label=f"{params/1e6:.1f}M "+('random weights' if r['initialization']=='random' else corpus)
            task_label={'exam':f"{len(json.loads((folder/'data.json').read_text())['train'])} driving questions",'poetry':'450 Pan Tadeusz Q&A','wiki-qa':f"{len(json.loads((folder/'data.json').read_text())['train']):,} Wikipedia definitions",'instruction':'Polish OWCA instructions'}[spec['task']]
            for stage_index,stage in enumerate(r['stages']):
                after=stage['after']['test'];before=r['before']['test']
                metric=(f"{before['correct']} → {after['correct']}" if spec['task']=='exam' else f"{before['loss']:.3f} → {after['loss']:.3f}")
                tables[kind].append([base_label,r['initialization'],task_label,' → '.join(x['method'] for x in r['stages'][:stage_index+1])+(' (LoRA '+str(spec['lora_rank'])+')' if spec.get('lora_rank') else '')+(' (3-action CE + KL)' if spec.get('sft_actions_only') else ''),f"{spec['lr']:g}",
                                    metric,f"{stage['training_seconds']/60:.1f}",f"${cost:.3f}"])
                h=json.loads((folder/f"{stage['method']}_history.json").read_text())
                metric_name='accuracy' if spec['task']=='exam' else 'loss'
                curves+=f"<h3>{e(stage['method'].upper())}</h3>"+chart([('Development '+metric_name,[(v['seconds'],v['dev'][metric_name]) for v in h])],'Seconds',metric_name.title())
                if spec['task']=='exam':
                    old=json.loads((folder/'before_test.json').read_text());new=json.loads((folder/f"{stage['method']}_after_test.json").read_text())
                    for x,y in selected_pairs(old,new):
                        examples+=pair(x['question']+'\nKey: '+x['answer'],x['prediction'],y['prediction'])
                else:
                    old=json.loads((folder/'samples_before.json').read_text());new=json.loads((folder/f"{stage['method']}_samples_after.json").read_text())
                    for x,y in selected_pairs(old,new):examples+=pair(x['prompt'],x['text'],y['text'])
        if kind=='scratch':detail_title=f"{model} trained on {spec['data']}, {spec['gpu']}"
        elif kind=='exam':detail_title=f"{spec['model']} + {' → '.join(spec['methods']).upper()} on {r['stages'][0]['before']['train']['n']} driving questions, seed {spec.get('seed',42)}"
        elif kind=='reasoning':detail_title=f"{r['model_spec']['id']} + final-answer RLVR, sampled explanations"
        elif kind=='evaluate':detail_title=f"Saved checkpoint diagnostics: {r['base_run']} ({r['base_task']})"
        else:detail_title=f"{base_label} + {spec['method'].upper()} on {task_label}"
        if superseded(spec):examples='<p><strong>Superseded data:</strong> the v1 reference-removal expression could remove prose after self-closing references. Retained for audit; do not use to select a workshop recipe.</p>'+examples
        details.append(f"<details><summary>{e(detail_title)}</summary><p>Run: {e(folder.name)}</p><p>{e(json.dumps(spec,ensure_ascii=False))}</p>{curves}{examples}</details>")
    headers={
      'scratch':['Model','Corpus','Context','GPU','Training min','Test loss','Tokens M','Corpus-equivalents','Tokens M / $','Worker $'],
      'exam':['Starting model','Method','Train questions','GPU / batch','LR','Seed','Test /40','Dev /25','Rotated /40','Training min','Run worker $'],
      'reasoning':['Model','Steps','Selected step','Strict final-answer score /40','Answer anywhere /40','Answer-only outputs /40','Training min','Worker $'],
      'evaluate':['Checkpoint','Stage','Raw Wikipedia test loss','Raw leads test loss','Plain v1 test loss (superseded)','Plain v2 test loss','Raw fact probes','Plain fact probes','Evaluation worker $'],
      'posttrain':['Starting checkpoint','Initialization','Task','Stage','LR','Test correct /40 or answer loss','Training min','Run worker $']}
    titles={'scratch':'GPU and architecture comparisons','exam':'Driving exam: existing models','posttrain':'Scratch models after pretraining','reasoning':'Driving exam: explanation prompt, final-answer RLVR','evaluate':'Common-corpus and instruction diagnostics'}
    intro="""# Training comparisons

Exploratory measurements, not guaranteed outcomes. Checkpoints are selected using development data. Test sets are small and have been inspected in previous experiments; these are not fresh, blind benchmarks.

Plain-text corpus v1 and the earlier 5,000-definition data used a faulty reference-removal expression. It could delete intervening prose after a self-closing ref. Those data comparisons are superseded; original-markup Wikipedia and Wolne Lektury are unaffected. Version2 fixes this with a regression test.

Costs are worker GPU + CPU/memory estimates, excluding image builds, controller and storage. Post-training and continued-pretraining costs exclude the earlier pretraining. For chains, the cost shown on each stage row is the whole run, not an additional charge. Losses on different corpora cannot be compared directly. Existing-model SFT→RLVR chains use the original base model as the KL reference; scratch-model chains use the SFT checkpoint. These are different regularization choices. Wikipedia definition loss uses 50 held-out examples whose articles retain their original pretraining split; this is not a test of recalling facts from those same articles in training. Poetry loss uses 25 held-out prompts, but their source verses may appear in pretraining.
"""
    findings = [
        'For ten-minute Wolne Lektury pretraining, H100 processed more tokens per dollar than L4. Compiling the training forward almost doubled throughput again; it did not double text quality.',
        'The cheaper expanded-data SFT recipe reached 31–32/40 across three seeds in three minutes, about $0.07 per worker. Rotated options gave 30–33/40. This is the practical workshop extension.',
        'Qwen3.5-0.8B + SFT on 289 official driving questions reached 33–35/40 across three seeds, versus 21/40 before training. Direct RLVR reached 29–33/40. Each run cost about $0.19; rotated options reveal remaining sensitivity.',
        'Wikipedia-pretrained 98M and 291M scratch models reached 20/40 with full-weight SFT and 22/40 with LoRA on 100 driving questions. Expanded-data scratch SFT reached 21–23/40. Direct RLVR did not improve the 100-question models. These results do not establish full-exam passing ability.',
        'SFT on 5,000 Wikipedia title/definition pairs taught short-answer formatting, but answers still invented facts. Wolne Lektury + Pan Tadeusz Q&A learned verse-like replies with weak relevance and meter.',
        'With an explanation prompt, Qwen3.5-2B RLVR improved strict final-answer compliance from 0 to 25/40 by removing explanations. Accepting the explicit answer anywhere gives 25/40 both before and after. The reward did not require an explanation; this is format learning, not evidence of better reasoning. The any-position score is a post-hoc diagnostic, not the training reward.',
        'Thirty-minute Wolne Lektury pretraining improved test loss to 2.720 for $2.12. Ten minutes with compilation reached 2.748 for $0.73: a more practical workshop recipe.',
    ]
    failures={}
    for p in (ROOT/'runs').glob('night-*/manifest.json'):
        for index,item in enumerate(json.loads(p.read_text()).get('results',[])):
            if item['status']=='failed':failures[item.get('run',str(p)+':'+str(index))]=item
    failed_cost=sum(f.get('estimated_compute_usd',0) for f in failures.values())
    intro+=f"\nFailed/canceled calls recorded: {len(failures)}; known worker estimates $"+"{:.3f}".format(failed_cost)+". Canceled calls have unknown billing; an additional $8.257 full-timeout bound is reserved separately.\n"
    md=intro+f"\nCompleted workers in this report: ${total:.3f}.\n"
    md+='\n## What changed\n\n'+'\n'.join('- '+f for f in findings)+'\n'
    body='<h1>Training comparisons</h1><p>'+e(intro.split('\n\n',1)[1])+'</p>'+f'<p>Completed workers: ${total:.3f}.</p>'
    body+='<h2>What changed</h2><ul>'+''.join('<li>'+e(f)+'</li>' for f in findings)+'</ul>'
    if (ROOT/'results/exam-comparison.svg').exists():
        body+='<h2>Driving exam: repeated runs</h2><img src="exam-comparison.svg" alt="Three seeds per exam training recipe" style="width:100%">'
        md+='\n![Repeated driving-exam runs](exam-comparison.svg)\n'
    body+='<h2>Choosing a checkpoint</h2><img src="checkpoint-selection.svg" alt="Development curves with selected and final checkpoints" style="width:100%">'
    md+='\n![Development curves: selected and final checkpoints](checkpoint-selection.svg)\n'
    if (ROOT/'results/wikipedia-scaling.svg').exists():
        body+='<h2>Wikipedia: does longer training help?</h2><img src="wikipedia-scaling.svg" alt="Measured Wikipedia loss against training time and worker cost" style="width:100%"><p>Original markup, shared 8k tokenizer. Runs differ in learning-rate schedule, batch size and compilation. Lower text loss does not establish factual accuracy.</p>'
        md+='\n![Wikipedia training time, loss and cost](wikipedia-scaling.svg)\n\nOriginal markup, shared 8k tokenizer. Schedules, batches and compilation differ; this is not a controlled scaling-law estimate. Lower text loss does not establish factual accuracy.\n'
    for kind in tables:
        if not tables[kind]:continue
        md+='\n## '+titles[kind]+'\n\n|'+'|'.join(headers[kind])+'|\n|'+'|'.join(['---']*len(headers[kind]))+'|\n'
        md+='\n'.join('|'+'|'.join(row)+'|' for row in tables[kind])+'\n'
        body+='<h2>'+titles[kind]+'</h2><div class="table"><table><thead><tr>'+''.join('<th>'+e(h)+'</th>' for h in headers[kind])+'</tr></thead><tbody>'
        body+=''.join('<tr>'+''.join('<td>'+e(v)+'</td>' for v in row)+'</tr>' for row in tables[kind])+'</tbody></table></div>'
    body+='<h2>GPU throughput and cost</h2><img src="gpu-comparison.svg" alt="GPU tokens and tokens per dollar" style="width:100%">'
    body+='<h2>Curves and selected examples</h2><p>First four examples per run, plus the first correction and regression when available. Complete predictions remain in the local run records.</p>'+''.join(details)
    md+='\n[Curves and selected literal before/after answers](training-comparisons.html).\n'
    (ROOT/'results/training-comparisons.md').write_text(md)
    (ROOT/'results/training-comparisons.html').write_text('<!doctype html><meta charset="utf-8"><title>Training comparisons</title><style>body{font:15px system-ui;max-width:1200px;margin:32px auto;padding:0 20px}.table{overflow:auto}table{border-collapse:collapse}th,td{padding:8px;border-bottom:1px solid #ddd;text-align:left}svg{width:100%;max-width:860px}details{margin:20px 0}summary{cursor:pointer;font-weight:600}pre{white-space:pre-wrap;overflow-wrap:anywhere}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}.pair section{background:#f4f6f8;padding:14px;min-width:0}h4{white-space:pre-wrap}@media(max-width:700px){.pair{grid-template-columns:1fr}}</style>'+body)
    print(len(records),'completed runs;',round(total,4),'worker USD')
def selected_pairs(before,after):
    key='id' if before and 'id' in before[0] else 'prompt'
    assert [r[key] for r in before]==[r[key] for r in after]
    pairs=list(zip(before,after));indices=list(range(min(4,len(pairs))))
    for old,new in ((False,True),(True,False)):
        found=next((i for i,(a,b) in enumerate(pairs) if a.get('correct',a.get('success'))==old and b.get('correct',b.get('success'))==new),None)
        if found is not None and found not in indices:indices.append(found)
    return [pairs[i] for i in indices]

def pair(prompt,before,after):
    return f'<h4>{e(prompt)}</h4><div class="pair"><section><b>Before</b><pre>{e(before)}</pre></section><section><b>After</b><pre>{e(after)}</pre></section></div>'

def save_svg(fig,name):
    import matplotlib
    path=ROOT/'results'/name
    with matplotlib.rc_context({'svg.hashsalt':name}):
        fig.savefig(path,metadata={'Date':None})
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')

def plot_gpus():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    tags=['wl30-L4','wl30-A10','wl30-L40S','wl30-H100','wl30-compiled-H100']
    found={}
    for p in (ROOT/'runs').glob('night-*/execution.json'):
        r=json.loads(p.read_text())
        if r.get('spec',{}).get('tag') in tags:found[r['spec']['tag']]=r
    if len(found)!=len(tags):return
    rows=[found[t] for t in tags]
    labels=['L4','A10','L40S','H100','H100\ncompiled']
    colors=['#487aa6']*4+['#d67a2a']
    plt.rcParams.update({'svg.hashsalt':'workshop-gpu-comparison','font.size':11})
    fig,axes=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
    values=[r['tokens_seen']/1e6 for r in rows]
    bars=axes[0].bar(labels,values,color=colors)
    axes[0].bar_label(bars,fmt='%.0fM',padding=4)
    axes[0].set_ylabel('Million token presentations in 10 minutes')
    axes[0].set_ylim(0,max(values)*1.15)
    value=[r['tokens_seen']/r['estimated_compute_usd']/1e6 for r in rows]
    bars=axes[1].bar(labels,value,color=colors)
    axes[1].bar_label(bars,fmt='%.0fM',padding=4)
    axes[1].set_ylabel('Million token presentations per worker dollar')
    axes[1].set_ylim(0,max(value)*1.15)
    for ax in axes:
        ax.spines[['top','right']].set_visible(False)
        ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    fig.suptitle('Ten-minute pretraining on Wolne Lektury\n30M parameters, batch 32, context 512')
    save_svg(fig,'gpu-comparison.svg')
    fig.savefig(ROOT/'results/gpu-comparison.png',dpi=160)
    plt.close(fig)


# A compact comparison of the repeated, budget-sized exam recipes.
def plot_exam():
    import matplotlib.pyplot as plt
    groups={('sft',180):[],('sft',600):[],('rlvr',600):[]}
    for p in (ROOT/'runs').glob('night-*/execution.json'):
        r=json.loads(p.read_text());s=r.get('spec',{})
        if s.get('kind')!='exam' or s.get('model')!='qwen3.5-0.8b' or s.get('dataset')!='prawko-expanded':continue
        key=(s['methods'][0],s['seconds'])
        if len(s['methods'])==1 and key in groups:groups[key].append(r['stages'][0])
    if any(len(rows)!=3 for rows in groups.values()):return
    labels=['Original','SFT\n3 minutes','SFT\n10 minutes','RLVR\n10 minutes']
    fig,axes=plt.subplots(1,2,figsize=(11,4.5),layout='constrained')
    for ax,split,title in zip(axes,['test','test_rotated'],['Original option order','Rotated option order']):
        baseline=groups[('sft',180)][0]['before'][split]['correct']
        values=[[baseline]]+[[s['after'][split]['correct'] for s in rows] for rows in groups.values()]
        means=[sum(v)/len(v) for v in values]
        ax.bar(labels,means,color=['#aaa','#487aa6','#487aa6','#d67a2a'],alpha=.65)
        for i,vals in enumerate(values):
            ax.scatter([i+(j-(len(vals)-1)/2)*.13 for j in range(len(vals))],vals,color='#222',zorder=3)
            ax.text(i,max(vals)+1,' / '.join(str(v) for v in vals),ha='center',fontsize=10)
        ax.set_ylim(0,40);ax.set_yticks(range(0,41,10));ax.set_ylabel('Correct answers / 40');ax.set_title(title)
        ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    fig.suptitle('Qwen3.5-0.8B, 289 official driving questions\nDots: three training seeds; bars: mean. Same 40 test questions.')
    save_svg(fig,'exam-comparison.svg');plt.close(fig)

def plot_stopping():
    """Fixed illustrative runs; validation selects checkpoints, test only compares them."""
    import matplotlib.pyplot as plt
    specs=[('night-1789675548767097321-wiki30-H100',None,'Wikipedia pretraining: 30M'),
           ('night-1789674358034520778-qwen3.5-0.8b-sft','stage-0-sft','Driving exam: Qwen3.5-0.8B SFT'),
           ('night-1789674358034520778-qwen3.5-0.8b-rlvr','stage-0-rlvr','Driving exam: Qwen3.5-0.8B RLVR')]
    if any(not (ROOT/'runs'/name/(sub or '')/'result.json').exists() for name,sub,_ in specs):return
    fig,axes=plt.subplots(1,3,figsize=(14,5),layout='constrained');audit=[]
    for ax,(name,sub,title) in zip(axes,specs):
        folder=ROOT/'runs'/name/(sub or '');r=json.loads((folder/'result.json').read_text());h=json.loads((folder/'checkpoints.json').read_text())
        if sub:
            key='steps';best=r['selected_steps'];metric='accuracy';before=r['before']['dev'][metric]
            points=[(0,before)]+[(v[key],v[metric]) for v in h]
            selected=r['after']['dev'][metric];final=r['final']['dev'][metric]
            selected_test=r['after']['test']['correct'];final_test=r['final']['test']['correct']
            note=f'Test /40: selected {selected_test}, final {final_test}'
            ax.set_ylabel('Development accuracy');ax.set_ylim(0,1)
        else:
            key='step';best=r['best_step'];metric='loss_nats';before=r['before']['dev'][metric]
            points=[(0,before)]+[(v[key],v[metric]) for v in h]
            selected=r['selected']['dev'][metric];final=r['final']['dev'][metric]
            selected_test=r['selected']['test'][metric];final_test=r['final']['test'][metric]
            note=f'Test loss: selected {selected_test:.3f}, final {final_test:.3f}'
            ax.set_ylabel('Development cross entropy');ax.set_ylim(1.5, min(4,before))
        points.append((r['steps'],final));ax.plot(*zip(*points),color='#487aa6')
        ax.axvline(best,color='#d67a2a',linestyle='--',alpha=.7)
        ax.scatter([best],[selected],marker='*',s=150,color='#d67a2a',label='Selected using dev',zorder=5)
        ax.scatter([r['steps']],[final],marker='x',s=65,color='#222',label='Final checkpoint',zorder=6)
        ax.set_title(title);ax.set_xlabel('Optimizer updates\n'+note);ax.legend(fontsize=8)
        ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.2)
        audit.append(dict(run=name,selected_step=best,final_step=r['steps'],selected_dev=selected,final_dev=final,selected_test=selected_test,final_test=final_test))
    fig.suptitle('When to stop: keep the best development checkpoint\nThe last update is not necessarily the best. Test scores do not select checkpoints.')
    save_svg(fig,'checkpoint-selection.svg');plt.close(fig)
    (ROOT/'results/checkpoint-selection.json').write_text(json.dumps(audit,indent=2))

def plot_wikipedia_scaling():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    names=[
        ('30M', 'night-1789681601127509000-wiki-30m-50min'),
        ('98M', 'night-1789681601127509000-wiki-100m-batch64-50min'),
        ('291M', 'night-1789681601127509000-wiki-300m-batch64-50min'),
        ('98M, earlier recipe', 'scratch-polish-dollar-1788900395083493729-wiki-100-uniform'),
        ('291M, earlier recipe', 'scratch-polish-dollar-1788900395083493729-wiki-300-uniform'),
    ]
    fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
    audit=[]
    for label,name in names:
        folder=ROOT/'runs'/name
        if not (folder/'execution.json').exists():continue
        r=json.loads((folder/'execution.json').read_text())
        checkpoints=json.loads((folder/'checkpoints.json').read_text())
        minutes=[x['elapsed_seconds']/60 for x in checkpoints]+[r['training_seconds']/60]
        losses=[x['loss_nats'] for x in checkpoints]+[r['final']['dev']['loss_nats']]
        line,=axes[0].plot(minutes,losses, '--' if 'earlier' in label else '-',label=label)
        cost=r['estimated_compute_usd'];loss=r['selected']['test']['loss_nats']
        axes[1].scatter(cost,loss,color=line.get_color(),marker='s' if 'earlier' in label else 'o')
        axes[1].annotate(label,(cost,loss),xytext=(4,5),textcoords='offset points',fontsize=8)
        audit.append(dict(run=name,label=label,training_minutes=r['training_seconds']/60,
                          worker_usd=cost,test_loss=loss,dev_minutes=minutes,dev_losses=losses,
                          tokens_seen=r['tokens_seen'],batch=r['batch_size'],peak_lr=r['peak_lr'],
                          compile_training=r.get('compile_training',False)))
    axes[0].set(xlabel='Training minutes',ylabel='Development loss (nats)',title='Measured checkpoints; lower is better')
    axes[0].legend(fontsize=8);axes[0].grid(alpha=.2)
    axes[1].set(xlabel='Estimated worker compute (USD)',ylabel='Selected test loss (nats)',title='Completed runs: quality versus cost',xlim=(0,12))
    axes[1].grid(alpha=.2)
    fig.suptitle('Polish Wikipedia from scratch: gains continue beyond short runs')
    save_svg(fig,'wikipedia-scaling.svg');plt.close(fig)
    (ROOT/'results/wikipedia-scaling.json').write_text(json.dumps(audit,indent=2)+'\n')

if __name__=='__main__':
    plot_wikipedia_scaling()
    plot_stopping()
    plot_gpus()
    plot_exam()
    render()
