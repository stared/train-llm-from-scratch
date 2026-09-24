"""Run the ordinary RLVR example using the existing SFT volume and image."""
import json
from pathlib import Path
import time
import modal

volume = modal.Volume.from_name('model-training-workshop', create_if_missing=True)
# Repeat the tiny image declaration so importing this remote module does not
# depend on a second local Modal module. The dependency image layer is cached.
image = (modal.Image.debian_slim(python_version='3.14')
         .pip_install_from_requirements('scripts/requirements.txt')
         .env({'HF_HOME': '/persist/hf', 'TOKENIZERS_PARALLELISM': 'false'}))

app = modal.App('model-training-workshop-rlvr')
rl_image = image.add_local_file('scripts/rlvr.py', '/work/scripts/rlvr.py')


@app.function(image=rl_image, gpu='L4', cpu=2, memory=8192, timeout=600,
              retries=0, max_containers=1, volumes={'/persist': volume})
def experiment(sft_run, groups, rollouts):
    import sys
    started = time.monotonic()
    sys.path.insert(0, '/work/scripts')
    from rlvr import run
    name = f'rlvr-{time.time_ns()}'
    path = Path('/persist/runs') / name
    try:
        result = run(str(Path('/persist/runs') / sft_run), str(path), groups, rollouts, 'cuda')
        result['remote_seconds'] = time.monotonic() - started
        result['estimated_compute_usd'] = result['remote_seconds'] * (.000222 + 2*.0000131 + 8*.00000222)
        (path / 'rl_result.json').write_text(json.dumps(result, indent=2), encoding='utf-8', newline='\n')
        return name, {p.name: p.read_text(encoding='utf-8') for p in path.iterdir() if p.is_file()}
    finally:
        volume.commit()


@app.local_entrypoint()
def main(sft_run: str, groups: int = 12, rollouts: int = 4):
    if Path(sft_run).name != sft_run or not 1 <= groups <= 32 or not 2 <= rollouts <= 8:
        raise ValueError('Use a single SFT run directory name, <=32 groups, and 2–8 rollouts')
    name, files = experiment.remote(sft_run, groups, rollouts)
    out = Path('runs') / name
    out.mkdir(parents=True, exist_ok=False)
    for filename, content in files.items():
        (out / filename).write_text(content, encoding='utf-8', newline='\n')
    print('Results:', out)
