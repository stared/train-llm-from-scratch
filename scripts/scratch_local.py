# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Train a fresh ScratchGPT on this computer from locally prepared tokens.

Uses the Apple GPU (MPS) or CUDA when available, otherwise the CPU. Progress
appears in the local viewer (pnpm dev) during training, like a Modal run.
"""
import argparse
from pathlib import Path
import time

import torch
from train_scratch import run
from training_progress import reporter, write_live

ROOT = Path(__file__).resolve().parents[1]
# size, prepared data, batch size, context, warmup updates
RECIPES = {
    'sejm': ('10m', 'sejm-scratch-v1', 32, 256, 20),
    'sejm-30m': ('30m', 'sejm-scratch-v1', 32, 512, 100),
}
PEAK_LR = {'10m': 6e-4, '30m': 6e-4, '100m': 4e-4, '300m': 3e-4}


def default_device():
    return 'mps' if torch.backends.mps.is_available() else 'cuda' if torch.cuda.is_available() else 'cpu'


class LiveChannel:
    """In-process stand-in for the Modal queue used by training_progress.reporter."""
    def __init__(self, folder, started):
        self.folder, self.started, self.events = folder, started, []

    def put(self, event, timeout=None):
        self.events.append(event)
        self.write('Running')

    def write(self, status, final=None):
        write_live(self.folder, 'pretrain', self.events, status, self.started, final=final)


def main(recipe, max_seconds, device, batch_size, size, data):
    default_size, data_name, default_batch, context, warmup = RECIPES[recipe]
    size = size or default_size
    data_dir = Path(data) if data else ROOT/'datasets/local'/data_name
    if not (data_dir/'tokens.json').exists():
        raise SystemExit(f'No prepared tokens in {data_dir}. Run first:\nuv run scripts/prepare_pretraining.py sejm')
    device = device or default_device()
    batch_size = batch_size or default_batch
    stamp = time.time_ns()
    out = ROOT/'runs'/f'scratch-{recipe}-{size}-{stamp}'
    live = ROOT/'runs'/f'live-pretrain-{stamp}'
    live.mkdir(parents=True)
    channel = LiveChannel(live, time.monotonic())
    channel.write('Running')
    print(f'{device}, ScratchGPT-{size}, batch {batch_size}, context {context}; training budget {max_seconds}s', flush=True)
    print('Open during training: pnpm dev', flush=True)
    try:
        run(data_dir, out, size, max_seconds, 42, device, batch_size, context_length=context,
            eval_interval=60, peak_lr=PEAK_LR[size], warmup_steps=warmup,
            research_limit_seconds=max(600, max_seconds), progress=reporter(channel))
    except KeyboardInterrupt:
        channel.write('Interrupted')
        raise
    except BaseException:
        channel.write('Failed')
        raise
    channel.write('Completed', final=out.name)
    print('Saved', out)
    print('View results: pnpm dev', flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--recipe', choices=list(RECIPES), default='sejm')
    p.add_argument('--max-seconds', type=int, default=600, help='Training budget, 60 to 8400 seconds')
    p.add_argument('--device', choices=['cpu', 'cuda', 'mps'], help='Default: mps, then cuda, then cpu')
    p.add_argument('--batch-size', type=int, choices=[8, 16, 32, 64], help='Default from the recipe')
    p.add_argument('--size', choices=list(PEAK_LR), help='Override the recipe model size')
    p.add_argument('--data', help='Prepared token folder (default from the recipe)')
    a = p.parse_args()
    if not 60 <= a.max_seconds <= 8400:
        p.error('--max-seconds must be between 60 and 8400')
    main(a.recipe, a.max_seconds, a.device, a.batch_size, a.size, a.data)
