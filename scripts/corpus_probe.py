# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Ordinary Polish chat before/after a saved full-book adapter; no training."""
import argparse
import json
from pathlib import Path

PROMPTS = [
    ('question','Dlaczego mój komputer znowu się zawiesił?'),
    ('question','Nie wiem, co chcę robić w życiu. Od czego zacząć?'),
    ('question','Dlaczego warto robić kopie zapasowe?'),
    ('question','Co robimy wieczorem?'),
    ('statement','Cześć, właśnie wróciłem z pracy.'),
    ('statement','Dzisiaj wszystko idzie nie tak.'),
    ('statement','Za oknem pada deszcz, a ja siedzę przy komputerze.'),
    ('statement','Dobra, jedziemy. Samochód już czeka.'),
]

def probe(adapter_dir, output, device='cuda', long_output_tokens=0):
    import torch
    from peft import PeftModel
    from style_workshop import setup, generate
    if long_output_tokens not in (0, 1024):
        raise ValueError('Long-output diagnostic is disabled (0) or capped at 1024 tokens')
    run=Path(adapter_dir)
    spec=json.loads((run/'corpus_result.json').read_text())
    tokenizer,stop,load,_=setup(spec['model'],device)
    model=load()
    rows=[]
    longer_rows=[]
    for variant in ('before','after'):
        if variant=='after':model=PeftModel.from_pretrained(model,run/'adapter')
        torch.manual_seed(42)
        for start in range(0,len(PROMPTS),4):
            batch=PROMPTS[start:start+4]
            answers=generate(model,tokenizer,stop,[p for _,p in batch],device,
                             sample=True,temperature=.7,top_p=.8,top_k=20,
                             repetition_penalty=1.1,max_tokens=192)
            rows.extend(dict(variant=variant,kind=kind,prompt=prompt,answer=answer)
                        for (kind,prompt),answer in zip(batch,answers))
        if long_output_tokens:
            torch.manual_seed(42)
            batch=PROMPTS[:2]
            answers=generate(model,tokenizer,stop,[p for _,p in batch],device,
                             sample=True,temperature=.7,top_p=.8,top_k=20,
                             repetition_penalty=1.1,max_tokens=long_output_tokens)
            longer_rows.extend(dict(variant=variant,kind=kind,prompt=prompt,answer=answer)
                               for (kind,prompt),answer in zip(batch,answers))
    result=dict(model=spec['model_spec'],training_corpus=spec['corpus'],
                training_objective=spec['objective'],adapter_run=run.name,
                full_corpus_seen=spec['full_corpus_seen'],evaluation_only=True,
                system_prompt=None,adapter_scale=1.0,batch_size=4,
                decoding=dict(seed=42,temperature=.7,top_p=.8,top_k=20,
                              repetition_penalty=1.1,max_new_tokens=192),rows=rows,
                longer_output_diagnostic=dict(max_new_tokens=long_output_tokens,batch_size=2,
                                              rows=longer_rows),
                training_target_tokens=spec.get('target_tokens_per_chunk',256))
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    (out/'probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--adapter-dir',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--device',default='cuda',choices=['cuda','cpu','mps'])
    p.add_argument('--long-output-tokens',type=int,default=0,choices=[0,1024])
    a=p.parse_args();probe(a.adapter_dir,a.output,a.device,a.long_output_tokens)
