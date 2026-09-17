"""CPU-prepared wikitext stays on a Modal volume; one bounded L4 at a time."""
import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-scratch-wikitext')
volume=modal.Volume.from_name('model-training-workshop',create_if_missing=True)
image=(modal.Image.debian_slim(python_version='3.12')
    .pip_install_from_requirements('scripts/requirements.txt')
    .pip_install('numpy==2.5.3','tokenizers==0.23.2')
    .add_local_file('scripts/scratch_model.py','/work/scripts/scratch_model.py')
    .add_local_file('scripts/train_scratch.py','/work/scripts/train_scratch.py')
    .add_local_file('scripts/sample_scratch.py','/work/scripts/sample_scratch.py'))


@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1000,retries=0,
              max_containers=1,volumes={'/persist':volume})
def experiment(size,max_seconds,batch_size):
    import subprocess
    import sys
    sys.path.insert(0,'/work/scripts')
    from train_scratch import run
    start=time.monotonic()
    name=f'scratch-wikitext-{size}-{time.time_ns()}'
    out=Path('/persist/runs')/name
    print('Run',name,flush=True)
    try:
        result=run('/persist/datasets/wiki-scratch-v1',str(out),size,max_seconds,42,'cuda',batch_size)
        subprocess.run([sys.executable,'/work/scripts/sample_scratch.py',str(out),
                        '--device','cuda','--output',str(out/'reload_samples.json')],check=True,timeout=120)
        matches=json.loads((out/'reload_samples.json').read_text())==json.loads((out/'samples_selected.json').read_text())
        if not matches:raise RuntimeError('Fresh-process generation differs')
        result['fresh_process_reload_matches']=matches
        result['remote_seconds']=time.monotonic()-start
        result['estimated_compute_usd']=result['remote_seconds']*(.000222+2*.0000131+16*.00000222)
        for file in ('scratch_model.py','train_scratch.py','sample_scratch.py'):
            (out/('executed_'+file)).write_text((Path('/work/scripts')/file).read_text())
        (out/'execution.json').write_text(json.dumps(result,indent=2))
        return name,{p.name:p.read_text() for p in out.iterdir() if p.suffix in ('.json','.py')}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(size:str='compare',max_seconds:int=300,batch_size:int=32):
    if size not in ('compare','10m','30m') or not 60<=max_seconds<=600:
        raise ValueError('Invalid size/time budget')
    print('Sequential L4 runs;1000s hard timeout each;no configured retries.',flush=True)
    for selected in (('10m','30m') if size=='compare' else (size,)):
        name,files=experiment.remote(selected,max_seconds,batch_size)
        out=Path('runs')/name;out.mkdir(parents=True,exist_ok=False)
        for filename,text in files.items():(out/filename).write_text(text)
        print('Saved',out,flush=True)
