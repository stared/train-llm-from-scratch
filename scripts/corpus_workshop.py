# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Full-book continued pretraining with LoRA, without instruction/answer pairs."""
import argparse
import gc
import hashlib
import json
from pathlib import Path
import random
import time

from style_workshop import setup, write_json, generate
from corpus_chunks import chunk_tokens

PROMPTS = [
    {'mode':'completion', 'prompt':'Na biurku laptop drzemał, za oknami świta,\n'},
    {'mode':'completion', 'prompt':'Wtem wszedł programista, niosąc wieść od rana,\n'},
    {'mode':'chat', 'prompt':'Wyjaśnij, czym jest kopia zapasowa.'},
    {'mode':'chat', 'prompt':'Napisz cztery wersy o programiście, któremu zepsuł się komputer.'},
]


def run(data_dir, output, model_key='lfm2.5-2.6b', epochs=1, max_seconds=600, device='cuda',
        target_tokens=256, batch_size=2, line_aligned=False):
    import torch
    from peft import LoraConfig, get_peft_model, PeftModel
    from transformers import GenerationConfig
    if not 1<=epochs<=3 or not 60<=max_seconds<=600:
        raise ValueError('Use 1–3 epochs and a 60–600-second training budget')
    if target_tokens not in (256, 1024, 2048, 4096) or batch_size not in (1, 2):
        raise ValueError('Choose 256/1024/2048/4096 target tokens and batch size 1/2')
    started=time.monotonic()
    data_dir, out=Path(data_dir), Path(output)
    manifest=json.loads((data_dir/'corpus.json').read_text())
    raw=(data_dir/'train.txt').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=manifest['text_sha256']:
        raise ValueError('Corpus hash mismatch')
    out.mkdir(parents=True,exist_ok=False)
    write_json(out/'corpus.json',manifest)
    torch.manual_seed(42)
    tokenizer, stop, load, spec=setup(model_key,device)
    text=raw.decode()
    encoded=tokenizer(text,add_special_tokens=False,return_offsets_mapping=line_aligned)
    token_ids=encoded['input_ids']
    line_ends=([i+1 for i,(_,end) in enumerate(encoded['offset_mapping'])
                if end>0 and text[end-1]=='\n'] if line_aligned else None)
    blocks,forced_splits=chunk_tokens(token_ids,target_tokens,line_ends)
    assert sum(len(b)-1 for b in blocks)==len(token_ids)-1
    write_json(out/'token_example.json',{'ids':blocks[0], 'decoded':tokenizer.decode(blocks[0]),
               'mask_note':'All actual next-token targets supervised; padding masked. No chat template.'})
    model=load()

    def evaluate(label):
        model.eval()
        answers=[]
        for row in PROMPTS:
            if row['mode']=='chat':
                answer=generate(model,tokenizer,stop,[row['prompt']],device)[0]
            else:
                inputs=tokenizer(row['prompt'],add_special_tokens=False,return_tensors='pt').to(device)
                with torch.inference_mode():
                    seq=model.generate(**inputs,generation_config=GenerationConfig(
                        max_new_tokens=128,do_sample=False,eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=tokenizer.pad_token_id))
                answer=tokenizer.decode(seq[0,inputs.input_ids.shape[1]:],skip_special_tokens=True)
            answers.append({**row,'answer':answer})
        write_json(out/f'{label}.json',answers)
        print(label,answers[0]['answer'],flush=True)
        return answers

    before=evaluate('before')
    targets=[name for name,m in model.named_modules() if isinstance(m,torch.nn.Linear)
             and name.rsplit('.',1)[-1] in ('q_proj','v_proj','o_proj','gate_proj','up_proj','down_proj')
             and not any(s in name for s in ('vision','visual','audio'))]
    if not targets:
        raise ValueError('No LoRA target modules')
    model=get_peft_model(model,LoraConfig(r=8,lora_alpha=16,lora_dropout=.05,
                           target_modules=targets,task_type='CAUSAL_LM'))
    if target_tokens>256:
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={'use_reentrant':False})
        model.enable_input_require_grads()
    optimizer=torch.optim.AdamW([p for p in model.parameters() if p.requires_grad],lr=1e-4)
    rng=random.Random(42)
    schedule=[]
    for _ in range(epochs):
        order=list(range(len(blocks)));rng.shuffle(order);schedule.extend(order)
    seen=set();trained_tokens=0;history=[]
    model.train(); train_start=time.monotonic()
    for start in range(0,len(schedule),batch_size):
        chosen=schedule[start:start+batch_size]
        batch=[blocks[i] for i in chosen]
        length=max(map(len,batch))
        ids=torch.tensor([b+[tokenizer.pad_token_id]*(length-len(b)) for b in batch],device=device)
        mask=torch.tensor([[1]*len(b)+[0]*(length-len(b)) for b in batch],device=device)
        labels=ids.clone();labels[mask==0]=-100
        optimizer.zero_grad(set_to_none=True)
        loss=model(input_ids=ids,attention_mask=mask,labels=labels,use_cache=False).loss
        if not torch.isfinite(loss):raise RuntimeError('Non-finite loss')
        loss.backward();torch.nn.utils.clip_grad_norm_(model.parameters(),1.);optimizer.step()
        seen.update(chosen);trained_tokens+=sum(len(b)-1 for b in batch)
        history.append({'step':len(history)+1,'loss':loss.item(),
                        'seconds':time.monotonic()-train_start,'target_tokens_seen':trained_tokens})
        if len(history)%25==1:print(history[-1],flush=True)
        if time.monotonic()-train_start>=max_seconds:break
    training_seconds=time.monotonic()-train_start
    model.save_pretrained(out/'adapter');tokenizer.save_pretrained(out/'tokenizer')
    write_json(out/'loss.json',history)
    after=evaluate('after')
    nonzero=any(p.detach().abs().sum().item()>0 for n,p in model.named_parameters() if 'lora_B' in n)
    del optimizer,loss,model
    gc.collect()
    if device=='cuda':torch.cuda.empty_cache()
    model=PeftModel.from_pretrained(load(),out/'adapter')
    reloaded=evaluate('reloaded')
    result={'model':model_key,'model_spec':spec,'objective':'continued pretraining on raw literary text',
            'target_tokens_per_chunk':target_tokens,'batch_size':batch_size,
            'line_aligned':line_aligned,'forced_line_splits':forced_splits,
            'gradient_checkpointing':target_tokens>256,
            'corpus':manifest,'corpus_tokens':len(token_ids),'blocks':len(blocks),
            'unique_blocks_seen':len(seen),'full_corpus_seen':len(seen)==len(blocks),
            'unique_target_fraction':sum(len(blocks[i])-1 for i in seen)/(len(token_ids)-1),
            'target_tokens_seen':trained_tokens,'epochs_requested':epochs,'steps':len(history),
            'training_seconds':training_seconds,'total_seconds':time.monotonic()-started,
            'adapter_nonzero':nonzero,'reload_matches':after==reloaded,
            'peak_vram_gb':torch.cuda.max_memory_allocated()/1e9 if device=='cuda' else None,
            'evaluation_note':'Original continuation prompts and two chat probes; no held-out perplexity. Full book includes text potentially present in base pretraining. No claim of generalization or always-poetic chat.'}
    write_json(out/'corpus_result.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir',default='datasets/pan-tadeusz-full')
    p.add_argument('--output',required=True)
    p.add_argument('--model',default='lfm2.5-2.6b')
    p.add_argument('--epochs',type=int,default=1)
    p.add_argument('--max-seconds',type=int,default=600)
    p.add_argument('--device',choices=['cuda','cpu','mps'],default='cpu')
    p.add_argument('--target-tokens',type=int,default=256)
    p.add_argument('--batch-size',type=int,default=2)
    p.add_argument('--line-aligned',action='store_true')
    a=p.parse_args();run(a.data_dir,a.output,a.model,a.epochs,a.max_seconds,a.device,
                        a.target_tokens,a.batch_size,a.line_aligned)
