"""Shared remote experiment body; no Modal app definitions at import time."""
import json
from pathlib import Path
import time

def execute(size,seconds,gpu_rate,tag='workshop',data_name='wiki-scratch-v1',volume=None,batch_size=64,context_length=512,warmup_steps=100,eval_interval=300):
    import sys
    import subprocess
    import traceback
    import torch
    sys.path.insert(0,'/work')
    from train_scratch import run
    from scratch_quality import evaluate_quality,evaluate_fixed_pool
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
        if stage in ('before','final','selected'):label=stage
        elif spent>=1 and not budget_saved:
            label='budget_1usd';budget_saved=True
            torch.save(model.state_dict(),path/'budget_1usd.pt')
        if label:
            if label=='selected' and data_name in ('wiki-leads-v1','wiki-popular-v1'):
                common=evaluate_fixed_pool(model,'cuda','/persist/datasets/wiki-scratch-v1')
                (path/'common_wiki_eval.json').write_text(json.dumps(common,indent=2))
            result=evaluate_quality(model,tokenizer,'cuda',path/f'quality_{label}.json',
                                    free_prompts=source_info.get('quality_prompts'),fact_probes=source_info.get('quality_fact_probes',[] if data_name.startswith('wl-') else None))
            result.update(model=f'ScratchGPT-{size}',source=source_info.get('source_label','Polish Wikipedia20260901 original wikitext; random initialization; no fine-tuning'),
                          checkpoint=label,run=name,stage=stage,step=step,training_elapsed=elapsed,worker_elapsed=time.monotonic()-start,
                          estimated_compute_usd=(time.monotonic()-start)*rate)
            (path/f'quality_{label}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        # Flush artifacts every five minutes; unique per-run paths allow parallel writers.
        volume.commit()
    try:
        result=run('/persist/datasets/'+data_name,out,size,seconds,42,'cuda',batch_size,
                   context_length=context_length,eval_interval=eval_interval,peak_lr={'10m':6e-4,'30m':6e-4,'100m':4e-4,'300m':3e-4}[size],
                   warmup_steps=warmup_steps,checkpoint_hook=hook)
        subprocess.run([sys.executable,'/work/sample_scratch.py',str(out),'--device','cuda',
                        '--output',str(out/'reload_samples.json')],check=True,timeout=120)
        result['fresh_process_reload_matches']=json.loads((out/'reload_samples.json').read_text())==json.loads((out/'samples_selected.json').read_text())
        if not result['fresh_process_reload_matches']:raise RuntimeError('Fresh-process samples mismatch')
        result.update(remote_seconds=time.monotonic()-start,estimated_compute_usd=(time.monotonic()-start)*rate,
                      configured_hourly_usd=rate*3600,quality_checkpoint_policy='before, first periodic checkpoint after $1 worker compute, final, development-selected')
        (out/'execution.json').write_text(json.dumps(result,indent=2))
    except Exception:
        out.mkdir(parents=True,exist_ok=True)
        (out/'failure.json').write_text(json.dumps(dict(traceback=traceback.format_exc(),seconds=time.monotonic()-start,
                                                       estimated_compute_usd=(time.monotonic()-start)*rate)))
        raise
    finally:
        if out.exists():
            for filename in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py','scratch_worker.py'):
                (out/('executed_'+filename)).write_text((Path('/work')/filename).read_text())
        volume.commit()
    return name,{p.name:p.read_text() for p in out.iterdir() if p.suffix in ('.json','.py')}
