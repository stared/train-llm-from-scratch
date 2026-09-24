"""Bounded Modal transport for the ordinary uv-run prawko.py script."""
import json
from pathlib import Path
import time
import modal

GPU_RATES = {'L4': .000222, 'A10': .000306, 'L40S': .000542, 'H100': .001097}

app = modal.App('workshop-prawko')
volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
image = (modal.Image.debian_slim(python_version='3.14')
    .pip_install_from_requirements('scripts/requirements.txt')
    .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'})
    .add_local_file('scripts/prawko.py', '/work/scripts/prawko.py')
    .add_local_file('scripts/training_progress.py', '/work/scripts/training_progress.py')
    .add_local_file('scripts/models.json', '/work/scripts/models.json')
    .add_local_dir('datasets/prawko-v2', '/work/datasets/prawko-v2'))


@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=1050,
              retries=0, max_containers=1, volumes={'/persist': volume})
def experiment(method, model, max_seconds, epochs, lr, seed, gpu='L4', batch_size=4, dataset='small', progress_queue=None):
    import sys
    sys.path.insert(0, '/work/scripts')
    from prawko import run
    from training_progress import reporter
    started = time.monotonic()
    name = f'prawko-{method}-{time.time_ns()}'
    path = Path('/persist/runs') / name
    try:
        result = run(str(path), method, model, max_seconds, epochs, lr, seed, 'cuda', progress=reporter(progress_queue),
                     train_batch_size=batch_size,eval_batch_size=2 if model=='qwen3.5-4b' else 8,
                     dataset_path='/work/datasets/prawko-v2/'+('extended.json' if dataset=='expanded' else 'data.json'))
        result['remote_seconds'] = time.monotonic() - started
        result['estimated_compute_usd'] = result['remote_seconds'] * (GPU_RATES[gpu] + 2*.0000131 + 16*.00000222)
        (path / 'executed_prawko.py').write_text(Path('/work/scripts/prawko.py').read_text(encoding='utf-8'), encoding='utf-8', newline='\n')
        (path / 'execution.json').write_text(json.dumps(result, indent=2), encoding='utf-8', newline='\n')
        return name, {p.name: p.read_text(encoding='utf-8') for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(method: str = 'screen', model: str = 'qwen3.5-0.8b', max_seconds: int = 0,
         epochs: int = 0, lr: float = 0., seed: int = 42, gpu: str = 'L4', batch_size: int = 0, dataset: str = 'small'):
    if dataset not in ('small','expanded'):
        raise ValueError('Dataset: small (100 training questions) or expanded (289)')
    max_seconds=max_seconds or (600 if dataset=='expanded' else 180)
    epochs=epochs or (40 if dataset=='expanded' else 10)
    lr=lr or (2e-5 if dataset=='expanded' else 5e-5)
    if method not in ('screen','sft','rlvr','compare'):
        raise ValueError('Unknown method')
    if not 60 <= max_seconds <= 720 or not 1 <= epochs <= 40 or not 1e-6 <= lr <= 5e-4:
        raise ValueError('Use 60–720 seconds, 1–40 epochs, learning rate 1e-6–5e-4')
    if gpu not in GPU_RATES or batch_size not in (0,1,2,4,8):
        raise ValueError('GPU: L4, A10, L40S, H100; batch size: 1, 2, 4, 8')
    batch_size = batch_size or (2 if model=='qwen3.5-4b' and gpu in ('L4','A10') else 4)
    ceiling=1050*(GPU_RATES[gpu]+2*.0000131+16*.00000222)
    print(f'One {gpu}, batch {batch_size}; timeout 1050s (~$'+'{:.2f}'.format(ceiling)+' at requested resource rates), excluding startup/storage.', flush=True)
    worker=experiment.with_options(gpu=gpu)
    for selected in (('sft','rlvr') if method=='compare' else (method,)):
        from training_progress import run_live
        name, files = run_live(worker, 'sft' if selected in ('sft','screen') else 'exam-rlvr', selected, model, max_seconds, epochs, lr, seed, gpu, batch_size, dataset)
        out = Path('runs') / name
        out.mkdir(parents=True, exist_ok=False)
        for filename, content in files.items():
            (out / filename).write_text(content, encoding='utf-8', newline='\n')
        print('Saved', out, flush=True)
        print('View results: pnpm dev', flush=True)
