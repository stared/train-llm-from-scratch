"""Bounded Modal transport for the ordinary uv-run prawko.py script."""
import json
from pathlib import Path
import time
import modal

app = modal.App('workshop-prawko')
volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.12')
    .pip_install_from_requirements('requirements.txt')
    .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'})
    .add_local_file('prawko.py', '/work/prawko.py')
    .add_local_file('models.json', '/work/models.json')
    .add_local_dir('datasets/prawko-v2', '/work/datasets/prawko-v2'))


@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=1050,
              retries=0, max_containers=1, volumes={'/persist': volume})
def experiment(method, model, max_seconds, epochs, lr, seed):
    import sys
    sys.path.insert(0, '/work')
    from prawko import run
    started = time.monotonic()
    name = f'prawko-{method}-{time.time_ns()}'
    path = Path('/persist/runs') / name
    try:
        result = run(str(path), method, model, max_seconds, epochs, lr, seed, 'cuda')
        result['remote_seconds'] = time.monotonic() - started
        result['estimated_compute_usd'] = result['remote_seconds'] * (.000222 + 2*.0000131 + 16*.00000222)
        (path / 'executed_prawko.py').write_text(Path('/work/prawko.py').read_text())
        (path / 'execution.json').write_text(json.dumps(result, indent=2))
        return name, {p.name: p.read_text() for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(method: str = 'screen', model: str = 'qwen3.5-0.8b', max_seconds: int = 180,
         epochs: int = 5, lr: float = 5e-5, seed: int = 42):
    if method not in ('screen','sft','rlvr','compare'):
        raise ValueError('Unknown method')
    if not 60 <= max_seconds <= 720 or not 1 <= epochs <= 40 or not 1e-6 <= lr <= 5e-4:
        raise ValueError('Use 60–720 seconds, 1–40 epochs, learning rate 1e-6–5e-4')
    print('One L4; each worker hard timeout 1050s (~$0.30 requested compute ceiling), excluding startup/storage.', flush=True)
    for selected in (('sft','rlvr') if method=='compare' else (method,)):
        name, files = experiment.remote(selected, model, max_seconds, epochs, lr, seed)
        out = Path('runs') / name
        out.mkdir(parents=True, exist_ok=False)
        for filename, content in files.items():
            (out / filename).write_text(content)
        print('Saved', out, flush=True)
