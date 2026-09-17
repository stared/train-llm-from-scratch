"""Final ten-minute controls: simple English stories and popular Wikipedia openings."""
from pathlib import Path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import modal
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.14').pip_install_from_requirements('scripts/requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2'))
for file in ('scratch_model.py','train_scratch.py','sample_scratch.py','scratch_quality.py','scratch_worker.py'):
    image=image.add_local_file('scripts/' + file,'/work/scripts/'+file)

app=modal.App('workshop-scratch-final-controls')
@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=1,volumes={'/persist':volume})
def small():
    import sys
    sys.path.insert(0,'/work/scripts')
    from scratch_worker import execute
    return execute('10m',600,.000222,tag='tiny',data_name='tinystories-v1',volume=volume,batch_size=32,context_length=256,warmup_steps=20)
@app.function(image=image,gpu='H100',cpu=2,memory=16384,timeout=1000,retries=0,max_containers=2,volumes={'/persist':volume})
def larger(data_name,tag):
    import sys
    sys.path.insert(0,'/work/scripts')
    from scratch_worker import execute
    return execute('30m',600,.001097,tag=tag,data_name=data_name,volume=volume,eval_interval=60 if tag=='popular' else 300)
@app.local_entrypoint()
def main():
    jobs=[small.spawn(),larger.spawn('tinystories-v1','tiny'),larger.spawn('wiki-popular-v1','popular')]
    failures=[]
    for job in jobs:
        try:
            name,files=job.get()
            out=Path('runs')/name;out.mkdir(parents=True,exist_ok=True)
            for name,text in files.items():(out/name).write_text(text)
            print('SAVED',out,flush=True)
        except Exception as exc:failures.append(str(exc));print('FAILED',str(exc),flush=True)
    if failures:raise RuntimeError(failures)
