# /// script
# requires-python = ">=3.14"
# dependencies = ["modal==1.5.5"]
# ///
"""Fetch detached results into this repository; no GPU is started."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
import json
from pathlib import Path
import modal
from sync_scratch_runs import sync

ROOT=Path(__file__).resolve().parents[2]
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    pointer=ROOT/'additional/research/scratch/latest_polish_batch.json'
    latest=json.loads(pointer.read_text())['batch_id'] if pointer.exists() else 'polish-1788888781465950317'
    parser.add_argument('batch',default=latest,nargs='?')
    parser.add_argument('--weights',action='store_true')
    args=parser.parse_args()
    if Path(args.batch).name!=args.batch or not args.batch.startswith('polish-'):
        raise ValueError('Expected a Polish experiment batch ID')
    volume=modal.Volume.from_name('model-training-workshop')
    out=ROOT/'runs'/args.batch;out.mkdir(parents=True,exist_ok=True)
    for entry in volume.listdir('/experiments/'+args.batch):
        filename=Path(entry.path).name
        if Path(filename).suffix in ('.json','.html','.md'):
            (out/filename).write_bytes(b''.join(volume.read_file(entry.path)))
    manifest=json.loads((out/'manifest.json').read_text())
    names=[result['run'] for result in manifest['results'] if 'run' in result]
    if names:sync(names,args.weights)
    print(manifest['status'],out)
