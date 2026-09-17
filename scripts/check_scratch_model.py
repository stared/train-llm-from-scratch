# /// script
# requires-python = ">=3.12,<3.14"
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

    def test_parameter_counts(self):
        for size,expected in [('10m',10244160),('30m',29893120)]:
            model=ScratchGPT(config_for(size))
            self.assertEqual(sum(p.numel() for p in model.parameters()),expected)

    def test_attention_cannot_read_future(self):
        torch.manual_seed(7)
        attention=Attention(Config(width=32,heads=2,context=16))
        x=torch.randn(2,16,32);changed=x.clone();changed[:,8:]=torch.randn(2,8,32)*100
        torch.testing.assert_close(attention(x)[:,:8],attention(changed)[:,:8],atol=1e-6,rtol=1e-6)

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
