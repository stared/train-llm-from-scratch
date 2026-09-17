# /// script
# requires-python = ">=3.14"
# dependencies = ["modal==1.5.5"]
# ///
"""Fetch completed overnight records (no weights and no GPU)."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import modal
ROOT=Path(__file__).resolve().parents[2]

def fetch(batch, only_run=None):
    if not batch.isdigit():raise ValueError('Pass the numeric batch ID printed at launch')
    volume=modal.Volume.from_name('model-training-workshop')
    out=ROOT/'runs'/('night-'+batch);out.mkdir(parents=True,exist_ok=True)
    raw=b''.join(volume.read_file('/experiments/night-'+batch+'/manifest.json'))
    (out/'manifest.json').write_bytes(raw);manifest=json.loads(raw)
    jobs=[];folders=[]
    def status(folder,state):
        folder.mkdir(parents=True,exist_ok=True)
        temp=folder/'fetch-status.tmp';temp.write_text(json.dumps({'state':state}))
        temp.replace(folder/'fetch-status.json')
    for result in manifest['results']:
        if 'run' not in result:continue
        if result['status']=='skipped':continue  # Dependency skips never created a GPU run directory.
        name=result['run']
        if only_run and name!=only_run:continue
        if Path(name).name!=name:raise ValueError('Unexpected run name')
        remote='/runs/'+name;local=ROOT/'runs'/name
        status(local,'fetching');folders.append(local)
        def entries(path,target):
            for entry in volume.listdir(path):
                filename=Path(entry.path).name
                if filename.startswith('stage-'):
                    entries(entry.path,target/filename)
                elif Path(filename).suffix in ('.json','.py'):
                    dest=target/filename
                    if not dest.exists():jobs.append((entry.path,dest))
        entries(remote,local)
    def copy(job):
        path,target=job;target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(b''.join(volume.read_file(path)))
    with ThreadPoolExecutor(max_workers=8) as pool:list(pool.map(copy,jobs))
    for folder in folders:status(folder,'complete')
    print(batch,manifest['status'],len(manifest['results']),'completed records',len(jobs),'files downloaded')
    for row in manifest['results']:print(row['status'],row.get('run'),row.get('estimated_compute_usd'))
    return manifest

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('batches',nargs='+')
    p.add_argument('--run',dest='only_run',help='Fetch one named worker, avoiding repeated listings of a large batch')
    args=p.parse_args()
    for batch in args.batches:fetch(batch,args.only_run)
