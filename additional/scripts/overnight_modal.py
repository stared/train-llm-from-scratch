"""Bounded research batches; remote completion survives a disconnected laptop."""
import json
from pathlib import Path
import time
import modal

ROOT = Path(__file__).resolve().parents[2] if modal.is_local() else Path('/work')
app = modal.App('workshop-overnight-research')
volume = modal.Volume.from_name('model-training-workshop')
claims = modal.Dict.from_name('workshop-night-20260917-claims',create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements(str(ROOT/'scripts/requirements.txt'))
         .pip_install('numpy==2.5.3', 'tokenizers==0.23.2')
         .env({'HF_HOME':'/persist/hf', 'TOKENIZERS_PARALLELISM':'false','TORCHINDUCTOR_COMPILE_THREADS':'2'}))
for name in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py','prawko.py','models.json','rlvr_showcase.py','rlvr_tasks.py'):
    image = image.add_local_file(str(ROOT/'scripts'/name), '/work/scripts/'+name)
image = image.add_local_dir(str(ROOT/'datasets/prawko-v2'),'/work/datasets/prawko-v2')
image = image.add_local_dir(str(ROOT/'datasets/pan-tadeusz-qa-v1'),'/work/datasets/pan-tadeusz-qa-v1')
image=image.add_local_dir(str(ROOT/'datasets/local/prawko-expanded'),'/work/datasets/prawko-expanded')
image=image.add_local_file(str(ROOT/'additional/scripts/exam_reasoning.py'),'/work/additional/scripts/exam_reasoning.py')
image=image.add_local_file(str(ROOT/'additional/scripts/scratch_posttrain.py'),'/work/additional/scripts/scratch_posttrain.py')
image=image.add_local_file(str(ROOT/'additional/scripts/scratch_evaluate.py'),'/work/additional/scripts/scratch_evaluate.py')
image=image.add_local_dir(str(ROOT/'datasets/local/wiki-qa-research'),'/work/datasets/wiki-qa-research')
image=image.add_local_file(str(ROOT/'datasets/local/polish-instructions/data.json'),'/work/datasets/polish-instructions/data.json')
RATES = {'L4':.000222,'A10':.000306,'L40S':.000542,'H100':.001097}
CPU_RATE = 2*.0000131 + 16*.00000222
TIMEOUT = 3600
DEADLINE = 1789711200  # 2026-09-18 06:00 UTC / 08:00 Warsaw.

@app.function(image=image,gpu='H100',cpu=(2,2),memory=(16384,16384),
              timeout=TIMEOUT,retries=0,max_containers=4,scaledown_window=2,
              volumes={'/persist':volume})
def experiment(batch, spec):
    import sys, traceback, subprocess
    sys.path.insert(0,'/work/scripts')
    start=time.monotonic()
    name=f"night-{batch}-{spec['tag']}"
    out=Path('/persist/runs')/name
    rate=RATES[spec['gpu']]+CPU_RATE
    # Infrastructure preemption can retry despite retries=0. Never repeat paid training.
    if not claims.put(name,{'started_at':time.time()},skip_if_exists=True):
        previous=claims.get(name)
        return previous.get('result',dict(run=name,status='interrupted',cost_unknown=True,
            resource_bound_usd=TIMEOUT*rate,reason='Prior attempt claimed this run; automatic retraining disabled'))
    try:
        if time.time()+TIMEOUT>DEADLINE:
            raise RuntimeError('Insufficient time before 08:00 Warsaw hard deadline')
        volume.reload()
        if spec['kind']=='exam':
            from prawko import run
            initial=None
            stages=[]
            for i,method in enumerate(spec['methods']):
                path=out/f'stage-{i}-{method}'
                result=run(path,method,spec['model'],spec['seconds'],40,spec['lr'],spec.get('seed',42),
                           initial_adapter=initial,answer_text=spec.get('answer_text',False),
                           train_batch_size=spec.get('train_batch_size',4),eval_batch_size=spec.get('eval_batch_size',8),
                           dataset_path='/work/datasets/'+spec.get('dataset','prawko-v2')+'/data.json')
                stages.append(result)
                initial=str(path/'adapter')
                volume.commit()
            result={'stages':stages}
        elif spec['kind']=='reasoning':
            sys.path.insert(0,'/work/additional/scripts')
            from exam_reasoning import run
            result=run(out,spec['model'],spec['seconds'],spec['lr'],spec.get('token_limit',192),spec.get('thinking',False))
        elif spec['kind']=='posttrain':
            sys.path.insert(0,'/work/additional/scripts')
            from scratch_posttrain import run
            result=run('/persist/runs/'+spec['base'],out,spec['task'],spec['method'],
                       spec['seconds'],spec['lr'],spec.get('seed',42),spec.get('random_init',False),spec.get('lora_rank',0),spec.get('beta',.01),
                       dataset_path='/work/datasets/'+spec['dataset']+'/data.json' if spec.get('dataset') else None,
                       batch_size=spec.get('batch_size',4),max_epochs=spec.get('max_epochs'),
                       initial_weights='/persist/runs/'+spec['base']+'/'+spec['initial_checkpoint'] if spec.get('initial_checkpoint') else None,
                       eval_steps=spec.get('eval_steps',50),batched=spec.get('batched',False),
                       selection_permutations=spec.get('selection_permutations',False))
        elif spec['kind']=='evaluate':
            sys.path.insert(0,'/work/additional/scripts')
            from scratch_evaluate import run
            result=run('/persist/runs/'+spec['base'],out,spec.get('corpora',[]))
        elif spec['kind']=='scratch':
            from train_scratch import run
            next_quality=600
            def selected_diagnostics(model,tokenizer,stage,step,elapsed,path):
                nonlocal next_quality
                if stage=='checkpoint' and spec.get('quality_checkpoints') and elapsed>=next_quality:
                    import torch
                    from scratch_quality import evaluate_quality
                    quality=evaluate_quality(model,tokenizer,'cuda',None)
                    quality.update(step=step,training_seconds=elapsed)
                    (path/f'quality_step_{step}.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2))
                    if next_quality in (600,1800):torch.save(model.state_dict(),path/f'checkpoint-{next_quality}s.pt')
                    next_quality+=600
                if stage!='selected':return
                from scratch_quality import evaluate_fixed_pool,evaluate_quality,FACT_PROBES,FREE_PROMPTS
                for corpus in spec.get('common_eval',[]):
                    diagnostic=evaluate_fixed_pool(model,'cuda','/persist/datasets/'+corpus)
                    tokenizer_path=Path('/persist/datasets')/spec['data']/'tokenizer.json'
                    if diagnostic['tokenizer_sha256']!=__import__('hashlib').sha256(tokenizer_path.read_bytes()).hexdigest():
                        raise ValueError('Cross-corpus tokenizer mismatch')
                    (path/('common_'+corpus+'.json')).write_text(json.dumps(diagnostic,indent=2))
                if spec.get('quality'):
                    evaluate_quality(model,tokenizer,'cuda',path/'quality_raw.json')
                    probes=[dict(p,prompt=p['prompt'].replace("'''",'')) for p in FACT_PROBES]
                    evaluate_quality(model,tokenizer,'cuda',path/'quality_plain.json',fact_probes=probes,
                                     free_prompts=[p.replace("'''",'') for p in FREE_PROMPTS[:6]])
            result=run('/persist/datasets/'+spec['data'],out,spec['size'],spec['seconds'],
                spec.get('seed',42),'cuda',spec.get('batch',32),context_length=spec.get('context',512),
                eval_interval=60 if spec['seconds']<=600 else 300,peak_lr=spec.get('lr',6e-4),warmup_steps=100,
                research_limit_seconds=3000,compile_training=spec.get('compile',False),
                checkpoint_hook=selected_diagnostics if spec.get('common_eval') or spec.get('quality') or spec.get('quality_checkpoints') else None)
            subprocess.run([sys.executable,'/work/scripts/sample_scratch.py',str(out),'--device','cuda',
                            '--output',str(out/'reload_samples.json')],check=True,timeout=150)
            result['fresh_process_reload_matches']=json.loads((out/'reload_samples.json').read_text())==json.loads((out/'samples_selected.json').read_text())
            if not result['fresh_process_reload_matches']:raise RuntimeError('Reload mismatch')
        else:
            raise ValueError('Unknown kind')
        import torch
        result.update(actual_gpu=torch.cuda.get_device_name(),spec=spec,remote_seconds=time.monotonic()-start,
                      estimated_compute_usd=(time.monotonic()-start)*rate)
        out.mkdir(parents=True,exist_ok=True)
        (out/'execution.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        summary={'run':name,'status':'complete','estimated_compute_usd':result['estimated_compute_usd']}
    except Exception:
        out.mkdir(parents=True,exist_ok=True)
        summary={'run':name,'status':'failed','traceback':traceback.format_exc(),
                 'estimated_compute_usd':(time.monotonic()-start)*rate}
        (out/'failure.json').write_text(json.dumps(summary,indent=2))
    finally:
        post_source=Path('/work/additional/scripts/scratch_posttrain.py')
        if out.exists() and post_source.exists():(out/'executed_scratch_posttrain.py').write_bytes(post_source.read_bytes())
        for file in Path('/work/additional/scripts').glob('*.py'):
            if out.exists():(out/('executed_'+file.name)).write_bytes(file.read_bytes())
        for file in Path('/work/scripts').glob('*.py'):
            if out.exists():(out/('executed_'+file.name)).write_bytes(file.read_bytes())
        volume.commit()
    claims.put(name,{'result':summary})
    print(json.dumps(summary),flush=True)
    return summary

@app.function(image=image,cpu=(1,1),memory=(1024,1024),timeout=18000,
              retries=0,nonpreemptible=True,max_containers=1,scaledown_window=2,volumes={'/persist':volume})
def orchestrate(plan,batch):
    if not plan or len(plan)>30:raise ValueError('1–30 bounded experiments')
    bound=sum(TIMEOUT*(RATES[s['gpu']]+CPU_RATE) for s in plan)+3*18000*(.0000131+.00000222)
    if bound>150:raise ValueError('Batch maximum $150 resource-time reservation')
    waves=(len(plan)+3)//4
    if time.time()+waves*TIMEOUT+120>DEADLINE:raise ValueError('Batch cannot finish before deadline')
    if not batch.isdigit():raise ValueError('Numeric stable batch ID required')
    root=Path('/persist/experiments')/('night-'+batch);root.mkdir(parents=True,exist_ok=True)
    manifest={'batch':batch,'status':'running','resource_bound_usd':bound,'deadline_utc':'2026-09-18T06:00:00Z',
              'plan':plan,'results':[]}
    existing=root/'manifest.json'
    if existing.exists():
        manifest=json.loads(existing.read_text())
        if manifest['plan']!=plan:raise ValueError('Batch ID reused with a different plan')
        if manifest['status']=='complete':return manifest
    def save():
        (root/'manifest.json').write_text(json.dumps(manifest,indent=2));volume.commit()
    save();print('BATCH',batch,'RESERVED',bound,flush=True)
    # Four jobs at a time avoids oversubscribing the account and keeps costs bounded.
    for offset in range(0,len(plan),4):
        if offset+len(plan[offset:offset+4])<=len(manifest['results']):continue
        if manifest.get('active_offset')==offset and manifest.get('active_call_ids'):
            jobs=[modal.FunctionCall.from_id(id) for id in manifest['active_call_ids']]
        else:
            jobs=[]
            for spec in plan[offset:offset+4]:
                call=experiment.with_options(gpu=spec['gpu']).spawn(batch,spec)
                jobs.append(call)
            manifest['active_offset']=offset
            manifest['active_call_ids']=[j.object_id for j in jobs];save()
        for index,job in enumerate(jobs):
            if offset+index<len(manifest['results']):continue
            try:record=job.get()
            except Exception as exc:record={'status':'failed','error':str(exc),'cost_unknown':True}
            manifest['results'].append(record);save()
    manifest['status']='complete';manifest['active_call_ids']=[];save()
    return manifest

@app.local_entrypoint()
def main(plan: str, batch: str = ''):
    specs=json.loads(Path(plan).read_text())
    result=orchestrate.remote(specs,batch or str(time.time_ns()))
    out=ROOT/'runs'/('night-'+result['batch']);out.mkdir(parents=True,exist_ok=True)
    (out/'manifest.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
