"""Ten-minute literary-corpus comparisons; no Wikipedia factual-score claims."""
from pathlib import Path
import modal
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.12').pip_install_from_requirements('requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2'))
for file in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py','scratch_worker.py'):
    image=image.add_local_file(file,'/work/'+file)

app=modal.App('workshop-scratch-literature')
@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=1,volumes={'/persist':volume})
def small():
    import sys
    sys.path.insert(0,'/work')
    from scratch_worker import execute
    return execute('10m',600,.000222,tag='wl',data_name='wl-scratch-v1',volume=volume)
@app.function(image=image,gpu='H100',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=2,volumes={'/persist':volume})
def larger(size):
    import sys
    sys.path.insert(0,'/work')
    from scratch_worker import execute
    return execute(size,600,.001097,tag='wl',data_name='wl-scratch-v1',volume=volume)
@app.local_entrypoint()
def main():
    jobs=[small.spawn(),larger.spawn('30m'),larger.spawn('100m')]
    failures=[]
    for job in jobs:
        try:
            name,files=job.get()
            out=Path('runs')/name;out.mkdir(parents=True,exist_ok=True)
            for name,text in files.items():(out/name).write_text(text)
            print('SAVED',out,flush=True)
        except Exception as exc:failures.append(str(exc));print('FAILED',str(exc),flush=True)
    if failures:raise RuntimeError(failures)
