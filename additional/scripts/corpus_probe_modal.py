"""One bounded inference-only Modal job for full-book chat probes."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-corpus-probe')
volume=modal.Volume.from_name('model-training-workshop')
probe_image=(modal.Image.debian_slim(python_version='3.14')
    .pip_install_from_requirements('scripts/requirements.txt')
    .env({'HF_HOME':'/persist/hf','TOKENIZERS_PARALLELISM':'false'})
    .add_local_file('scripts/models.json','/work/scripts/models.json')
    .add_local_file('scripts/style_workshop.py','/work/scripts/style_workshop.py')
    .add_local_file('scripts/style_data.py','/work/scripts/style_data.py')
    .add_local_file('additional/scripts/corpus_probe.py','/work/additional/scripts/corpus_probe.py'))

@app.function(image=probe_image,gpu='L4',cpu=2,memory=16384,timeout=300,retries=0,
              max_containers=1,volumes={'/persist':volume})
def experiment(adapter_run,long_output_tokens):
    import sys
    sys.path.insert(0,'/work/scripts')
    from corpus_probe import probe
    started=time.monotonic()
    name=f'corpus-probe-{time.time_ns()}'
    path=Path('/persist/runs')/name
    try:
        result=probe(str(Path('/persist/runs')/adapter_run),str(path),long_output_tokens=long_output_tokens)
        result['remote_seconds']=time.monotonic()-started
        result['estimated_compute_usd']=result['remote_seconds']*(.000222+2*.0000131+16*.00000222)
        (path/'probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
        (path/'executed_corpus_probe.py').write_text(Path('/work/additional/scripts/corpus_probe.py').read_text())
        return name,{p.name:p.read_text() for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()

@app.local_entrypoint()
def main(adapter_run:str='pan-tadeusz-1788776622044561619',long_output_tokens:int=0):
    if Path(adapter_run).name!=adapter_run:
        raise ValueError('Expected one saved run name')
    if long_output_tokens not in (0,1024):
        raise ValueError('Long-output diagnostic must be 0 or 1024')
    name,files=experiment.remote(adapter_run,long_output_tokens)
    out=Path('runs')/name
    out.mkdir(parents=True,exist_ok=False)
    for filename,content in files.items():
        (out/filename).write_text(content)
    print('Saved:',out)
