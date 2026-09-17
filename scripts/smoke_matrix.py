"""Run a deliberately small sequential verification matrix. Never retries.

One GPU at a time; five jobs, each capped remotely at 600 seconds.
Approximate requested runtime compute ceiling: $0.80, plus startup/build/storage.
"""
import json
from pathlib import Path
import subprocess
import time

JOBS = [
    ('lfm2.5-350m', 'extraction', 40),
    ('lfm2.5-350m', 'polish', 40),
    ('qwen3.5-0.8b', 'routing', 20),
    ('lfm2.5-2.6b', 'extraction', 20),
    ('gemma4-e2b', 'routing', 2),
]


if __name__ == '__main__':
    out = Path('runs') / f'matrix-{time.time_ns()}'
    out.mkdir(parents=True)
    records = []
    for model, task, steps in JOBS:
        command = ['modal', 'run', 'scripts/modal_app.py', '--model', model, '--task', task,
                   '--steps', str(steps), '--eval-size', '8', '--max-seconds', '90']
        print('RUN', ' '.join(command), flush=True)
        start = time.monotonic()
        with (out / f'{model}-{task}.log').open('w') as log:
            process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
        records.append(dict(model=model, task=task, steps=steps, returncode=process.returncode,
                            local_elapsed_seconds=time.monotonic() - start))
        (out / 'matrix.json').write_text(json.dumps(records, indent=2))
        print('DONE', records[-1], flush=True)
    print('Logs:', out, flush=True)
