# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Generate from a saved scratch model in a fresh process."""
import argparse
from contextlib import nullcontext
import json
from pathlib import Path
import torch
from tokenizers import Tokenizer
from scratch_model import ScratchGPT,Config
from train_scratch import PROMPTS


def sample(run,output,device):
    run=Path(run)
    result=json.loads((run/'result.json').read_text(encoding='utf-8'))
    model=ScratchGPT(Config(**result['config'])).to(device)
    model.load_state_dict(torch.load(run/'best.pt',map_location=device,weights_only=True))
    model.eval()
    tokenizer=Tokenizer.from_file(str(run/'tokenizer.json'))
    torch.manual_seed(2026)
    records=[]
    for prompt in result.get('generation_prompts',PROMPTS):
        ids=torch.tensor([tokenizer.encode(prompt).ids],device=device)
        with torch.autocast('cuda',dtype=torch.bfloat16) if device=='cuda' else nullcontext():
            generated=model.generate(ids,new_tokens=128)
        records.append(dict(prompt=prompt,continuation=tokenizer.decode(generated[0,ids.shape[1]:].tolist(),skip_special_tokens=False)))
    Path(output).write_text(json.dumps(records,ensure_ascii=False,indent=2), encoding='utf-8', newline='\n')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('run')
    p.add_argument('--output',default='scratch_samples.json')
    p.add_argument('--device',choices=['cpu','cuda'],default='cpu')
    a=p.parse_args();sample(a.run,a.output,a.device)
