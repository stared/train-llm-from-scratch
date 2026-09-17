"""Detached Polish-only experiment controller. All completion work is remote."""
import json
from pathlib import Path
import time
import modal

app=modal.App('polish-scratch-budget-experiments')
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.12')
       .pip_install_from_requirements('scripts/requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2'))
for filename in ('scratch_model.py','train_scratch.py','sample_scratch.py',
                 'scratch_quality.py','scratch_long_report.py','verify_pretraining.py'):
    image=image.add_local_file('scripts/' + filename,'/work/scripts/'+filename)

# Resource requests and limits coincide; no unbounded CPU/RAM autoscaling.
RATE=.001097+2*.0000131+16*.00000222
TIMEOUT=8500
DOLLAR_PLAN=[
    ('wiki-100-uniform','100m','wiki-scratch-v1','uniform'),
    ('wiki-300-uniform','300m','wiki-scratch-v1','uniform'),
    ('wiki-100-mixed','100m','wiki-scratch-v1','mixed'),
    ('wl-100','100m','wl-scratch-v1','uniform'),
]
PLAN=[
    ('wiki-100-uniform','100m','wiki-scratch-v1','uniform'),
    ('wiki-100-mixed','100m','wiki-scratch-v1','mixed'),
    ('wiki-300-uniform','300m','wiki-scratch-v1','uniform'),
    ('wiki-300-mixed','300m','wiki-scratch-v1','mixed'),
    ('wiki-100-openings','100m','wiki-scratch-v1','openings'),
    ('wl-30','30m','wl-scratch-v1','uniform'),
    ('wl-100','100m','wl-scratch-v1','uniform'),
    ('wl-300','300m','wl-scratch-v1','uniform'),
]

@app.function(image=image,gpu='H100',cpu=(2,2),memory=(16384,16384),
              timeout=TIMEOUT,retries=0,max_containers=4,scaledown_window=2,
              volumes={'/persist':volume})
def train_one(batch_id,recipe,seconds):
    import sys,subprocess,traceback
    sys.path.insert(0,'/work/scripts')
    from train_scratch import run
    from scratch_quality import evaluate_quality
    started=time.monotonic();tag,size,data,mode=recipe
    name=f'scratch-{batch_id}-{tag}';out=Path('/persist/runs')/name
    meta=json.loads((Path('/persist/datasets')/data/'tokens.json').read_text())
    source=meta.get('source_label',data)
    if mode!='uniform':source+=f'; {mode} sampling with filtered Wikipedia lead substrings'
    try:
        def hook(model,tokenizer,stage,step,elapsed,path):
            if stage in ('before','final','selected'):
                q=evaluate_quality(model,tokenizer,'cuda',path/f'quality_{stage}.json',
                    free_prompts=meta.get('quality_prompts'),
                    fact_probes=[] if data.startswith('wl-') else None)
                q.update(model=f'ScratchGPT-{size}',source=source,
                         checkpoint=stage,run=name,step=step,training_elapsed=elapsed)
                (path/f'quality_{stage}.json').write_text(json.dumps(q,ensure_ascii=False,indent=2))
            volume.commit()
        result=run('/persist/datasets/'+data,out,size,seconds,42,'cuda',64,
            context_length=512,eval_interval=600 if seconds>600 else 300,peak_lr={'30m':6e-4,'100m':4e-4,'300m':3e-4}[size],
            warmup_steps=100,checkpoint_hook=hook,research_limit_seconds=8400,
            sampling_mode=mode,mixture_dir='/persist/datasets/wiki-leads-v1' if mode!='uniform' else None)
        subprocess.run([sys.executable,'/work/scripts/sample_scratch.py',str(out),'--device','cuda',
                        '--output',str(out/'reload_samples.json')],check=True,timeout=180)
        result['fresh_process_reload_matches']=json.loads((out/'reload_samples.json').read_text())==json.loads((out/'samples_selected.json').read_text())
        if not result['fresh_process_reload_matches']:raise RuntimeError('Reload mismatch')
        result.update(source=source,remote_seconds=time.monotonic()-started,estimated_compute_usd=(time.monotonic()-started)*RATE,
                      configured_hourly_usd=3600*RATE,recipe=tag)
        (out/'execution.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        return dict(run=name,status='complete',estimated_compute_usd=result['estimated_compute_usd'])
    except Exception:
        out.mkdir(parents=True,exist_ok=True)
        error=dict(run=name,status='failed',traceback=traceback.format_exc(),estimated_compute_usd=(time.monotonic()-started)*RATE)
        (out/'failure.json').write_text(json.dumps(error,indent=2))
        return error
    finally:
        for filename in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py'):
            if out.exists():(out/('executed_'+filename)).write_text((Path('/work/scripts')/filename).read_text())
        volume.commit()

@app.function(image=image,cpu=(1,1),memory=(2048,2048),timeout=24000,retries=0,
              max_containers=1,scaledown_window=2,volumes={'/persist':volume})
def orchestrate(seconds:int=600, dollar_runs:bool=False):
    import sys,traceback
    sys.path.insert(0,'/work/scripts')
    from scratch_long_report import render
    from verify_pretraining import audit
    if not 60<=seconds<=8000:raise ValueError('Maximum 8000 training seconds')
    if dollar_runs and seconds!=8000:raise ValueError('Dollar-scale profile uses 8000 seconds of training')
    plan=DOLLAR_PLAN if dollar_runs else PLAN
    assert RATE*TIMEOUT<10
    assert len(plan)*RATE*TIMEOUT+24000*(.0000131+2*.00000222)<100
    batch_id=('polish-dollar-' if dollar_runs else 'polish-')+str(time.time_ns());root=Path('/persist/experiments')/batch_id
    root.mkdir(parents=True)
    manifest=dict(batch_id=batch_id,status='running',training_seconds_per_run=seconds,
                  per_run_resource_bound_usd=RATE*TIMEOUT,
                  batch_resource_bound_usd=len(plan)*RATE*TIMEOUT+24000*(.0000131+2*.00000222),
                  plan=plan,results=[],notes='Polish corpora only; no retries. Resource-time bounds exclude build/storage. Full completion and reporting run remotely.')
    def save():
        (root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));volume.commit()
    save();print('REMOTE_BATCH',batch_id,flush=True)
    jobs=[train_one.spawn(batch_id,recipe,seconds) for recipe in plan]
    manifest['function_call_ids']=[job.object_id for job in jobs];save()
    for recipe,job in zip(plan,jobs):
        try:result=job.get()
        except Exception:result=dict(recipe=recipe[0],status='failed',traceback=traceback.format_exc())
        manifest['results'].append(result);save()
    volume.reload()
    completed=[Path('/persist/runs')/r['run'] for r in manifest['results'] if r['status']=='complete']
    try:
        for path in completed:
            if not audit(path,require_weights=True)['passed']:raise RuntimeError(f'Artifact audit failed: {path.name}')
        if completed:render(completed,root)
        manifest['status']='complete' if len(completed)==len(plan) else 'complete_with_failures'
    except Exception:
        manifest['status']='report_failed';manifest['report_error']=traceback.format_exc()
    save();print(json.dumps(manifest,ensure_ascii=False),flush=True)
    return manifest
