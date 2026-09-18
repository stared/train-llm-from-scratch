# /// script
# requires-python = ">=3.14"
# dependencies = ["matplotlib==3.11.2"]
# ///
"""Curate the fetched overnight measurements, curves, and literal outputs."""
from html import escape
from collections import Counter
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
            or (spec.get('task')=='wiki-qa' and spec.get('dataset') in (None,'wiki-qa-research')))

def render():
    records=[]
    for path in sorted((ROOT/'runs').glob('night-*/execution.json')):
        fetching=path.parent/'fetch-status.json'
        if fetching.exists() and json.loads(fetching.read_text())['state']!='complete':continue
        r=json.loads(path.read_text())
        if 'spec' not in r:continue
        records.append((path.parent,r))
    tables={'scratch':[], 'exam':[], 'posttrain':[], 'reasoning':[], 'evaluate':[], 'extended':[], 'known':[]};details=[]
    total=0
    for folder,r in records:
        spec=r['spec'];cost=r['estimated_compute_usd'];total+=cost
        curves='';examples='';kind=spec['kind']
        if kind=='scratch':
            model=r['model']+(' (continued)' if r.get('initial_checkpoint_run') else '')+(' [Muon]' if r.get('optimizer_kind')=='muon' else '')+(' [superseded data]' if superseded(spec) else '');dataset=spec['data']+(' + '+spec['mixture_data'] if spec.get('mixture_data') else '')
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
            extended=r.get('extended_common',{})
            if extended:
                names=['wiki-scratch-v1','wiki-plain-leads-v2','wiki-plain-full-v1','wl-scratch-v1']
                tables['extended'].append([r['base_run'],r['checkpoint']]+[f"{extended[n]['test']['loss_nats']:.4f}" if n in extended else '—' for n in names]+[f"{next(iter(extended.values()))['test']['tokens']:,}"])
            examples='<p>Greedy instruction diagnostics; no instruction fine-tuning unless explicitly labeled. References are illustrative, not an automatic score.</p>'
            known=r.get('known_fact_recall')
            if known:
                tables['known'].append([r['base_run'],r['checkpoint'],known.get('prompt_condition','unseen prompt templates')]+[f"{known[s]['correct']}/{known[s]['n']}" for s in ('dev','test')])
                examples+='<p><strong>Known-fact probes:</strong> '+e(known['meaning'])+'.</p>'
                for row in json.loads((folder/'known_facts.json').read_text())['test'][:4]:
                    examples+='<h4>'+e(row['prompt'])+'</h4><pre>'+e(row['text'])+'</pre><p>Source-derived reference: '+e(row['answer'])+'</p>'
            for probe in r['instruction_probes']:
                examples+='<h4>'+e(probe['prompt'])+'</h4><pre>'+e(probe['text'])+'</pre>'
                if probe.get('reference') is not None:examples+='<p>Reference: '+e(probe['reference'])+'</p>'
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
            if r['initialization']!='random' and r.get('base_task','pretraining')!='pretraining':
                prior_label={'instruction':'OWCA instruction SFT','wiki-qa':'Wikipedia-definition SFT','exam':'exam post-training','poetry':'poetry SFT'}.get(r['base_task'],r['base_task'])
                prior_path=ROOT/'runs'/r['base_run']/'result.json'
                if prior_path.exists():
                    count=json.loads(prior_path.read_text()).get('split_sizes',{}).get('train')
                    if count:prior_label=f'{count:,} examples of '+prior_label
                base_label+=' + '+prior_label
            train_count=r.get('split_sizes',{}).get('train')
            if train_count is None:train_count=len(json.loads((folder/'data.json').read_text())['train'])
            definition_label=(f"{train_count:,} QA rows / {train_count//8:,} facts" if spec.get('dataset')=='wiki-short-qa-varied' else f"{train_count:,} Wikipedia definitions")
            task_label={'exam':f"{train_count} driving questions",'poetry':'450 Pan Tadeusz Q&A','wiki-qa':definition_label,'instruction':'Polish OWCA instructions'}[spec['task']]
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
                    for x,y in selected_pairs(old,new):
                        examples+=pair(x['prompt'],x['text'],y['text'])
                        if y.get('reference') is not None:examples+='<p><b>Dataset reference</b></p><pre>'+e(y['reference'])+'</pre>'
        if kind=='scratch':detail_title=f"{model} trained on {spec['data']}, {spec['gpu']}"
        elif kind=='exam':detail_title=f"{spec['model']} + {' → '.join(spec['methods']).upper()} on {r['stages'][0]['before']['train']['n']} driving questions, seed {spec.get('seed',42)}"
        elif kind=='reasoning':detail_title=f"{r['model_spec']['id']} + final-answer RLVR, sampled explanations"
        elif kind=='evaluate':detail_title=f"Saved checkpoint diagnostics: {r['base_run']} ({r['base_task']})"
        else:detail_title=f"{base_label} + {spec['method'].upper()} on {task_label}"
        if superseded(spec):examples='<p><strong>Superseded data:</strong> the v1 reference-removal expression could remove prose after self-closing references. Retained for audit; do not use to select a workshop recipe.</p>'+examples
        hardware=r.get('actual_gpu') or r.get('environment',{}).get('device') or 'Not recorded by this older runner'
        details.append(f"<details><summary>{e(detail_title)}</summary><p>Run: {e(folder.name)}</p><p>Hardware: {e(hardware)}. Requested GPU / billing rate: {e(spec['gpu'])}.</p><p>{e(json.dumps(spec,ensure_ascii=False))}</p>{curves}{examples}</details>")
    headers={
      'scratch':['Model','Corpus','Context','GPU','Training min','Test loss','Tokens M','Corpus-equivalents','Tokens M / $','Worker $'],
      'exam':['Starting model','Method','Train questions','GPU / batch','LR','Seed','Test /40','Dev /25','Rotated /40','Training min','Run worker $'],
      'reasoning':['Model','Steps','Selected step','Strict final-answer score /40','Answer anywhere /40','Answer-only outputs /40','Training min','Worker $'],
      'evaluate':['Checkpoint','Stage','Raw Wikipedia test loss','Raw leads test loss','Plain v1 test loss (superseded)','Plain v2 test loss','Raw fact probes','Plain fact probes','Evaluation worker $'],
      'extended':['Starting run','Weights','Original Wikipedia test loss','Plain leads v2 test loss','Full prose test loss','Wolne Lektury test loss','Tokens per split'],
      'known':['Starting run','Weights','Question wording','Development exact answers','Test exact answers'],
      'posttrain':['Starting checkpoint','Initialization','Task','Stage','LR','Test correct /40 or answer loss','Training min','Run worker $']}
    titles={'scratch':'GPU and architecture comparisons','exam':'Driving exam: existing models','posttrain':'Scratch models after pretraining','reasoning':'Driving exam: explanation prompt, final-answer RLVR','evaluate':'Common-corpus and instruction diagnostics (16k-token pools)','extended':'Larger held-out evaluations (1M-token pools)','known':'Short-answer recall of facts from training'}
    intro="""# Training comparisons

Exploratory measurements, not guaranteed outcomes. Training checkpoints are selected using development data; separately labeled final-weight diagnostics expose what this selection can miss. Test sets are small and have been inspected in previous experiments; these are not fresh, blind benchmarks.

Plain-text corpus v1 and the earlier 5,000-definition data used a faulty reference-removal expression. It could delete intervening prose after a self-closing ref. Those data comparisons are superseded; original-markup Wikipedia and Wolne Lektury are unaffected. Version2 fixes this with a regression test.

Costs are worker GPU + CPU/memory estimates, excluding image builds, controller and storage. Post-training and continued-pretraining costs exclude the earlier pretraining. For chains, the cost shown on each stage row is the whole run, not an additional charge. Losses on different corpora cannot be compared directly. Existing-model SFT→RLVR chains use the original base model as the KL reference; scratch-model chains use the SFT checkpoint. These are different regularization choices. Wikipedia definition loss uses up to50 held-out examples in earlier runs and200 in the100k-example study, retaining original pretraining splits. This differs from recall of familiar training entities. Poetry loss uses25 held-out prompts, but their source verses may appear in pretraining. Larger corpus evaluations use a separate fixed seed and1,048,576 tokens per split; keep them separate from the original16,384-token live curves.
"""
    findings = [
        'For ten-minute Wolne Lektury pretraining, H100 processed more tokens per dollar than L4. Compiling the training forward almost doubled throughput again; it did not double text quality.',
        'The cheaper expanded-data SFT recipe reached 31–32/40 across three seeds in three minutes, about $0.07 per worker. Rotated options gave 30–33/40. This is the practical workshop extension.',
        'Qwen3.5-0.8B + SFT on 289 official driving questions reached 33–35/40 across three seeds, versus 21/40 before training. Direct RLVR reached 29–33/40. Each run cost about $0.19; rotated options reveal remaining sensitivity.',
        'On 289 driving questions, Wikipedia-pretrained 291M direct RLVR reached 26–27/40 across three seeds. A matched three-action supervised loss plus the same KL penalty reached 25–27/40; rotated options gave 22–25 and 21–24 respectively. This small, repeatedly inspected test does not establish a large RLVR advantage or official-exam passing ability.',
        'Grounded SFT on 9,602 Wikipedia definitions learned answer formatting and some familiar paragraphs. Longer training worsened held-out definition loss while improving recall of a Warsaw training example. The earlier 5,000-definition experiment used faulty reference removal and is superseded. Wolne Lektury + Pan Tadeusz Q&A learned verse-like replies with weak relevance and meter.',
        'With an explanation prompt, Qwen3.5-2B RLVR improved strict final-answer compliance from 0 to 25/40 by removing explanations. Accepting the explicit answer anywhere gives 25/40 both before and after. The reward did not require an explanation; this is format learning, not evidence of better reasoning. The any-position score is a post-hoc diagnostic, not the training reward.',
        'Thirty-minute Wolne Lektury pretraining improved test loss to 2.720 for $2.12. Ten minutes with compilation reached 2.748 for $0.73: a more practical workshop recipe.',
        'Original-markup Wikipedia 98M test loss improved from 1.619 at ten minutes to 1.426 at thirty and 1.339 at fifty ($3.56 worker compute). The older 133-minute recipe reached 1.301. Schedules and batches differ; loss gains continue, but generated facts remain unreliable.',
        'Another fifty minutes improved all four Wikipedia checkpoints. On the separate million-token test pool, 98M improved 1.303→1.241 from the fifty-minute base; 291M improved 1.328→1.249. The older 133-minute bases improved 1.265→1.222 and 1.246→1.201. Extra worker cost: $3.55–3.62 each. Driving-exam transfer did not improve consistently.',
        'Short-definition SFT produces a visible narrow result: the historical 291M Wikipedia model recalls 72/100 known definitions after single-wording SFT versus 93/100 after eight-wording SFT, with 30 presentations per fact in both. It still fails arithmetic and general instructions. This is recall of supplied facts, not an unseen-knowledge benchmark.',
        'Seven fresh raw-Wikipedia candidates near $10 were compared using the same million-token development pool. The 291M B200 run leads: 83 minutes, $9.13, test loss1.184. Its generated facts remain unreliable. Downstream exam scores also do not beat the earlier checkpoint: SFT21–26/40, three-action SFT+KL25–26/40, RLVR21–23/40 across three seeds.',
        'B200 processed 567M tokens for $1.14 with 98M parameters in ten minutes, versus 298M for $0.79 on H100 and 328M for $0.87 on H200, at batch64/context512. Hardware and compilation startup matter; token throughput alone is not model quality.',
        'A general Polish instruction stage did not improve the first matched scratch-model driving comparison: 291M direct SFT scored 25/40 versus 19/40 after instruction SFT. Treat instruction formatting and task competence as separate measurements.',
    ]
    failures={}
    for p in (ROOT/'runs').glob('night-*/manifest.json'):
        for index,item in enumerate(json.loads(p.read_text()).get('results',[])):
            if item['status']=='failed':failures[item.get('run',str(p)+':'+str(index))]=item
    failed_cost=sum(f.get('estimated_compute_usd',0) for f in failures.values())
    intro+=f"\nFailed/canceled calls recorded: {len(failures)}; known worker estimates $"+"{:.3f}".format(failed_cost)+". Canceled calls with unknown billing retain conservative timeout reservations in the local budget ledger; they are not counted as free.\n"
    counts=Counter(r['spec']['kind'] for _,r in records)
    count_summary=(f"Completed workers: {counts['scratch']} pretraining, "
                   f"{counts['posttrain']+counts['exam']+counts['reasoning']} post-training, "
                   f"{counts['evaluate']} evaluation only. These are runs, not distinct model architectures.")
    md=intro+f"\n{count_summary}\n\nWorker compute in this report: ${total:.3f}.\n"
    md+='\n## What changed\n\n'+'\n'.join('- '+f for f in findings)+'\n'
    body='<h1>Training comparisons</h1><p>'+e(intro.split('\n\n',1)[1])+'</p>'+f'<p>{e(count_summary)} Worker compute: ${total:.3f}.</p>'
    body+='<h2>What changed</h2><ul>'+''.join('<li>'+e(f)+'</li>' for f in findings)+'</ul>'
    if (ROOT/'results/exam-comparison.svg').exists():
        body+='<h2>Driving exam: repeated runs</h2><img src="exam-comparison.svg" alt="Three seeds per exam training recipe" style="width:100%">'
        md+='\n![Repeated driving-exam runs](exam-comparison.svg)\n'
    if (ROOT/'results/scratch-exam-comparison.svg').exists():
        body+='<h2>Wikipedia to the driving exam</h2><img src="scratch-exam-comparison.svg" alt="Scratch-model supervised and reinforcement-learning controls" style="width:100%">'
        md+='\n![Wikipedia to the driving exam: measured controls](scratch-exam-comparison.svg)\n'
    if (ROOT/'results/scratch-exam-transfer.svg').exists():
        body+='<h2>Latest Wikipedia checkpoint: exam transfer</h2><img src="scratch-exam-transfer.svg" alt="Three-seed exam transfer after longer Wikipedia pretraining" style="width:100%">'
        md+='\n![Latest Wikipedia checkpoint: exam transfer](scratch-exam-transfer.svg)\n'
    if (ROOT/'results/wiki-qa-recall.svg').exists():
        body+='<h2>Pretraining and question wording</h2><img src="wiki-qa-recall.svg" alt="Known-fact recall after supervised training, comparing pretraining and question diversity" style="width:100%">'
        md+='\n![Known-fact recall and SFT question wording](wiki-qa-recall.svg)\n'
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
    if (ROOT/'results/wikipedia-gpus.svg').exists():
        body+='<h2>Wikipedia GPU comparison</h2><img src="wikipedia-gpus.svg" alt="Measured Wikipedia tokens per dollar and loss on H100, H200 and B200" style="width:100%">'
        md+='\n![Wikipedia GPU comparison](wikipedia-gpus.svg)\n'
    if (ROOT/'results/wikipedia-long-runs.svg').exists():
        body+='<h2>Longer Wikipedia runs</h2><img src="wikipedia-long-runs.svg" alt="Near-$10 Wikipedia training curves and common-pool evaluation" style="width:100%">'
        md+='\n![Longer Wikipedia runs](wikipedia-long-runs.svg)\n'
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

def plot_wikipedia_gpus():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    rows=[]
    for size in ('100m','300m'):
        for gpu in ('H100','H200','B200'):
            name=(f'night-1789685347749346000-{size}-batch64-context512' if gpu=='H100'
                  else f'night-1789688810710019000-{size}-{gpu}-batch64')
            path=ROOT/'runs'/name/'execution.json'
            if not path.exists():return
            r=json.loads(path.read_text())
            rows.append(dict(run=name,size=size,gpu=gpu,actual_gpu=r['environment']['device'],
                tokens=r['tokens_seen'],worker_usd=r['estimated_compute_usd'],
                training_seconds=r['training_seconds'],compute_seconds=r['training_compute_seconds'],
                test_loss=r['selected']['test']['loss_nats']))
    fig,axes=plt.subplots(2,2,figsize=(11,7),layout='constrained')
    for i,size in enumerate(('100m','300m')):
        group=[r for r in rows if r['size']==size];labels=[r['gpu'] for r in group]
        values=[r['tokens']/r['worker_usd']/1e6 for r in group]
        bars=axes[i,0].bar(labels,values,color=['#487aa6','#6c9c72','#d67a2a'])
        axes[i,0].bar_label(bars,fmt='%.0fM',padding=4)
        axes[i,0].set(ylabel='Million tokens per worker dollar',ylim=(0,max(values)*1.2),title=('98M' if i==0 else '291M')+' parameters')
        losses=[r['test_loss'] for r in group]
        bars=axes[i,1].bar(labels,losses,color=['#487aa6','#6c9c72','#d67a2a'])
        axes[i,1].bar_label(bars,labels=[f'{r["test_loss"]:.3f}\n${r["worker_usd"]:.2f}' for r in group],padding=4)
        axes[i,1].set(ylabel='Selected test loss (lower is better)',ylim=(0,max(losses)*1.25))
        for ax in axes[i]:ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    fig.suptitle('Polish Wikipedia: ten-minute GPU comparisons\nBatch 64, context 512, compiled forward, AdamW LR 0.0006')
    fig.supxlabel('Includes compilation inside training budget; worker cost includes loading/evaluation. One run per setting.',fontsize=9)
    save_svg(fig,'wikipedia-gpus.svg');plt.close(fig)
    (ROOT/'results/wikipedia-gpus.json').write_text(json.dumps(rows,indent=2)+'\n')


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
    continued={
        names[1][1]:'night-1789685113120810000-100m-from-50min',
        names[2][1]:'night-1789685113120810000-300m-from-50min',
        names[3][1]:'night-1789685113120810000-100m-from-8000s',
        names[4][1]:'night-1789685113120810000-300m-from-8000s',
    }
    for label,name in names:
        folder=ROOT/'runs'/name
        if not (folder/'execution.json').exists():continue
        folders=[folder]
        follow=ROOT/'runs'/continued.get(name,'missing')
        if (follow/'execution.json').exists():folders.append(follow)
        minutes=[];losses=[];stages=[];offset=0;cost=0;restarts=[]
        for current in folders:
            r=json.loads((current/'execution.json').read_text())
            if offset:restarts.append((offset,r['before']['dev']['loss_nats']))
            checkpoints=json.loads((current/'checkpoints.json').read_text())
            minutes.extend([offset+x['elapsed_seconds']/60 for x in checkpoints]+[offset+r['training_seconds']/60])
            losses.extend([x['loss_nats'] for x in checkpoints]+[r['final']['dev']['loss_nats']])
            cost+=r['estimated_compute_usd'];offset+=r['training_seconds']/60
            stages.append(dict(run=current.name,training_minutes=r['training_seconds']/60,worker_usd=r['estimated_compute_usd'],
                               tokens_seen=r['tokens_seen'],batch=r['batch_size'],peak_lr=r['peak_lr'],compile_training=r.get('compile_training',False),
                               cumulative_cost=cost,selected_test_loss=r['selected']['test']['loss_nats']))
        line,=axes[0].plot(minutes,losses, '--' if 'earlier' in label else '-',label=label+(' + continuation' if restarts else ''))
        for x,y in restarts:axes[0].scatter(x,y,color=line.get_color(),marker='D',s=22)
        loss=r['selected']['test']['loss_nats']
        if len(stages)>1:
            axes[1].scatter(stages[0]['cumulative_cost'],stages[0]['selected_test_loss'],facecolors='none',edgecolors=line.get_color())
            axes[1].plot([s['cumulative_cost'] for s in stages],[s['selected_test_loss'] for s in stages],color=line.get_color(),alpha=.5)
        axes[1].scatter(cost,loss,color=line.get_color(),marker='s' if 'earlier' in label else 'o')
        axes[1].annotate(label.replace(', earlier recipe',' (old base)'),(cost,loss),xytext=(4,5),textcoords='offset points',fontsize=8)
        audit.append(dict(run=folders[-1].name,label=label,training_minutes=offset,
                          worker_usd=cost,test_loss=loss,dev_minutes=minutes,dev_losses=losses,
                          tokens_seen=sum(s['tokens_seen'] for s in stages),stages=stages))
    axes[0].set(xlabel='Total training minutes',ylabel='Development loss (nats)',title='Diamonds mark continuation with optimizer reset')
    axes[0].legend(fontsize=8);axes[0].grid(alpha=.2)
    axes[1].set(xlabel='Cumulative worker compute (USD)',ylabel='Selected test loss (16k-token sample)',title='Open markers: before continuation',xlim=(0,max(a['worker_usd'] for a in audit)*1.3))
    axes[1].grid(alpha=.2)
    fig.suptitle('Polish Wikipedia from scratch: gains continue beyond short runs')
    save_svg(fig,'wikipedia-scaling.svg');plt.close(fig)
    (ROOT/'results/wikipedia-scaling.json').write_text(json.dumps(audit,indent=2)+'\n')

def plot_long_wikipedia():
    """Fresh near-$10 raw-Wikipedia recipes, evaluated on one fixed pool."""
    import matplotlib.pyplot as plt
    batches={'1789686602382545000','1789687464977579000','1789689694697165000'}
    evaluations={}
    for path in (ROOT/'runs').glob('night-*/execution.json'):
        result=json.loads(path.read_text())
        common=result.get('extended_common',{}).get('wiki-scratch-v1')
        if common and result.get('checkpoint')=='best.pt':
            evaluations[result['base_run']]=(path.parent.name,common)
    rows=[]
    for batch in sorted(batches):
        for path in sorted((ROOT/'runs').glob(f'night-{batch}-*/execution.json')):
            result=json.loads(path.read_text());spec=result.get('spec',{})
            if spec.get('kind')!='scratch' or spec.get('mixture_data') or path.parent.name not in evaluations:continue
            evaluation,common=evaluations[path.parent.name]
            assert common['seed']==20260918 and common['test']['tokens']==1048576
            label=f"{result['parameters']/1e6:.0f}M {spec['gpu']}"
            if 'wide' in spec['size']:label+=' wide'
            if spec.get('sampling')=='shuffled':label+=' shuffled'
            rows.append(dict(run=path.parent.name,evaluation=evaluation,label=label,
                minutes=result['training_seconds']/60,worker_usd=result['estimated_compute_usd'],
                tokens=result['tokens_seen'],dev_loss=common['dev']['loss_nats'],test_loss=common['test']['loss_nats'],
                checkpoints=json.loads((path.parent/'checkpoints.json').read_text())+[
                    dict(step=result['steps'],elapsed_seconds=result['training_seconds'],loss_nats=result['final']['dev']['loss_nats'])],
                selected_step=result['best_step'],final_step=result['steps']))
    if not rows:return
    rows.sort(key=lambda r:r['dev_loss'])  # Declared selection uses development, never test.
    fig,axes=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
    for i,row in enumerate(rows):
        points=row['checkpoints'];color=f'C{i}'
        axes[0].plot([p['elapsed_seconds']/60 for p in points],[p['loss_nats'] for p in points],color=color,label=row['label'])
        chosen=next((p for p in points if p['step']==row['selected_step']),None)
        if chosen:axes[0].scatter(chosen['elapsed_seconds']/60,chosen['loss_nats'],color=color,marker='*',s=80,zorder=4)
        axes[1].scatter(row['test_loss'],i,color=color,s=70)
        axes[1].annotate(f"  ${row['worker_usd']:.2f}, {row['minutes']:.0f} min, {row['tokens']/1e9:.2f}B tokens",
                         (row['test_loss'],i),xytext=(5,6),textcoords='offset points',fontsize=8)
    axes[0].set(xlabel='Training minutes',ylabel='Development loss (16k-token pool)',title='Stars: checkpoints selected using development loss')
    axes[0].legend(fontsize=8);axes[0].grid(alpha=.2)
    axes[1].set(yticks=range(len(rows)),yticklabels=[r['label'] for r in rows],xlabel='Test loss (fixed 1,048,576-token pool)',title='Rows ordered by million-token development loss')
    axes[1].invert_yaxis();axes[1].margins(x=.8,y=.2);axes[1].grid(axis='x',alpha=.2)
    fig.suptitle('Fresh Polish Wikipedia pretraining near $10 per run')
    fig.supxlabel('Same raw markup, 8k tokenizer, batch64 and context512. Single runs; GPU recipes have different wall-clock budgets.',fontsize=9)
    save_svg(fig,'wikipedia-long-runs.svg');plt.close(fig)
    (ROOT/'results/wikipedia-long-runs.json').write_text(json.dumps(rows,indent=2)+'\n')


def plot_scratch_exam():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    groups=['Random\n+ SFT','Random\n+ RLVR','Wiki\n+ SFT','Wiki\n+ conditional SFT','Wiki\n+ RLVR','Wiki + short SFT\n+ RLVR','Wiki + instruction\n+ SFT']
    batches=('1789681233954934000','1789682451250225000','1789683433671484000','1789681777371983000')
    rows=[]
    for batch in batches:
        for path in sorted((ROOT/'runs').glob('night-'+batch+'-*/execution.json')):
            r=json.loads(path.read_text())
            if r['task']!='exam' or r['lr']!=1e-6:continue
            spec=r['spec'];tag=spec['tag']
            if r['initialization']=='random':group=0 if r['method']=='sft' else 1
            elif 'instruction' in tag:
                if r['method']!='sft':continue
                group=6
            elif r.get('sft_actions_only'):group=3
            elif 'sft-then-rlvr' in tag:group=5
            else:group=2 if r['method']=='sft' else 4
            stage=r['stages'][-1]
            rows.append(dict(run=path.parent.name,model='98M' if r['config']['width']==768 else '291M',
                group=group,seed=r['seed'],original=stage['after']['test']['correct'],
                rotated=stage['after']['test_rotated']['correct'],selected_step=stage['selected_step']))
    fig,axes=plt.subplots(1,2,figsize=(14,5.6),layout='constrained',sharey=True)
    for ax,model in zip(axes,['98M','291M']):
        for group in range(len(groups)):
            records=[r for r in rows if r['model']==model and r['group']==group]
            for metric,color,shift in [('original','#2166ac',-.13),('rotated','#d95f02',.13)]:
                for i,r in enumerate(records):
                    x=group+shift+(i-(len(records)-1)/2)*.035
                    ax.scatter(x,r[metric],color=color,s=35,alpha=.8)
                if records:
                    mean=sum(r[metric] for r in records)/len(records)
                    ax.plot([group+shift-.08,group+shift+.08],[mean,mean],color=color,lw=2)
        ax.axhline(40/3,color='gray',ls=':',label='Uniform random expectation')
        ax.set(title=model+' parameters',xticks=range(len(groups)),xticklabels=groups,ylim=(0,40),ylabel='Correct answers out of 40')
        ax.tick_params(axis='x',rotation=30,labelsize=8);ax.grid(axis='y',alpha=.2)
    axes[0].scatter([],[],color='#2166ac',label='Original option order')
    axes[0].scatter([],[],color='#d95f02',label='Rotated options')
    axes[0].legend(fontsize=8,loc='upper left')
    fig.suptitle('Polish Driving Licence Exam: Wikipedia pretraining and post-training\n289 training questions; dev-selected weights. Dots = runs, bars = means; 1–3 seeds per recipe.')
    fig.supxlabel('Exploratory, repeatedly inspected 40-question test. Random controls use the same low LR, not a tuned scratch baseline.',fontsize=9)
    save_svg(fig,'scratch-exam-comparison.svg');plt.close(fig)
    (ROOT/'results/scratch-exam-comparison.json').write_text(json.dumps(rows,indent=2)+'\n')

def plot_known_recall():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    groups=[
        ('98M\nrandom weights','1789690403457968000','100m-random-short-final','100m-random-varied-final'),
        ('98M\n10min Wikipedia','1789690403457968000','100m-10min-short-final','100m-10min-varied-final'),
        ('291M\n10min Wikipedia','1789690403457968000','300m-10min-short-final','300m-10min-varied-final'),
        ('291M\n133min Wikipedia','1789694506585130000','300m-single-30passes-final','300m-8000s-varied-final'),
    ]
    rows=[]
    for i,(label,batch,plain,varied) in enumerate(groups):
        for condition,name in [('one wording',f'night-{batch}-{plain}'),('eight wordings',f'night-1789691672093057000-{varied}')]:
            folder=ROOT/'runs'/name
            if not (folder/'execution.json').exists():return
            result=json.loads((folder/'execution.json').read_text());score=result['known_fact_recall']
            training=json.loads((ROOT/'runs'/result['base_run']/'execution.json').read_text())
            stage=training['stages'][-1]
            rows.append(dict(group=i,label=label.replace('\n',' '),wording=condition,run=name,
                pretraining_run=training['base_run'],sft_run=result['base_run'],weights=result['checkpoint'],
                dev_correct=score['dev']['correct'],test_correct=score['test']['correct'],n=score['test']['n'],
                mean_fact_presentations=stage['exposure_ratio']*(8 if condition=='eight wordings' else 1),
                sft_seconds=stage['training_seconds'],sft_worker_usd=training['estimated_compute_usd'],
                probes_sha256=score['probes_sha256']))
    assert len({r['probes_sha256'] for r in rows})==1
    fig,ax=plt.subplots(figsize=(11,5),layout='constrained')
    for condition,shift,color in [('one wording',-.18,'#487aa6'),('eight wordings',.18,'#d67a2a')]:
        group=[r for r in rows if r['wording']==condition]
        bars=ax.bar([r['group']+shift for r in group],[r['test_correct'] for r in group],width=.34,color=color,label=condition.capitalize()+' per fact')
        ax.bar_label(bars,labels=[str(r['test_correct'])+('*' if r['mean_fact_presentations']<29.9 else '') for r in group],padding=4)
    ax.set(xticks=range(len(groups)),xticklabels=[g[0] for g in groups],ylim=(0,105),ylabel='Exact definitions out of 100',
           title='Known Wikipedia facts, new question wording\nSame 8,912 training facts; four frozen evaluation question templates')
    ax.legend(loc='upper left');ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    fig.supxlabel('Final SFT weights; 30 presentations per fact. Known facts, not unseen knowledge. Single runs.',fontsize=9)
    save_svg(fig,'wiki-qa-recall.svg');plt.close(fig)
    (ROOT/'results/wiki-qa-recall.json').write_text(json.dumps(rows,indent=2)+'\n')


def plot_latest_exam_transfer():
    import matplotlib.pyplot as plt
    groups={label:[] for label in ['Markup\nSFT','Markup\n3-letter SFT + KL','Markup\nRLVR',
        'Prose\nSFT','Prose\nRLVR','Prose + instruction\nSFT','Prose + instruction\nRLVR']}
    for path in (ROOT/'runs').glob('night-*/execution.json'):
        r=json.loads(path.read_text());spec=r.get('spec',{});tag=spec.get('tag','')
        if spec.get('task')!='exam':continue
        if tag.startswith('best-wiki-'):prefix='Markup'
        elif tag.startswith('full-prose-instruction-'):prefix='Prose + instruction'
        elif tag.startswith('full-prose-'):prefix='Prose'
        else:continue
        method='3-letter SFT + KL' if spec.get('sft_actions_only') else spec['method'].upper()
        stage=r['stages'][-1];label=prefix+'\n'+method
        if label not in groups:continue
        groups[label].append(dict(run=path.parent.name,label=label,base=r['base_run'],seed=spec['seed'],
            before=r['before']['test']['correct'],test=stage['after']['test']['correct'],
            before_rotated=r['before']['test_rotated']['correct'],rotated=stage['after']['test_rotated']['correct'],
            selected_step=stage['selected_step'],steps=stage['steps'],worker_usd=r['estimated_compute_usd']))
    groups={label:sorted(rows,key=lambda r:r['seed']) for label,rows in groups.items()
            if len(rows)==3 and {r['seed'] for r in rows}=={42,123,2026}}
    if not groups:return
    fig,axes=plt.subplots(2,1,figsize=(12,8),sharex=True,layout='constrained')
    for ax,metric,before,title in zip(axes,['test','rotated'],['before','before_rotated'],['Original option order','Rotated option order']):
        for i,(label,rows) in enumerate(groups.items()):
            scores=[r[metric] for r in rows];baselines={r[before] for r in rows}
            assert len(baselines)==1
            color='#d67a2a' if label.endswith('RLVR') else '#6c9c72' if '3-letter' in label else '#487aa6'
            ax.bar(i,sum(scores)/3,color=color,alpha=.7,width=.65)
            ax.scatter([i-.13,i,i+.13],scores,color='#222',s=25,zorder=4)
            ax.scatter(i,baselines.pop(),marker='D',color='#aaa',edgecolor='#555',zorder=5,label='Before exam training' if i==0 else None)
            ax.text(i,max(scores)+1,' / '.join(map(str,scores)),ha='center',fontsize=9)
        ax.set(title=title,ylabel='Correct answers / 40',ylim=(0,40),yticks=range(0,41,5))
        ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True);ax.legend(loc='upper right',fontsize=9)
    axes[-1].set(xticks=range(len(groups)),xticklabels=list(groups))
    fig.suptitle('291M Wikipedia models → Polish Driving Licence Exam\nSame 289 training questions and 80-presentation limit; dots are three training seeds')
    fig.supxlabel('Development selects checkpoints using all six option permutations. Small, repeatedly inspected test; not official-exam passing evidence.',fontsize=9)
    save_svg(fig,'scratch-exam-transfer.svg');plt.close(fig)
    (ROOT/'results/scratch-exam-transfer.json').write_text(json.dumps([r for rows in groups.values() for r in rows],indent=2)+'\n')

if __name__=='__main__':
    plot_wikipedia_scaling()
    plot_long_wikipedia()
    plot_scratch_exam()
    plot_known_recall()
    plot_latest_exam_transfer()
    plot_stopping()
    plot_gpus()
    plot_wikipedia_gpus()
    plot_exam()
    render()
