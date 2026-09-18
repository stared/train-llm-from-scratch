"""Add probabilities to existing example text only when checkpoint replay matches."""
import json
from pathlib import Path
import sys
import modal

ROOT=Path(__file__).resolve().parents[2] if modal.is_local() else Path('/work')
if modal.is_local():
    sys.path.insert(0,str(ROOT/'scripts'))
    from scratch_recipe_modal import image as scratch_image
    from rlvr_showcase_modal import image as rlvr_image
else:
    # The deployed images are already resolved; local recipe imports are unnecessary here.
    scratch_image=rlvr_image=modal.Image.debian_slim()

app=modal.App('workshop-visualization-traces')
volume=modal.Volume.from_name('model-training-workshop')


@app.function(image=scratch_image,gpu='H100',cpu=2,memory=16384,timeout=180,retries=0,volumes={'/persist':volume})
def scratch():
    import time
    import torch
    from tokenizers import Tokenizer
    sys.path.insert(0,'/work/scripts')
    from scratch_model import ScratchGPT,Config
    from training_progress import token_records
    started=time.monotonic()
    name='scratch-wolne-lektury-30m-1789676785288825614'
    folder=Path('/persist/runs')/name
    result=json.loads((folder/'result.json').read_text())
    tokenizer=Tokenizer.from_file(str(folder/'tokenizer.json'))
    output={}
    for stage in ('before','selected'):
        torch.manual_seed(result['seed'])
        model=ScratchGPT(Config(**result['config'])).cuda().eval()
        if stage=='selected':model.load_state_dict(torch.load(folder/'best.pt',map_location='cuda',weights_only=True))
        rows=json.loads((folder/f'samples_{stage}.json').read_text())
        torch.manual_seed(2026)
        for row in rows[:2]:
            ids=torch.tensor([tokenizer.encode(row['prompt']).ids],device='cuda')
            with torch.autocast('cuda',dtype=torch.bfloat16):
                generated,trace=model.generate(ids,new_tokens=128,return_trace=True)
            text=tokenizer.decode(generated[0,ids.shape[1]:].tolist(),skip_special_tokens=False)
            if text!=row['continuation']:raise ValueError('Replay differs; refusing to attach probabilities to different text')
            row['tokens']=token_records([t['id'] for t in trace],[t['probability'] for t in trace],
                [t['alternatives'] for t in trace],tokenizer,[t['sampling_probability'] for t in trace])
        output[f'visualization_samples_{stage}.json']=rows
        del model
    return name,output,dict(seconds=time.monotonic()-started,rate=.001097+2*.0000131+16*.00000222)


@app.function(image=rlvr_image,gpu='L4',cpu=2,memory=16384,timeout=180,retries=0,volumes={'/persist':volume})
def rlvr():
    import time
    import torch
    from transformers import AutoTokenizer,AutoModelForImageTextToText,GenerationConfig
    from peft import PeftModel
    sys.path.insert(0,'/work/scripts')
    from training_progress import completion_trace
    started=time.monotonic()
    name='rlvr-train-six_words-1789672431850535000'
    folder=Path('/persist/runs')/name
    result=json.loads((folder/'result.json').read_text());spec=result['model_spec']
    tokenizer=AutoTokenizer.from_pretrained(spec['id'],revision=spec['revision'])
    tokenizer.padding_side='left'
    if tokenizer.pad_token_id is None:tokenizer.pad_token=tokenizer.eos_token
    model=AutoModelForImageTextToText.from_pretrained(spec['id'],revision=spec['revision'],dtype=torch.bfloat16,attn_implementation='sdpa').cuda().eval()
    output={}
    for stage in ('before','after'):
        if stage=='after':model=PeftModel.from_pretrained(model,folder/'adapter').eval()
        rows=json.loads((folder/f'{stage}_dev.json').read_text())
        prompts=[tokenizer.apply_chat_template([dict(role='user',content=row['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False) for row in rows[:8]]
        inputs=tokenizer(prompts,padding=True,add_special_tokens=False,return_tensors='pt').to('cuda')
        with torch.no_grad():
            seq=model.generate(**inputs,generation_config=GenerationConfig(max_new_tokens=40,do_sample=False,pad_token_id=tokenizer.pad_token_id,eos_token_id=tokenizer.eos_token_id))
        offset=inputs.input_ids.shape[1]
        text=tokenizer.decode(seq[0,offset:],skip_special_tokens=True)
        if text!=rows[0]['text']:raise ValueError('Replay differs; refusing to attach probabilities to different text')
        rows[0]['tokens']=completion_trace(model,tokenizer,seq,inputs.attention_mask,offset)
        output[f'visualization_{stage}_dev.json']=rows
    return name,output,dict(seconds=time.monotonic()-started,rate=.000222+2*.0000131+16*.00000222)


@app.local_entrypoint()
def main(kind: str):
    if kind not in ('scratch','rlvr'):raise ValueError('Choose scratch or rlvr')
    name,files,timing=(scratch if kind=='scratch' else rlvr).remote()
    folder=ROOT/'runs'/name
    for filename,value in files.items():(folder/filename).write_text(json.dumps(value,ensure_ascii=False))
    timing['estimated_compute_usd']=timing['seconds']*timing['rate']
    (folder/'visualization_trace_cost.json').write_text(json.dumps(timing,indent=2))
    print('Matched replay:',name,json.dumps(timing))
