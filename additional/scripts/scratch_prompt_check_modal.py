"""Exploratory prompt-format check, separate from the frozen factual diagnostics."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import json
from pathlib import Path
import time
import modal

app=modal.App('workshop-scratch-prompt-check')
volume=modal.Volume.from_name('model-training-workshop')
image=(modal.Image.debian_slim(python_version='3.14').pip_install_from_requirements('scripts/requirements.txt')
       .pip_install('numpy==2.5.3','tokenizers==0.23.2')
       .add_local_file('scripts/scratch_model.py','/work/scripts/scratch_model.py'))
PROMPTS=["'''Warszawa'''", "'''Kraków'''", "'''Wisła'''", "'''Polska'''", "Warszawa jest", "Stolicą Polski jest", "Wisła to"]

@app.function(image=image,gpu='L4',cpu=2,memory=16384,timeout=400,retries=0,max_containers=1,volumes={'/persist':volume})
def check(names):
    import sys
    sys.path.insert(0,'/work/scripts')
    import torch
    from tokenizers import Tokenizer
    from scratch_model import ScratchGPT,Config
    torch.set_num_threads(2);start=time.monotonic();records={}
    for name in names:
        root=Path('/persist/runs')/name;r=json.loads((root/'result.json').read_text())
        model=ScratchGPT(Config(**r['config'])).cuda();model.load_state_dict(torch.load(root/'best.pt',map_location='cuda',weights_only=True));model.eval()
        tok=Tokenizer.from_file(str(root/'tokenizer.json'));rows=[]
        for i,prompt in enumerate(PROMPTS):
            torch.manual_seed(22000+i)
            ids=torch.tensor([tok.encode(prompt).ids],device='cuda')
            with torch.autocast('cuda',dtype=torch.bfloat16):output=model.generate(ids,new_tokens=256,temperature=.8,top_k=50)
            raw=tok.decode(output[0,ids.shape[1]:].tolist(),skip_special_tokens=False)
            rows.append(dict(prompt=prompt,raw_continuation=raw,continuation_until_eod=raw.split('<|endoftext|>')[0],seed=22000+i))
        report=dict(model=r['model'],source=r['source'],checkpoint='best.pt',run=name,temperature=.8,top_k=50,new_tokens=256,
                    purpose='Exploratory alternate prompt formats chosen after seeing original failures; not the frozen benchmark. Display may stop at first generated EOD; raw256-token output preserved.',rows=rows)
        (root/'prompt_format_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));records[name]=report
        del model;torch.cuda.empty_cache()
    cost=dict(seconds=time.monotonic()-start,estimated_compute_usd=(time.monotonic()-start)*(.000222+2*.0000131+16*.00000222))
    volume.commit();return records,cost

@app.local_entrypoint()
def main(names:str):
    records,cost=check.remote(names.split(','))
    for name,report in records.items():(Path('runs')/name/'prompt_format_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    Path(f'runs/scratch_prompt_check_cost_{time.time_ns()}.json').write_text(json.dumps(cost,indent=2));print(json.dumps(cost))
