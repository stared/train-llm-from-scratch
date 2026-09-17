"""One bounded L4 at a time; ordinary trainer lives in rlvr_showcase.py."""
import json
from pathlib import Path
import time
import modal

app = modal.App('workshop-rlvr-showcase')
volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements('scripts/requirements.txt')
         .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'})
         .add_local_file('scripts/rlvr_showcase.py', '/work/scripts/rlvr_showcase.py')
         .add_local_file('scripts/rlvr_tasks.py', '/work/scripts/rlvr_tasks.py')
         .add_local_file('scripts/models.json', '/work/scripts/models.json'))


@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=1100,
              retries=0, max_containers=1, volumes={'/persist': volume})
def experiment(task, stage, model, max_seconds, steps, lr, seed, beta, dev_interval):
    import sys
    sys.path.insert(0, '/work/scripts')
    from rlvr_showcase import run
    started = time.monotonic()
    name = f'rlvr-{stage}-{task}-{time.time_ns()}'
    path = Path('/persist/runs') / name
    try:
        result = run(str(path), task, stage, model, max_seconds, steps, lr, seed, 'cuda', beta, dev_interval)
        result['remote_seconds'] = time.monotonic() - started
        result['estimated_compute_usd'] = result['remote_seconds'] * (.000222 + 2*.0000131 + 16*.00000222)
        for filename in ['rlvr_showcase.py', 'rlvr_tasks.py']:
            (path / ('executed_' + filename)).write_text((Path('/work/scripts') / filename).read_text())
        (path / 'execution.json').write_text(json.dumps(result, indent=2))
        return name, {p.name: p.read_text() for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(task: str = 'six_words', stage: str = 'train', model: str = 'qwen3.5-4b',
         max_seconds: int = 600, steps: int = 160, lr: float = 5e-5, seed: int = 42,
         beta: float = .01, dev_interval: int = 20):
    if task not in ('all', 'six_words', 'countdown', 'maze') or stage not in ('screen', 'train'):
        raise ValueError('Unknown task/stage')
    if not 60 <= max_seconds <= 600 or not 1 <= steps <= 400 or not 1e-6 <= lr <= 5e-4:
        raise ValueError('Invalid bounded settings')
    if not 0 <= beta <= .1 or dev_interval not in (0, 20, 40):
        raise ValueError('Invalid regularization/checkpoint settings')
    print('One L4, 16 GiB host RAM, 1100s hard timeout (~$0.31 requested compute ceiling); excludes startup/storage.', flush=True)
    for selected in (('six_words', 'countdown', 'maze') if task == 'all' else (task,)):
        name, files = experiment.remote(selected, stage, model, max_seconds, steps, lr, seed, beta, dev_interval)
        out = Path('runs') / name
        out.mkdir(parents=True, exist_ok=False)
        for filename, content in files.items():
            (out / filename).write_text(content)
        print('Saved:', out, flush=True)
        if stage == 'train':
            from training_report import render
            print('Open in your browser:', render(out))
