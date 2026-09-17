"""Measure the existing five-minute checkpoints with the same fixed diagnostics."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-scratch-baseline-quality')
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.14').pip_install_from_requirements('scripts/requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2'))
for file in ('scratch_model.py','scratch_quality.py'):
    image=image.add_local_file('scripts/' + file,'/work/scripts/'+file)

@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=300,retries=0,max_containers=1,volumes={'/persist':volume})
def evaluate():
    import sys
    sys.path.insert(0,'/work/scripts')
    import torch
    from tokenizers import Tokenizer
    from scratch_model import ScratchGPT,Config
    from scratch_quality import evaluate_quality
    start=time.monotonic();results={}
    for name in ('scratch-wikitext-10m-1788878678148970671','scratch-wikitext-30m-1788879030853732196'):
        root=Path('/persist/runs')/name
        metadata=json.loads((root/'result.json').read_text())
        model=ScratchGPT(Config(**metadata['config'])).cuda()
        model.load_state_dict(torch.load(root/'best.pt',map_location='cuda',weights_only=True))
        tokenizer=Tokenizer.from_file(str(root/'tokenizer.json'))
        quality=evaluate_quality(model,tokenizer,'cuda',root/'quality.json')
        quality.update(model=metadata['model'],source=metadata['source'],checkpoint='best.pt',run=name)
        (root/'quality.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2))
        results[name]=quality
        del model
        torch.cuda.empty_cache()
    cost=dict(seconds=time.monotonic()-start,estimated_compute_usd=(time.monotonic()-start)*(.000222+2*.0000131+16*.00000222))
    volume.commit()
    return results,cost

@app.local_entrypoint()
def main():
    results,cost=evaluate.remote()
    for name,quality in results.items():(Path('runs')/name/'quality.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2))
    Path('runs/scratch_baseline_quality_cost.json').write_text(json.dumps(cost,indent=2))
    print(json.dumps(cost))
