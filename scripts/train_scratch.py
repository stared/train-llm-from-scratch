# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Train a fresh GPT on the full Polish Wikipedia wikitext training pool."""
import argparse
from contextlib import nullcontext
from dataclasses import asdict
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import time

import numpy as np
import torch
from tokenizers import Tokenizer
from scratch_model import ScratchGPT, Config, config_for

PROMPTS = ["'''Warszawa''' –", '== Historia ==\n', '{{Infobox', "'''Polska''' –"]


def save(path,value):
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2))


class ShuffledWindows:
    """Visit every full training block once before reshuffling the next pass."""
    def __init__(self, token_count, context, seed):
        self.windows=(token_count-1)//context
        if self.windows<1:raise ValueError('Training corpus is shorter than one window')
        self.context=context;self.seed=seed;self.epoch=0;self.cursor=0;self.draws=0
        self.order=np.random.default_rng(seed).permutation(self.windows)

    def next(self,count):
        chunks=[];remaining=count
        while remaining:
            if self.cursor==self.windows:
                self.epoch+=1;self.cursor=0
                self.order=np.random.default_rng(self.seed+self.epoch).permutation(self.windows)
            take=min(remaining,self.windows-self.cursor)
            chunks.append(self.order[self.cursor:self.cursor+take]*self.context)
            self.cursor+=take;self.draws+=take;remaining-=take
        return np.concatenate(chunks)

    def state(self):
        return dict(seed=self.seed,epoch=self.epoch,cursor=self.cursor,windows=self.windows,
                    context=self.context,draws=self.draws,passes=self.draws/self.windows)


def run(data_dir, output, size='10m', max_seconds=300, seed=42, device='cuda', batch_size=32, context_length=256, eval_interval=60, peak_lr=6e-4, warmup_steps=20, checkpoint_hook=None, research_limit_seconds=600, sampling_mode='uniform', mixture_dir=None, progress=None, compile_training=False,initial_checkpoint=None,mixture_fraction=.5,optimizer_kind='adamw'):
    if not 60<=max_seconds<=research_limit_seconds<=8400 or batch_size not in (8,16,32,64,128,256):
        raise ValueError('Invalid explicit time budget or batch size')
    if sampling_mode not in ('uniform','openings','mixed','mixed-uniform','shuffled'):
        raise ValueError('Unknown sampling mode')
    if optimizer_kind not in ('adamw','muon'):raise ValueError('Unknown optimizer')
    if not 0<mixture_fraction<=1 or int(batch_size*mixture_fraction)<1:raise ValueError('Mixture must contain at least one sample per batch')
    if context_length not in (256,512,1024) or eval_interval<60 or warmup_steps<1 or not 0<peak_lr<=.002:
        raise ValueError('Invalid context/evaluation/learning-rate configuration')
    if device=='cuda' and not torch.cuda.is_bf16_supported():
        raise ValueError('This GPU recipe requires BF16 support')
    started=time.monotonic()
    if device=='cuda':torch.set_num_threads(2)  # Match reserved host CPU; avoid initialization oversubscription.
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    data_dir=Path(data_dir)
    metadata=json.loads((data_dir/'tokens.json').read_text())
    generation_prompts=metadata.get('generation_prompts',PROMPTS)
    tokenizer=Tokenizer.from_file(str(data_dir/'tokenizer.json'))
    if hashlib.sha256((data_dir/'tokenizer.json').read_bytes()).hexdigest()!=metadata['tokenizer_sha256']:
        raise ValueError('Tokenizer checksum mismatch')
    arrays={s:np.memmap(data_dir/f'{s}.bin',dtype='<u2',mode='r') for s in ('train','dev','test')}
    for split,arr in arrays.items():
        if len(arr)!=metadata['splits'][split]['tokens']:
            raise ValueError('Token count mismatch')
        with (data_dir/f'{split}.bin').open('rb') as f:
            if hashlib.file_digest(f,'sha256').hexdigest()!=metadata['splits'][split]['sha256']:
                raise ValueError('Token file checksum mismatch')
    config=config_for(size,metadata['vocab_size']);config.context=context_length
    extra=None;article_starts=None
    if sampling_mode not in ('uniform','shuffled'):
        extra_dir=Path(mixture_dir) if mixture_dir else data_dir
        extra_meta=json.loads((extra_dir/'tokens.json').read_text())
        if extra_meta['tokenizer_sha256']!=metadata['tokenizer_sha256']:
            raise ValueError('Mixture tokenizer mismatch')
        with (extra_dir/'train.bin').open('rb') as f:
            if hashlib.file_digest(f,'sha256').hexdigest()!=extra_meta['splits']['train']['sha256']:
                raise ValueError('Mixture training checksum mismatch')
        extra=np.memmap(extra_dir/'train.bin',dtype='<u2',mode='r')
        # Only training boundaries are indexed. Half of enriched samples begin
        # at the original article opening; others use random windows.
        if sampling_mode!='mixed-uniform':
            article_starts=np.concatenate(([0],np.flatnonzero(extra==extra_meta['eod_id'])+1))
            article_starts=article_starts[article_starts<len(extra)-config.context-1]
    torch.manual_seed(seed)
    if device=='cuda':
        torch.cuda.reset_peak_memory_stats()
    model=ScratchGPT(config).to(device)
    if initial_checkpoint:
        initial_checkpoint=Path(initial_checkpoint)
        initial_tokenizer=initial_checkpoint.parent/'tokenizer.json'
        if hashlib.sha256(initial_tokenizer.read_bytes()).hexdigest()!=metadata['tokenizer_sha256']:
            raise ValueError('Continued pretraining requires the same tokenizer')
        model.load_state_dict(torch.load(initial_checkpoint,map_location=device,weights_only=True))
    parameters=sum(p.numel() for p in model.parameters())
    # Muon is a research comparison; tied embeddings and norms stay on AdamW.
    matrices=[p for n,p in model.named_parameters() if p.dim()==2 and n!='embedding.weight']
    decay=[p for n,p in model.named_parameters() if p.dim()>=2 and (optimizer_kind=='adamw' or n=='embedding.weight')]
    no_decay=[p for p in model.parameters() if p.dim()<2]
    optimizer=torch.optim.AdamW([{'params':decay,'weight_decay':.1},{'params':no_decay,'weight_decay':0.}],
        lr=peak_lr,betas=(.9,.95),fused=device=='cuda')
    matrix_optimizer=torch.optim.Muon(matrices,lr=peak_lr,weight_decay=.1,adjust_lr_fn='match_rms_adamw') if optimizer_kind=='muon' else None
    rng=np.random.default_rng(seed)
    sampler=ShuffledWindows(len(arrays['train']),config.context,seed) if sampling_mode=='shuffled' else None
    eval_rng=np.random.default_rng(20260908)
    eval_context=256  # Same fixed evaluation windows as the original five-minute runs.
    offsets={s:eval_rng.integers(0,len(arr)-eval_context-1,size=(8,8)) for s,arr in arrays.items()}
    def context():
        return torch.autocast('cuda',dtype=torch.bfloat16) if device=='cuda' else nullcontext()
    def batch(split,starts,length=None):
        length=length or config.context
        block=np.stack([arrays[split][int(i):int(i)+length+1] for i in starts]).astype(np.int64)
        ids=torch.from_numpy(block).to(device)
        return ids[:,:-1],ids[:,1:]
    def evaluate(name,split):
        model.eval();losses=[]
        with torch.no_grad(),context():
            for starts in offsets[split]:
                x,y=batch(split,starts,eval_context);losses.append(model(x,y).item())
        result=dict(loss_nats=sum(losses)/len(losses),tokens=8*8*eval_context)
        save(out/f'{name}.json',result)
        return result
    def samples(name):
        # Preserve training RNG; same sampling seed for every time checkpoint.
        with torch.random.fork_rng(devices=[torch.cuda.current_device()] if device=='cuda' else []):
            torch.manual_seed(2026)
            records=[]; previews=[]
            for index,prompt in enumerate(generation_prompts):
                ids=torch.tensor([tokenizer.encode(prompt).ids],device=device)
                trace_enabled=hasattr(progress,'preview') and index<2
                with context():
                    generated=model.generate(ids,new_tokens=128,return_trace=True) if trace_enabled else model.generate(ids,new_tokens=128)
                if trace_enabled: generated,trace=generated
                row=dict(prompt=prompt,continuation=tokenizer.decode(generated[0,ids.shape[1]:].tolist(),skip_special_tokens=False))
                records.append(row)
                if trace_enabled:
                    from training_progress import token_records
                    row={**row,'tokens':token_records([t['id'] for t in trace],[t['probability'] for t in trace],
                        [t['alternatives'] for t in trace],tokenizer,[t['sampling_probability'] for t in trace])}
                previews.append(row)
        save(out/f'{name}.json',records)
        if progress is not None:
            save(out/f'visualization_{name}.json',previews)
            current_step=0 if name=='samples_before' else (best_step if name=='samples_selected' else step)
            getattr(progress,'preview',lambda **kw:None)(label=name.removeprefix('samples_').replace('_',' ').capitalize(),
                step=current_step,split='fixed prompts',rows=previews,
                metadata=dict(model=f'ScratchGPT-{size}',source=metadata.get('source_label','Polish Wikipedia')))
        return records
    before={s:evaluate('before_'+s,s) for s in ('train','dev','test')}
    samples('samples_before')
    if progress: progress('Development loss', 0, before['dev']['loss_nats'])
    if checkpoint_hook:checkpoint_hook(model,tokenizer,'before',0,0,out)
    best_loss=before['dev']['loss_nats'];best_step=0
    torch.save(model.state_dict(),out/'best.pt')
    history=[];checkpoints=[];step=0;tokens_seen=0;training_compute=0.
    train_forward=torch.compile(model.forward,mode='reduce-overhead') if compile_training else model.forward
    train_started=time.monotonic();next_eval=eval_interval
    while True:
        elapsed=time.monotonic()-train_started
        if elapsed>=max_seconds:
            break
        # Fixed wall-time budget, warmup in updates then time-based cosine decay.
        budget_fraction=min(elapsed/max_seconds,1.)
        lr=peak_lr*min((step+1)/warmup_steps,1.)*(.1+.9*.5*(1+math.cos(math.pi*budget_fraction)))
        for group in optimizer.param_groups:group['lr']=lr
        if matrix_optimizer:
            for group in matrix_optimizer.param_groups:group['lr']=lr
        tick=time.monotonic()
        starts=sampler.next(batch_size) if sampler else rng.integers(0,len(arrays['train'])-config.context-1,size=batch_size)
        x,y=batch('train',starts)
        if extra is not None:
            x=x.clone();y=y.clone()
            count=batch_size if sampling_mode=='openings' else int(batch_size*mixture_fraction)
            starts=rng.integers(0,len(extra)-config.context-1,size=count)
            if article_starts is not None:starts[:count//2]=rng.choice(article_starts,size=count//2)
            block=np.stack([extra[int(i):int(i)+config.context+1] for i in starts]).astype(np.int64)
            ids=torch.from_numpy(block).to(device)
            x[:count]=ids[:,:-1];y[:count]=ids[:,1:]
        model.train();optimizer.zero_grad(set_to_none=True)
        if matrix_optimizer:matrix_optimizer.zero_grad(set_to_none=True)
        with context():loss=train_forward(x,y)
        if not torch.isfinite(loss):raise RuntimeError('Nonfinite loss')
        loss.backward();norm=torch.nn.utils.clip_grad_norm_(model.parameters(),1.)
        optimizer.step()
        if matrix_optimizer:matrix_optimizer.step()
        if device=='cuda':torch.cuda.synchronize()
        training_compute+=time.monotonic()-tick
        step+=1;tokens_seen+=batch_size*config.context
        if step%25==0:
            record=dict(step=step,elapsed_seconds=time.monotonic()-train_started,loss=loss.item(),lr=lr,gradient_norm=norm.item(),tokens_seen=tokens_seen)
            history.append(record);print(json.dumps(record),flush=True)
            if progress: progress('Training loss', step, record['loss'])
        if next_eval<=time.monotonic()-train_started<max_seconds-15:
            metric=evaluate(f'dev_step_{step}','dev')
            checkpoint=dict(step=step,elapsed_seconds=time.monotonic()-train_started,tokens_seen=tokens_seen,**metric)
            checkpoints.append(checkpoint)
            if progress: progress('Development loss', step, metric['loss_nats'])
            if metric['loss_nats']<best_loss:
                best_loss=metric['loss_nats'];best_step=step;torch.save(model.state_dict(),out/'best.pt')
            samples(f'samples_step_{step}')
            print('checkpoint',json.dumps(checkpoint),flush=True)
            save(out/'history.json',history);save(out/'checkpoints.json',checkpoints)
            if checkpoint_hook:checkpoint_hook(model,tokenizer,'checkpoint',step,time.monotonic()-train_started,out)
            next_eval+=eval_interval
    training_seconds=time.monotonic()-train_started
    final={s:evaluate('final_'+s,s) for s in ('train','dev','test')}
    samples('samples_final')
    if progress: progress('Development loss', step, final['dev']['loss_nats'])
    if checkpoint_hook:checkpoint_hook(model,tokenizer,'final',step,training_seconds,out)
    torch.save(dict(model=model.state_dict(),optimizer=optimizer.state_dict(),config=asdict(config),step=step,
        matrix_optimizer=matrix_optimizer.state_dict() if matrix_optimizer else None,
        numpy_rng=rng.bit_generator.state,torch_rng=torch.get_rng_state(),
        sampler_state=sampler.state() if sampler else None,
        cuda_rng=torch.cuda.get_rng_state() if device=='cuda' else None),out/'final.pt')
    if final['dev']['loss_nats']<best_loss:
        best_loss=final['dev']['loss_nats'];best_step=step;torch.save(model.state_dict(),out/'best.pt')
    model.load_state_dict(torch.load(out/'best.pt',map_location=device,weights_only=True))
    selected={s:evaluate('selected_'+s,s) for s in ('train','dev','test')}
    selected_samples=samples('samples_selected')
    if checkpoint_hook:checkpoint_hook(model,tokenizer,'selected',best_step,training_seconds,out)
    secondary_count=0 if extra is None else (batch_size if sampling_mode=='openings' else int(batch_size*mixture_fraction))
    secondary_tokens=step*config.context*secondary_count
    exposures={'primary':dict(corpus=data_dir.name,tokens=tokens_seen-secondary_tokens,ratio=(tokens_seen-secondary_tokens)/len(arrays['train']))}
    if extra is not None:exposures['mixture']=dict(corpus=extra_dir.name,tokens=secondary_tokens,ratio=secondary_tokens/len(extra))
    source_label=metadata.get('source_label','Polish Wikipedia20260901, original main-namespace wikitext including redirects')
    if extra is not None:source_label+='; mixed with '+extra_meta.get('source_label',extra_dir.name)
    result=dict(model=f'ScratchGPT-{size}',initialization=('Continued pretraining; optimizer reset; ' if initial_checkpoint else 'Random model weights; ')+metadata.get('tokenizer_origin','Wiki8k BPE tokenizer'),config=asdict(config),
        initial_checkpoint_run=initial_checkpoint.parent.name if initial_checkpoint else None,
        initial_checkpoint_file=initial_checkpoint.name if initial_checkpoint else None,
        environment=dict(torch=torch.__version__,numpy=np.__version__,tokenizers=importlib.metadata.version('tokenizers'),
                         device=torch.cuda.get_device_name() if device=='cuda' else 'CPU',precision='BF16 autocast with FP32 weights' if device=='cuda' else 'FP32'),
        parameters=parameters,seed=seed,source=source_label,source_exposures=exposures,sampler_state=sampler.state() if sampler else None,
        optimizer_kind=optimizer_kind,muon_adjust_lr='match_rms_adamw' if matrix_optimizer else None,
        data=metadata,generation_prompts=generation_prompts,before=before,final=final,selected=selected,best_step=best_step,steps=step,
        tokens_seen=tokens_seen,training_pool_tokens=len(arrays['train']),
        exposure_ratio=tokens_seen/len(arrays['train']),sampling=sampling_mode,mixture_dir=Path(mixture_dir).name if mixture_dir else None,mixture_fraction=secondary_count/batch_size,
        compile_training=compile_training,batch_size=batch_size,peak_lr=peak_lr,warmup_steps=warmup_steps,eval_context=eval_context,eval_interval=eval_interval,training_seconds=training_seconds,training_compute_seconds=training_compute,
        tokens_per_training_compute_second=tokens_seen/training_compute,
        peak_vram_gb=torch.cuda.max_memory_allocated()/1e9 if device=='cuda' else None,
        total_seconds=time.monotonic()-started)
    save(out/'result.json',result);save(out/'history.json',history);save(out/'checkpoints.json',checkpoints)
    (out/'tokenizer.json').write_bytes((data_dir/'tokenizer.json').read_bytes())
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data',default=Path(__file__).resolve().parents[1] / 'datasets/local/wiki-scratch-v1')
    p.add_argument('--output',default=Path(__file__).resolve().parents[1] / 'runs/scratch-local')
    p.add_argument('--size',choices=['10m','30m','100m','300m'],default='10m')
    p.add_argument('--max-seconds',type=int,default=300)
    p.add_argument('--seed',type=int,default=42)
    p.add_argument('--batch-size',type=int,default=32)
    p.add_argument('--device',choices=['cpu','cuda'],default='cpu')
    p.add_argument('--context',type=int,default=256,choices=[256,512,1024])
    p.add_argument('--eval-interval',type=int,default=60)
    p.add_argument('--peak-lr',type=float,default=6e-4)
    p.add_argument('--warmup-steps',type=int,default=20)
    p.add_argument('--compile-training',action='store_true')
    a=p.parse_args();run(a.data,a.output,a.size,a.max_seconds,a.seed,a.device,a.batch_size,a.context,a.eval_interval,a.peak_lr,a.warmup_steps,compile_training=a.compile_training)
