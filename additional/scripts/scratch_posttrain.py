# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Full-weight SFT / answer-only RLVR of our scratch GPT, with held-out evaluation."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import random
import sys
import time

ROOT=Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents)>2 else Path('/work')
sys.path.insert(0,str(ROOT/'scripts'))
from scratch_model import ScratchGPT,Config
from prawko import question

def save(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2))

def run(base,output,task='exam',method='sft',seconds=600,lr=1e-4,seed=42,random_init=False,lora_rank=0,beta=.01,dataset_path=None):
    import torch
    from tokenizers import Tokenizer
    if task not in ('exam','poetry','wiki-qa') or method not in ('sft','rlvr','sft-rlvr'):
        raise ValueError('Unsupported task/method')
    if task!='exam' and method!='sft':raise ValueError('Only exam has a verifiable answer key')
    if not 60<=seconds<=1200:raise ValueError('Bounded 60–1200 seconds per stage')
    torch.set_num_threads(2);torch.manual_seed(seed);rng=random.Random(seed)
    base=Path(base);out=Path(output);out.mkdir(parents=True,exist_ok=False)
    meta=json.loads((base/'result.json').read_text())
    config=Config(**meta['config'])
    model=ScratchGPT(config).cuda()
    if not random_init:model.load_state_dict(torch.load(base/'best.pt',map_location='cuda',weights_only=True))
    if lora_rank:
        class LoRALinear(torch.nn.Module):
            def __init__(self,linear):
                super().__init__();self.base=linear
                self.a=torch.nn.Parameter(torch.randn(lora_rank,linear.in_features,device='cuda')*.01)
                self.b=torch.nn.Parameter(torch.zeros(linear.out_features,lora_rank,device='cuda'))
            def forward(self,x):
                return self.base(x)+2*torch.nn.functional.linear(torch.nn.functional.linear(x,self.a),self.b)
        for p in model.parameters():p.requires_grad_(False)
        for block in model.blocks:
            block.attention.qkv=LoRALinear(block.attention.qkv)
            block.attention.proj=LoRALinear(block.attention.proj)
            for name in ('gate','up','down'):setattr(block,name,LoRALinear(getattr(block,name)))
    tok=Tokenizer.from_file(str(base/'tokenizer.json'))
    eod=tok.token_to_id('<|endoftext|>')
    labels=torch.tensor([tok.encode(c).ids[0] for c in 'ABC'],device='cuda')
    assert all(len(tok.encode(c).ids)==1 for c in 'ABC')
    if task=='exam':
        source=Path(dataset_path) if dataset_path else ROOT/'datasets/prawko-v2/data.json'
        data=json.loads(source.read_text())
    elif task=='poetry':
        folder=ROOT/'datasets/pan-tadeusz-qa-v1'
        train=[json.loads(l) for l in (folder/'train.jsonl').read_text().splitlines()]
        held=[json.loads(l) for l in (folder/'validation.jsonl').read_text().splitlines()]
        # Fixed split before training; pretraining may include all source verses.
        data={'train':train,'dev':held[:25],'test':held[25:]}
        source=folder/'train.jsonl'
    else:
        source=ROOT/'datasets/local/wiki-qa-research/data.json'
        if not source.exists():source=ROOT/'datasets/wiki-qa-research/data.json'
        data=json.loads(source.read_text())
    save(out/'data.json',data)
    def text_prompt(row,order=(0,1,2)):
        content=question(row,order)[0] if task=='exam' else row['prompt']
        return 'Pytanie: '+content+'\nOdpowiedź:\n'
    def encoded(row,order=(0,1,2)):
        ids=tok.encode(text_prompt(row,order)).ids
        if len(ids)>=config.context:raise ValueError(f"Prompt exceeds context: {row['id']}")
        return torch.tensor([ids],device='cuda')
    for rows in data.values():
        for row in rows:encoded(row)
    amp=lambda:torch.autocast('cuda',dtype=torch.bfloat16)
    def eval_exam(split,tag,rotate=False):
        model.eval();records=[]
        with torch.no_grad(),amp():
            for row in data[split]:
                order=(1,2,0) if rotate else (0,1,2)
                logits=model(encoded(row,order))[0]
                probs=logits[labels].softmax(-1)
                answer=order.index(row['answer']);pred=int(probs.argmax())
                records.append(dict(id=row['id'],question=row['question'],options=[row['options'][j] for j in order],
                    answer='ABC'[answer],prediction='ABC'[pred],correct=pred==answer,probabilities=probs.tolist()))
        save(out/(tag+'.json'),records)
        return {'n':len(records),'correct':sum(r['correct'] for r in records),
                'accuracy':sum(r['correct'] for r in records)/len(records),
                'correct_probability':sum(r['probabilities']['ABC'.index(r['answer'])] for r in records)/len(records)}
    def pair(row):
        prefix=tok.encode(text_prompt(row)).ids
        target=tok.encode(row['answer']).ids+[eod]
        ids=prefix+target
        if len(ids)>config.context+1:return None
        x=torch.tensor([ids[:-1]],device='cuda')
        y=torch.tensor([[-100]*(len(prefix)-1)+target],device='cuda')
        return x,y
    skipped={}
    if task!='exam':
        for split,rows in data.items():
            skipped[split]=sum(pair(r) is None for r in rows)
            data[split]=[r for r in rows if pair(r) is not None]
            if not data[split]:raise ValueError('No examples fit the context')
    def eval_text(split,tag):
        model.eval();losses=[]
        with torch.no_grad(),amp():
            for row in data[split][:50]:
                x,y=pair(row);losses.append(float(model(x,y)))
        return {'loss':sum(losses)/len(losses),'n':len(losses)}
    def samples(tag):
        if task=='exam':return
        model.eval();records=[]
        with torch.random.fork_rng(devices=[torch.cuda.current_device()]),torch.no_grad(),amp():
            torch.manual_seed(2026)
            for row in data['test'][:10]:
                ids=encoded(row);answer=[]
                for _ in range(192):
                    logits=model(ids[:,-config.context:])[0]/.8
                    top=logits.topk(40).values[-1]
                    token=int(torch.multinomial(logits.masked_fill(logits<top,-float('inf')).softmax(-1),1))
                    if token==eod:break
                    answer.append(token);ids=torch.cat([ids,torch.tensor([[token]],device='cuda')],1)
                records.append({'id':row['id'],'prompt':row['prompt'],'reference':row['answer'],
                                'text':tok.decode(answer),'tokens':len(answer),'terminated':token==eod})
        save(out/(tag+'.json'),records)
    evaluate=eval_exam if task=='exam' else eval_text
    before={split:evaluate(split,'before_'+split) for split in ('train','dev','test')}
    if task=='exam':before['test_rotated']=eval_exam('test','before_test_rotated',True)
    samples('samples_before')
    stages=[]
    for stage_method in (['sft','rlvr'] if method=='sft-rlvr' else [method]):
        reference=copy.deepcopy(model).eval() if stage_method=='rlvr' else None
        if reference:
            for p in reference.parameters():p.requires_grad_(False)
        optimizer=torch.optim.AdamW([p for p in model.parameters() if p.requires_grad],lr=lr,weight_decay=.01)
        initial_dev=evaluate('dev',stage_method+'_dev_initial')
        best_score=(initial_dev['correct'],initial_dev['correct_probability']) if task=='exam' else (-initial_dev['loss'],)
        best={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};best_step=0
        start=time.monotonic();history=[];step=0;presentations=0
        while time.monotonic()-start<seconds:
            rows=rng.sample(data['train'],min(4,len(data['train'])))
            model.train();optimizer.zero_grad(set_to_none=True);loss_value=0.
            for row in rows:
                with amp():
                    if task=='exam':
                        order=rng.sample(range(3),3);x=encoded(row,order);correct=order.index(row['answer'])
                        full=model(x);logp=full[:,labels].log_softmax(-1)
                        if stage_method=='sft':
                            loss=torch.nn.functional.cross_entropy(full,labels[torch.tensor([correct],device='cuda')])
                        else:
                            actions=torch.multinomial(logp.detach().exp(),4,replacement=True)
                            rewards=actions.eq(correct).float()
                            advantages=rewards-(rewards.sum(-1,keepdim=True)-rewards)/3
                            with torch.no_grad():ref=reference(x)[:,labels].log_softmax(-1)
                            kl=(logp.exp()*(logp-ref)).sum(-1).mean()
                            loss=-(logp.gather(-1,actions)*advantages).mean()+beta*kl
                    else:
                        x,y=pair(row);loss=model(x,y)
                if not torch.isfinite(loss):raise RuntimeError('Nonfinite loss')
                (loss/len(rows)).backward();loss_value+=float(loss.detach())/len(rows)
            torch.nn.utils.clip_grad_norm_(model.parameters(),1.)
            optimizer.step();step+=1;presentations+=len(rows)
            if step%50==0:
                metric=evaluate('dev',f'{stage_method}_dev_{step}')
                score=(metric['correct'],metric['correct_probability']) if task=='exam' else (-metric['loss'],)
                history.append({'step':step,'seconds':time.monotonic()-start,'training_loss':loss_value,'dev':metric})
                if score>best_score:
                    best_score=score;best_step=step
                    best={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
                save(out/f'{stage_method}_history.json',history)
                print(stage_method,step,history[-1],flush=True)
        train_seconds=time.monotonic()-start
        final_dev=evaluate('dev',stage_method+'_final_dev')
        score=(final_dev['correct'],final_dev['correct_probability']) if task=='exam' else (-final_dev['loss'],)
        if score>best_score:
            best_step=step;best={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
        model.load_state_dict(best)
        after={split:evaluate(split,stage_method+'_after_'+split) for split in ('train','dev','test')}
        if task=='exam':after['test_rotated']=eval_exam('test',stage_method+'_after_test_rotated',True)
        torch.save(model.state_dict(),out/(stage_method+'.pt'))
        samples(stage_method+'_samples_after')
        stages.append({'method':stage_method,'selected_step':best_step,'steps':step,
                       'presentations':presentations,'exposure_ratio':presentations/len(data['train']),
                       'after':after,'training_seconds':train_seconds})
        del reference,optimizer
    result={'base_run':base.name,'initialization':'random' if random_init else 'pretrained',
            'base_data':meta.get('source'),'config':meta['config'],'task':task,'method':method,
            'seed':seed,'lr':lr,'lora_rank':lora_rank,'beta':beta,'before':before,'stages':stages,'skipped_over_context':skipped,
            'split_sizes':{split:len(rows) for split,rows in data.items()},
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'limitations':'Small held-out split. Poetry source verses may occur in pretraining; held-out prompts do not.'}
    save(out/'result.json',result)
    # Reload last selected weights and reproduce predictions.
    if task=='exam':
        old=json.loads((out/(stages[-1]['method']+'_after_test.json')).read_text())
        model.load_state_dict(torch.load(out/(stages[-1]['method']+'.pt'),weights_only=True))
        eval_exam('test','reload')
        new=json.loads((out/'reload.json').read_text())
        result['reload_matches']=[r['prediction'] for r in old]==[r['prediction'] for r in new]
        assert result['reload_matches']
    save(out/'result.json',result)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('base');p.add_argument('--output',required=True)
    p.add_argument('--task',choices=['exam','poetry','wiki-qa'],default='exam')
    p.add_argument('--method',choices=['sft','rlvr','sft-rlvr'],default='sft')
    p.add_argument('--seconds',type=int,default=600);p.add_argument('--lr',type=float,default=1e-4)
    p.add_argument('--dataset-path',type=Path)
    p.add_argument('--random-init',action='store_true')
    a=p.parse_args();run(a.base,a.output,a.task,a.method,a.seconds,a.lr,random_init=a.random_init,dataset_path=a.dataset_path)
