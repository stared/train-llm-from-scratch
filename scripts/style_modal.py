"""Bounded Modal jobs for the minute-scale workshop showcases."""
import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-style-showcase')
volume=modal.Volume.from_name('model-training-workshop',create_if_missing=True)
image=(modal.Image.debian_slim(python_version='3.14')
       .pip_install_from_requirements('scripts/requirements.txt')
       .env({'HF_HOME':'/persist/hf','TOKENIZERS_PARALLELISM':'false'})
       .add_local_file('scripts/style_workshop.py','/work/scripts/style_workshop.py')
       .add_local_file('scripts/style_data.py','/work/scripts/style_data.py')
       .add_local_file('scripts/models.json','/work/scripts/models.json')
       .add_local_file('datasets/pan_tadeusz_excerpt.txt','/work/datasets/pan_tadeusz_excerpt.txt'))
# Mount only versioned exercise datasets, never downloaded corpora or local backups.
for dataset in ('pan-tadeusz-qa-v1', 'chlopaki-bidirectional-v1', 'poetry-v1', 'wit-v1'):
    image = image.add_local_dir('datasets/' + dataset, '/work/datasets/' + dataset)


@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=1200,retries=0,
              max_containers=1,volumes={'/persist':volume})
def experiment(stage,style,model,languages,data_run,epochs,max_seconds,prompt,batch_tokens,resume_run,adapter_scale):
    import sys
    sys.path.insert(0,'/work/scripts')
    from style_workshop import make_data,train,chat,sample_saved
    started=time.monotonic()
    if stage in ('train','chat','sample'):
        source=Path('/work/datasets')/data_run
        if stage!='train' or not source.exists():
            source=Path('/persist/runs')/data_run
        manifest='dataset.json' if stage=='train' else 'style_result.json'
        style=json.loads((source/manifest).read_text())['style']
    name=f'style-{stage}-{style}-{time.time_ns()}'
    path=Path('/persist/runs')/name
    try:
        if stage=='data':
            result=make_data(str(path),style,model,languages,max_seconds,'cuda')
        elif stage=='train':
            resume_dir=str(Path('/persist/runs')/resume_run) if resume_run else None
            result=train(str(source),str(path),model,epochs,max_seconds,'cuda',batch_tokens=batch_tokens,resume_dir=resume_dir)
        elif stage=='chat':
            result=chat(str(source),str(path),prompt,'cuda')
        else:
            result=sample_saved(str(source),str(path),'cuda',adapter_scale)
        result['remote_seconds']=time.monotonic()-started
        result['estimated_compute_usd']=result['remote_seconds']*(.000222+2*.0000131+16*.00000222)
        # Preserve the executed source alongside outputs, even after later edits.
        (path/'executed_style_workshop.py').write_text(Path('/work/scripts/style_workshop.py').read_text())
        (path/'executed_style_data.py').write_text(Path('/work/scripts/style_data.py').read_text())
        (path/'execution.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        return name,{p.name:p.read_text() for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(stage:str='data',style:str='poetry',model:str='qwen3.5-4b',languages:str='both',
         data_run:str='',epochs:int=4,max_seconds:int=300,prompt:str='Why should I write tests?',batch_tokens:int=0,resume_run:str='',adapter_scale:float=1.0):
    if stage not in ('data','train','chat','sample') or style not in ('poetry','wit'):
        raise ValueError('Choose data/train/chat/sample and poetry/wit')
    if not 60<=max_seconds<=600 or not 1<=epochs<=20:
        raise ValueError('Choose 60–600 seconds and 1–20 epochs')
    if stage in ('train','chat','sample') and (not data_run or Path(data_run).name!=data_run):
        raise ValueError('Supply the printed data run name')
    if resume_run and (stage!='train' or Path(resume_run).name!=resume_run):
        raise ValueError('Resume requires train stage and a single run directory name')
    if not 0 < adapter_scale <= 1:
        raise ValueError('Adapter scale must be in (0, 1]')
    print('One L4; 1200s function timeout; ~ $0.34 requested compute ceiling plus startup/storage.',flush=True)
    name,files=experiment.remote(stage,style,model,languages,data_run,epochs,max_seconds,prompt,batch_tokens,resume_run,adapter_scale)
    out=Path('runs')/name
    out.mkdir(parents=True,exist_ok=False)
    for filename,contents in files.items():
        (out/filename).write_text(contents)
    print('Saved:',out)
    if stage == 'train':
        print('View results: pnpm dev', flush=True)
