"""Run one tested workshop recipe; no experiment matrix is launched implicitly."""
from pathlib import Path
import modal

RECIPES = {
    'wiki-cheap': ('10m', 'wiki-scratch-v1', 'L4', 32, 256, 20),
    'wiki': ('30m', 'wiki-scratch-v1', 'H100', 64, 512, 100),
    'wiki-100m': ('100m', 'wiki-scratch-v1', 'H100', 64, 512, 100),
    'wolne-lektury': ('30m', 'wl-scratch-v1', 'H100', 64, 512, 100),
    'sejm': ('30m', 'sejm-scratch-v1', 'H100', 64, 512, 100),
    'stories-cheap': ('10m', 'tinystories-v1', 'L4', 32, 256, 20),
    'stories': ('30m', 'tinystories-v1', 'H100', 64, 512, 100),
    'popular-wiki': ('30m', 'wiki-popular-v1', 'H100', 64, 512, 100),
}
GPU_RATES = {'L4': .000222, 'A10': .000306, 'L40S': .000542, 'H100': .001097,
             'H200': .001261, 'B200': .001736}  # modal.com/pricing, checked 2026-09-18.

app = modal.App('workshop-scratch-single-recipe')
volume = modal.Volume.from_name('model-training-workshop')
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements('scripts/requirements.txt')
         .pip_install('numpy==2.5.3', 'tokenizers==0.23.2')
         .env({'TORCHINDUCTOR_COMPILE_THREADS':'2'}))
for name in ('scratch_model.py', 'train_scratch.py', 'sample_scratch.py',
             'scratch_quality.py', 'scratch_worker.py', 'training_progress.py'):
    image = image.add_local_file('scripts/' + name, '/work/scripts/' + name)

def execute_recipe(recipe, seconds, gpu_override='', batch_override=0, compile_training=False, progress_queue=None):
    import sys
    sys.path.insert(0, '/work/scripts')
    from scratch_worker import execute
    from training_progress import reporter
    size, data, gpu, batch, context, warmup = RECIPES[recipe]
    gpu = gpu_override or gpu
    batch = batch_override or batch
    return execute(size, seconds, GPU_RATES[gpu],
                   tag=recipe, data_name=data, volume=volume,
                   batch_size=batch, context_length=context, warmup_steps=warmup,
                   eval_interval=60, progress=reporter(progress_queue),compile_training=compile_training)

@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=1000,
              retries=0, max_containers=1, volumes={'/persist': volume})
def cheap(recipe, seconds, gpu_override='', batch_override=0, compile_training=False, progress_queue=None):
    return execute_recipe(recipe, seconds, gpu_override, batch_override, compile_training, progress_queue)

@app.function(image=image, gpu='H100', cpu=2, memory=16384, timeout=1000,
              retries=0, max_containers=1, volumes={'/persist': volume})
def fast(recipe, seconds, gpu_override='', batch_override=0, compile_training=False, progress_queue=None):
    return execute_recipe(recipe, seconds, gpu_override, batch_override, compile_training, progress_queue)

@app.local_entrypoint()
def main(recipe: str = 'wolne-lektury', max_seconds: int = 600, gpu: str = '', batch_size: int = 0, compile_training: bool = False):
    if recipe not in RECIPES:
        raise ValueError(f'Choose one of: {", ".join(RECIPES)}')
    if not 60 <= max_seconds <= 600:
        raise ValueError('Workshop training must be between 60 and 600 seconds')
    gpu = gpu or RECIPES[recipe][2]
    if gpu not in GPU_RATES or batch_size not in (0,8,16,32,64):
        raise ValueError('GPU: '+', '.join(GPU_RATES)+'; batch size: 8, 16, 32, 64')
    batch_size = batch_size or min(RECIPES[recipe][3], 64 if gpu in ('H100','H200','B200') else 32)
    worker = (cheap if gpu == 'L4' else fast).with_options(gpu=gpu)
    print(f'{gpu}, batch {batch_size}; training budget {max_seconds}s', flush=True)
    from training_progress import run_live
    name, files = run_live(worker, 'pretrain', recipe, max_seconds, gpu, batch_size, compile_training)
    out = Path(__file__).resolve().parents[1] / 'runs' / name
    out.mkdir(parents=True, exist_ok=True)
    for filename, content in files.items():
        (out / filename).write_text(content, encoding='utf-8', newline='\n')
    print('Saved', out)
    print('View results: pnpm dev', flush=True)
