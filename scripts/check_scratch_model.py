# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "tokenizers==0.23.2", "numpy==2.5.3"]
# ///
"""Fast CPU checks before spending on fresh-model training."""
import tempfile
import json
from pathlib import Path
import unittest
import torch
from scratch_model import ScratchGPT,Config,config_for,Attention

torch.set_num_threads(2)


class ScratchModelChecks(unittest.TestCase):
    def test_shuffled_windows_cover_each_pass_without_replacement(self):
        import numpy as np
        from train_scratch import ShuffledWindows
        sampler=ShuffledWindows(193,8,7)
        starts=np.concatenate([sampler.next(9),sampler.next(31)])
        self.assertEqual(sorted(starts[:24].tolist()),list(range(0,192,8)))
        self.assertEqual(len(set(starts[24:].tolist())),16)
        self.assertTrue(np.all(starts+8<193))
        self.assertEqual(starts.tolist(),ShuffledWindows(193,8,7).next(40).tolist())
        self.assertEqual(sampler.state()['draws'],40)

    def test_full_tokenization_keeps_original_markup(self):
        import numpy as np
        from tokenizers import Tokenizer
        from prepare_wiki_scratch import tokenize
        text="'''Żółć''' [[Polska|PL]] {{Infobox|x=1}}\n<ref>A &amp; B</ref>\n{|\n| Łódź\n|}\n"
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)
            (path/'extraction.json').write_text('{}')
            row=json.dumps(dict(id='fixture',text=text),ensure_ascii=False)+'\n'
            for name in ('train','dev','test','tokenizer_sample'):
                (path/f'{name}.jsonl').write_text(row)
            tokenize(path)
            tok=Tokenizer.from_file(str(path/'tokenizer.json'))
            ids=np.fromfile(path/'test.bin',dtype='<u2').tolist()
            self.assertEqual(tok.decode(ids[:-1],skip_special_tokens=False),text)
            self.assertEqual(ids[-1],tok.token_to_id('<|endoftext|>'))

    def test_training_loop_emits_progress(self):
        # Exercise the real loop beyond update 25 without a minute-long test.
        import hashlib
        import itertools
        import numpy as np
        from tokenizers import Tokenizer, models
        from unittest.mock import patch
        from train_scratch import run
        with tempfile.TemporaryDirectory() as temp:
            data=Path(temp)/'data';data.mkdir()
            tok=Tokenizer(models.WordLevel({'[UNK]':0,'a':1,'b':2,'<|endoftext|>':3},unk_token='[UNK]'))
            tok.save(str(data/'tokenizer.json'))
            splits={}
            for split in ('train','dev','test'):
                array=np.tile(np.array([1,2,1,2,3],dtype='<u2'),300)
                array.tofile(data/f'{split}.bin')
                splits[split]=dict(tokens=len(array),sha256=hashlib.sha256(array.tobytes()).hexdigest())
            (data/'tokens.json').write_text(json.dumps(dict(vocab_size=4,splits=splits,
                tokenizer_sha256=hashlib.sha256((data/'tokenizer.json').read_bytes()).hexdigest(),generation_prompts=['a'])))
            events=[]
            with patch('train_scratch.time.monotonic',side_effect=itertools.count(0,2)), \
                 patch('train_scratch.config_for',return_value=Config(vocab_size=4,width=16,layers=1,heads=2,hidden=32,context=256)), \
                 patch.object(ScratchGPT,'generate',lambda self,ids,new_tokens:ids):
                result=run(data,Path(temp)/'run',max_seconds=600,device='cpu',batch_size=8,eval_interval=600,
                           progress=lambda *event:events.append(event))
            self.assertGreaterEqual(result['steps'],25)
            self.assertTrue(any(e[0]=='Training loss' and e[1]==25 for e in events))
            self.assertEqual(events[0][0],'Development loss')
            self.assertEqual(events[-1][0],'Development loss')
            with patch('train_scratch.time.monotonic',side_effect=itertools.count(0,2)), \
                 patch('train_scratch.config_for',return_value=Config(vocab_size=4,width=16,layers=1,heads=2,hidden=32,context=256)), \
                 patch.object(ScratchGPT,'generate',lambda self,ids,new_tokens:ids):
                continued=run(data,Path(temp)/'continued',max_seconds=60,device='cpu',batch_size=8,
                              initial_checkpoint=Path(temp)/'run/best.pt',sampling_mode='shuffled')
            self.assertEqual(continued['before']['test'],result['selected']['test'])
            self.assertEqual(continued['initial_checkpoint_run'],'run')
            self.assertEqual(continued['sampler_state']['draws'],continued['steps']*8)
            from scratch_quality import evaluate_fixed_pool
            loaded=ScratchGPT(Config(**result['config']))
            loaded.load_state_dict(torch.load(Path(temp)/'run/best.pt',weights_only=True))
            original_pool=evaluate_fixed_pool(loaded,'cpu',data)
            self.assertEqual(original_pool['test'],result['selected']['test'])
            other_pool=evaluate_fixed_pool(loaded,'cpu',data,batch_count=2,batch_size=4,seed=17)
            self.assertEqual(other_pool['test']['tokens'],2048)
            self.assertTrue(loaded.training)
            self.assertEqual(other_pool,evaluate_fixed_pool(loaded,'cpu',data,batch_count=2,batch_size=4,seed=17))
            mixture=Path(temp)/'mixture';mixture.mkdir()
            (mixture/'tokenizer.json').write_bytes((data/'tokenizer.json').read_bytes())
            meta=json.loads((data/'tokens.json').read_text())
            for split in ('train','dev','test'):
                values=np.full(1500,2,dtype='<u2');values.tofile(mixture/f'{split}.bin')
                meta['splits'][split]=dict(tokens=len(values),sha256=hashlib.sha256(values.tobytes()).hexdigest())
            (mixture/'tokens.json').write_text(json.dumps(meta))
            batches=[];original_forward=ScratchGPT.forward
            def inspect_forward(model,ids,targets=None,positions=None):
                if model.training and targets is not None:batches.append(ids.clone())
                return original_forward(model,ids,targets,positions)
            with patch('train_scratch.time.monotonic',side_effect=itertools.count(0,2)), \
                 patch('train_scratch.config_for',return_value=Config(vocab_size=4,width=16,layers=1,heads=2,hidden=32,context=256)), \
                 patch.object(ScratchGPT,'generate',lambda self,ids,new_tokens:ids), \
                 patch.object(ScratchGPT,'forward',inspect_forward):
                mixed=run(data,Path(temp)/'mixed',max_seconds=60,device='cpu',batch_size=8,
                          sampling_mode='mixed-uniform',mixture_dir=mixture,mixture_fraction=.25)
            self.assertTrue(batches)
            for batch in batches:
                self.assertTrue(torch.all(batch[:2]==2))
                self.assertFalse(torch.all(batch[2:]==2))
            self.assertEqual(mixed['source_exposures']['primary']['tokens'],mixed['tokens_seen']*3//4)
            self.assertEqual(mixed['source_exposures']['mixture']['tokens'],mixed['tokens_seen']//4)
            self.assertEqual(mixed['mixture_fraction'],.25)
            with patch('train_scratch.time.monotonic',side_effect=itertools.count(0,2)), \
                 patch('train_scratch.config_for',return_value=Config(vocab_size=4,width=16,layers=1,heads=2,hidden=32,context=256)), \
                 patch.object(ScratchGPT,'generate',lambda self,ids,new_tokens:ids):
                muon=run(data,Path(temp)/'muon',max_seconds=60,device='cpu',batch_size=8,optimizer_kind='muon')
            self.assertLess(muon['final']['train']['loss_nats'],muon['before']['train']['loss_nats'])
            saved=torch.load(Path(temp)/'muon/final.pt',weights_only=True)
            self.assertEqual(len(saved['optimizer']['state']),4)  # Embedding and three RMS norms.
            self.assertEqual(len(saved['matrix_optimizer']['state']),5)  # Attention and feed-forward matrices.

    def test_parameter_counts(self):
        for size,expected in [('10m',10244160),('30m',29893120)]:
            model=ScratchGPT(config_for(size))
            self.assertEqual(sum(p.numel() for p in model.parameters()),expected)

    def test_attention_cannot_read_future(self):
        torch.manual_seed(7)
        attention=Attention(Config(width=32,heads=2,context=16))
        x=torch.randn(2,16,32);changed=x.clone();changed[:,8:]=torch.randn(2,8,32)*100
        torch.testing.assert_close(attention(x)[:,:8],attention(changed)[:,:8],atol=1e-6,rtol=1e-6)

    def test_right_padded_batch_matches_individual_logits_and_gradients(self):
        torch.manual_seed(11)
        c=Config(vocab_size=32,width=16,layers=2,heads=2,hidden=32,context=16)
        model=ScratchGPT(c)
        rows=[torch.randint(0,32,(1,n)) for n in (3,7,11)]
        individual=torch.cat([model(row) for row in rows])
        batch=torch.zeros(3,16,dtype=torch.long)
        for i,row in enumerate(rows):batch[i,:row.shape[1]]=row[0]
        positions=torch.tensor([row.shape[1]-1 for row in rows])
        batched=model(batch,positions=positions)
        torch.testing.assert_close(batched,individual,atol=1e-6,rtol=1e-5)
        targets=torch.tensor([1,2,3])
        torch.nn.functional.cross_entropy(individual,targets).backward()
        expected=[p.grad.clone() for p in model.parameters()]
        model.zero_grad()
        torch.nn.functional.cross_entropy(model(batch,positions=positions),targets).backward()
        for p,grad in zip(model.parameters(),expected):
            torch.testing.assert_close(p.grad,grad,atol=2e-6,rtol=2e-5)

    def test_learns_and_reloads(self):
        torch.manual_seed(8)
        c=Config(vocab_size=64,width=32,layers=2,heads=2,hidden=64,context=16)
        model=ScratchGPT(c)
        x=torch.randint(0,64,(4,16));y=(x+1)%64
        optimizer=torch.optim.AdamW(model.parameters(),lr=.01)
        before=model(x,y).item()
        for _ in range(30):
            optimizer.zero_grad();loss=model(x,y);loss.backward();optimizer.step()
        self.assertLess(model(x,y).item(),before/2)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'model.pt';torch.save(model.state_dict(),p)
            reloaded=ScratchGPT(c);reloaded.load_state_dict(torch.load(p,weights_only=True))
            torch.testing.assert_close(model(x),reloaded(x))


if __name__=='__main__':unittest.main(verbosity=2)
