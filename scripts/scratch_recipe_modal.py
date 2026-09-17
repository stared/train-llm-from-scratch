"""Run one tested workshop recipe; no experiment matrix is launched implicitly."""
from pathlib import Path
import modal

RECIPES = {
    'wiki-cheap': ('10m', 'wiki-scratch-v1', 'L4', 32, 256, 20),
    'wiki': ('30m', 'wiki-scratch-v1', 'H100', 64, 512, 100),
    'literature': ('30m', 'wl-scratch-v1', 'H100', 64, 512, 100),
    'stories-cheap': ('10m', 'tinystories-v1', 'L4', 32, 256, 20),
    'stories': ('30m', 'tinystories-v1', 'H100', 64, 512, 100),
    'popular-wiki': ('30m', 'wiki-popular-v1', 'H100', 64, 512, 100),
}
app = modal.App('workshop-scratch-single-recipe')
volume = modal.Volume.from_name('model-training-workshop')
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements('scripts/requirements.txt')
         .pip_install('numpy==2.5.3', 'tokenizers==0.23.2'))
for name in ('scratch_model.py', 'train_scratch.py', 'sample_scratch.py',
             'scratch_quality.py', 'scratch_worker.py'):
    image = image.add_local_file('scripts/' + name, '/work/scripts/' + name)

def execute_recipe(recipe, seconds):
    import sys
    sys.path.insert(0, '/work/scripts')
    from scratch_worker import execute
    size, data, gpu, batch, context, warmup = RECIPES[recipe]
    return execute(size, seconds, .000222 if gpu == 'L4' else .001097,
                   tag=recipe, data_name=data, volume=volume,
                   batch_size=batch, context_length=context, warmup_steps=warmup,
                   eval_interval=60 if recipe == 'popular-wiki' else 300)

@app.function(image=image, gpu='L4', cpu=2, memory=16384, timeout=1000,
              retries=0, max_containers=1, volumes={'/persist': volume})
def cheap(recipe, seconds):
    return execute_recipe(recipe, seconds)

@app.function(image=image, gpu='H100', cpu=2, memory=16384, timeout=1000,
              retries=0, max_containers=1, volumes={'/persist': volume})
def fast(recipe, seconds):
    return execute_recipe(recipe, seconds)

@app.local_entrypoint()
def main(recipe: str = 'stories-cheap', max_seconds: int = 600):
    if recipe not in RECIPES:
        raise ValueError(f'Choose one of: {", ".join(RECIPES)}')
    if not 60 <= max_seconds <= 600:
        raise ValueError('Workshop training must be between 60 and 600 seconds')
    worker = cheap if RECIPES[recipe][2] == 'L4' else fast
    name, files = worker.remote(recipe, max_seconds)
    out = Path(__file__).resolve().parents[1] / 'runs' / name
    out.mkdir(parents=True, exist_ok=True)
    for filename, content in files.items():
        (out / filename).write_text(content)
    print('Saved', out)
    from training_report import render
    print('Open in your browser:', render(out))
