# /// script
# requires-python = ">=3.14"
# dependencies = ["modal==1.5.5"]
# ///
"""Copy experiment artifacts from Modal into visible local runs/ directories."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
from pathlib import Path
import modal

ROOT=Path(__file__).resolve().parents[2]

def sync(names,weights=False):
    volume=modal.Volume.from_name('model-training-workshop')
    for name in names:
        if Path(name).name!=name or not name.startswith('scratch-'):
            raise ValueError('Pass a scratch run directory name')
        out=ROOT/'runs'/name;out.mkdir(parents=True,exist_ok=True)
        count=0
        for entry in volume.listdir('/runs/'+name):
            remote=Path(entry.path)
            if remote.suffix not in ('.json','.py') and not (weights and remote.suffix=='.pt'):continue
            target=out/remote.name
            if target.suffix=='.pt' and target.exists():continue
            partial=target.with_name(target.name+'.part')
            with partial.open('wb') as f:
                for chunk in volume.read_file(entry.path):f.write(chunk)
            partial.replace(target);count+=1
        print(name,count,'files copied',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs',nargs='+');p.add_argument('--weights',action='store_true')
    a=p.parse_args();sync(a.runs,a.weights)
