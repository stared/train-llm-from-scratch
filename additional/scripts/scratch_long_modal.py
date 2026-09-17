"""Three concurrent, bounded scratch experiments. Ordinary trainer remains usable with uv."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-scratch-long')
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.14')
       .pip_install_from_requirements('scripts/requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2'))
for filename in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py'):
    image=image.add_local_file('scripts/' + filename,'/work/scripts/'+filename)


def execute(size,seconds,gpu_rate,tag='workshop',data_name='wiki-scratch-v1'):
    import sys
    import subprocess
    import traceback
    import torch
    sys.path.insert(0,'/work/scripts')
    from train_scratch import run
    from scratch_quality import evaluate_quality
    start=time.monotonic()
    rate=gpu_rate+2*.0000131+16*.00000222
    name=f'scratch-{tag}-{size}-{time.time_ns()}'
    out=Path('/persist/runs')/name
    source_info=json.loads((Path('/persist/datasets')/data_name/'tokens.json').read_text())
    budget_saved=False
    print('RUN',name,flush=True)
    def hook(model,tokenizer,stage,step,elapsed,path):
        nonlocal budget_saved
        spent=(time.monotonic()-start)*rate
        label=None
        if stage in ('before','selected'):label=stage
        elif spent>=1 and not budget_saved:
            label='budget_1usd';budget_saved=True
            torch.save(model.state_dict(),path/'budget_1usd.pt')
        if label:
            result=evaluate_quality(model,tokenizer,'cuda',path/f'quality_{label}.json',
                                    free_prompts=source_info.get('quality_prompts'),fact_probes=[] if data_name.startswith('wl-') else None)
            result.update(model=f'ScratchGPT-{size}',source=source_info.get('source_label','Polish Wikipedia20260901 original wikitext; random initialization; no fine-tuning'),
                          checkpoint=label,run=name,stage=stage,step=step,training_elapsed=elapsed,worker_elapsed=time.monotonic()-start,
                          estimated_compute_usd=(time.monotonic()-start)*rate)
            (path/f'quality_{label}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        # Flush artifacts every five minutes; unique per-run paths allow parallel writers.
        volume.commit()
    try:
        result=run('/persist/datasets/'+data_name,out,size,seconds,42,'cuda',64,
                   context_length=512,eval_interval=300,peak_lr={'10m':6e-4,'30m':6e-4,'100m':4e-4,'300m':3e-4}[size],
                   warmup_steps=100,checkpoint_hook=hook)
        subprocess.run([sys.executable,'/work/scripts/sample_scratch.py',str(out),'--device','cuda',
                        '--output',str(out/'reload_samples.json')],check=True,timeout=120)
        result['fresh_process_reload_matches']=json.loads((out/'reload_samples.json').read_text())==json.loads((out/'samples_selected.json').read_text())
        if not result['fresh_process_reload_matches']:raise RuntimeError('Fresh-process samples mismatch')
        result.update(remote_seconds=time.monotonic()-start,estimated_compute_usd=(time.monotonic()-start)*rate,
                      configured_hourly_usd=rate*3600,quality_checkpoint_policy='before, first5min checkpoint after $1 worker compute, development-selected')
        (out/'execution.json').write_text(json.dumps(result,indent=2))
    except Exception:
        out.mkdir(parents=True,exist_ok=True)
        (out/'failure.json').write_text(json.dumps(dict(traceback=traceback.format_exc(),seconds=time.monotonic()-start,
                                                       estimated_compute_usd=(time.monotonic()-start)*rate)))
        raise
    finally:
        if out.exists():
            for filename in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py'):
                (out/('executed_'+filename)).write_text((Path('/work/scripts')/filename).read_text())
        volume.commit()
    return name,{p.name:p.read_text() for p in out.iterdir() if p.suffix in ('.json','.py')}


@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=1,volumes={'/persist':volume})
def small(seconds):return execute('10m',seconds,.000222)


@app.function(image=image,gpu='A100-40GB',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=2,volumes={'/persist':volume})
def larger(size,seconds):return execute(size,seconds,.000583)


@app.function(image=image,gpu='H100',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=3,volumes={'/persist':volume})
def fast(size,seconds):return execute(size,seconds,.001097,tag='h100')


@app.local_entrypoint()
def main(seconds:int=600):
    if not 60<=seconds<=600:raise ValueError('Maximum10min per worker, no retries')
    jobs=[small.spawn(seconds),larger.spawn('30m',seconds),fast.spawn('30m',seconds),fast.spawn('100m',seconds),fast.spawn('300m',seconds)]
    failures=[]
    for job in jobs:
        try:
            name,files=job.get()
            out=Path('runs')/name;out.mkdir(parents=True,exist_ok=True)
            for name,text in files.items():(out/name).write_text(text)
            print('SAVED',out,flush=True)
        except Exception as exc:
            failures.append(str(exc));print('FAILED',str(exc),flush=True)
    if failures:raise RuntimeError(failures)
