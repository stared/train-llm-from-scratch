# /// script
# requires-python = ">=3.12,<3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Exercise the full trainer path with a tiny model and accelerated clock."""
import hashlib
import itertools
import json
from pathlib import Path
import tempfile
import os
from unittest.mock import patch
import numpy as np
import torch
from tokenizers import Tokenizer
import train_scratch
from scratch_model import Config,ScratchGPT,config_for

torch.set_num_threads(2)
with torch.device('meta'):
    large=ScratchGPT(config_for('100m'))
    print('100m actual parameters:',sum(p.numel() for p in large.parameters()))
with tempfile.TemporaryDirectory(dir='data') as temp:
    root=Path(temp);data=root/'data';data.mkdir()
    raw=Path('data/wiki-scratch-v1/tokenizer.json').read_bytes();(data/'tokenizer.json').write_bytes(raw)
    tok=Tokenizer.from_file(str(data/'tokenizer.json'))
    arr=np.asarray(tok.encode('Warszawa jest stolicą Polski. '*200).ids,dtype='<u2')
    splits={}
    for split in ('train','dev','test'):
        blob=arr.tobytes();(data/f'{split}.bin').write_bytes(blob)
        splits[split]=dict(tokens=len(arr),sha256=hashlib.sha256(blob).hexdigest())
    (data/'tokens.json').write_text(json.dumps(dict(vocab_size=tok.get_vocab_size(),tokenizer_sha256=hashlib.sha256(raw).hexdigest(),splits=splits,eod_id=0)))
    clock=itertools.count(0,2);events=[]
    def hook(model,tok,stage,step,elapsed,out):events.append(stage)
    with patch.object(train_scratch,'config_for',lambda *args:Config(width=32,layers=1,heads=2,hidden=64)),patch.object(train_scratch.time,'monotonic',lambda:next(clock)):
        result=train_scratch.run(data,root/'run',max_seconds=60,device='cpu',batch_size=8,context_length=512,eval_interval=60,checkpoint_hook=hook,sampling_mode=os.environ.get('SCRATCH_TEST_SAMPLING','uniform'),mixture_dir=data)
    assert result['steps']>0
    assert result['tokens_seen']==result['steps']*8*512
    assert result['selected']['test']['tokens']==16384
    assert events[0]=='before' and events[-1]=='selected'
    assert (root/'run/final.pt').exists()
    print('Full trainer passed:',result['steps'],'updates,512 training context,256 evaluation context, hooks and checkpoints.')
