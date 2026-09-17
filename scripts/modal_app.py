"""Thin, bounded Modal wrapper around the ordinary Python implementation."""
import json
from pathlib import Path
import time
import modal

app = modal.App('model-training-workshop')
volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.12')
         .pip_install_from_requirements('scripts/requirements.txt')
         .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'})
         .add_local_file('scripts/finetune.py', '/work/scripts/finetune.py')
         .add_local_file('scripts/examples.py', '/work/scripts/examples.py')
         .add_local_file('config/models.json', '/work/config/models.json'))


@app.function(image=image, gpu='L4', cpu=2, memory=8192, timeout=600,
              retries=0, max_containers=1, volumes={'/persist': volume})
def experiment(model, task, steps, eval_size, max_seconds):
    started = time.monotonic()
    import sys
    sys.path.insert(0, '/work/scripts')
    from finetune import run
    name = f'{model}-{task}-{time.time_ns()}'
    path = Path('/persist/runs') / name
    try:
        result = run(model, task, steps, eval_size, str(path), 'cuda', max_seconds)
        # Formula includes requested CPU and RAM, but is not a billing receipt.
        result['remote_seconds'] = time.monotonic() - started
        result['estimated_compute_usd'] = result['remote_seconds'] * (.000222 + 2*.0000131 + 8*.00000222)
        (path / 'result.json').write_text(json.dumps(result, indent=2))
        files = {p.name: p.read_text() for p in path.iterdir() if p.is_file()}
        return name, files
    finally:
        volume.commit()


@app.local_entrypoint()
def main(model: str = 'qwen3-0.6b', task: str = 'routing', steps: int = 40,
         eval_size: int = 8, max_seconds: int = 180):
    from finetune import MODELS
    from examples import TASKS
    if model not in MODELS or task not in TASKS:
        raise ValueError('Choose a model from models.json and routing/extraction/polish')
    if not 1 <= steps <= 200 or not 1 <= eval_size <= 64 or not 1 <= max_seconds <= 400:
        raise ValueError('Use <=200 steps, <=64 evaluation examples and <=400 training seconds')
    print('One L4; no retries; 600s remote timeout. Approximate requested compute ceiling: $0.16 plus startup/build/storage.')
    name, files = experiment.remote(model, task, steps, eval_size, max_seconds)
    out = Path('runs') / name
    out.mkdir(parents=True, exist_ok=False)
    for filename, data in files.items():
        (out / filename).write_text(data)
    print(f'Results: {out}; adapter: Modal volume model-training-workshop /runs/{name}/adapter')
