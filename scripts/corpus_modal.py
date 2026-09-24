"""One bounded L4 run of the full-book training script."""
import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-full-book')
volume=modal.Volume.from_name('model-training-workshop',create_if_missing=True)
image=(modal.Image.debian_slim(python_version='3.14')
       .pip_install_from_requirements('scripts/requirements.txt')
       .env({'HF_HOME':'/persist/hf','TOKENIZERS_PARALLELISM':'false'})
       .add_local_file('scripts/corpus_workshop.py','/work/scripts/corpus_workshop.py')
       .add_local_file('scripts/corpus_chunks.py','/work/scripts/corpus_chunks.py')
       .add_local_file('scripts/style_workshop.py','/work/scripts/style_workshop.py')
       .add_local_file('scripts/style_data.py','/work/scripts/style_data.py')
       .add_local_file('scripts/models.json','/work/scripts/models.json')
       .add_local_dir('datasets/pan-tadeusz-full','/work/corpus'))


@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1200,retries=0,
              max_containers=1,volumes={'/persist':volume})
def experiment(model,epochs,max_seconds,target_tokens,batch_size,line_aligned):
    import sys
    sys.path.insert(0,'/work/scripts')
    from corpus_workshop import run
    started=time.monotonic();name=f'pan-tadeusz-{time.time_ns()}'
    path=Path('/persist/runs')/name
    try:
        result=run('/work/corpus',str(path),model,epochs,max_seconds,'cuda',target_tokens,batch_size,line_aligned)
        result['remote_seconds']=time.monotonic()-started
        result['estimated_compute_usd']=result['remote_seconds']*(.000222+2*.0000131+16*.00000222)
        (path/'execution.json').write_text(json.dumps(result,ensure_ascii=False,indent=2), encoding='utf-8', newline='\n')
        for filename in ('corpus_workshop.py','corpus_chunks.py','style_workshop.py','models.json'):
            (path/('executed_'+filename)).write_bytes((Path('/work/scripts')/filename).read_bytes())
        return name,{p.name:p.read_text(encoding='utf-8') for p in path.iterdir() if p.is_file()}
    finally:volume.commit()


@app.local_entrypoint()
def main(model:str='lfm2.5-2.6b',epochs:int=1,max_seconds:int=600,
         target_tokens:int=256,batch_size:int=2,line_aligned:bool=False):
    if not 1<=epochs<=3 or not 60<=max_seconds<=600:raise ValueError('Invalid run budget')
    if target_tokens not in (256,1024,2048,4096) or batch_size not in (1,2):
        raise ValueError('Invalid chunk/batch size')
    name,files=experiment.remote(model,epochs,max_seconds,target_tokens,batch_size,line_aligned)
    path=Path('runs')/name;path.mkdir(parents=True,exist_ok=False)
    for filename,contents in files.items():(path/filename).write_text(contents, encoding='utf-8', newline='\n')
    print('Saved:',path)
