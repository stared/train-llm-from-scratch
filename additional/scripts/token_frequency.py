# /// script
# requires-python = ">=3.14"
# dependencies = ["numpy==2.5.3", "tokenizers==0.23.2"]
# ///
"""Count actual training-token occurrences without loading the corpus into RAM."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from tokenizers import Tokenizer


def audit(folder):
    folder=Path(folder)
    meta=json.loads((folder/'tokens.json').read_text())
    tokenizer_bytes=(folder/'tokenizer.json').read_bytes()
    assert hashlib.sha256(tokenizer_bytes).hexdigest()==meta['tokenizer_sha256']
    tok=Tokenizer.from_str(tokenizer_bytes.decode())
    count=np.zeros(tok.get_vocab_size(),dtype=np.int64)
    digest=hashlib.sha256()
    with (folder/'train.bin').open('rb') as file:
        while block:=file.read(32*1024*1024):
            digest.update(block)
            values=np.frombuffer(block,dtype='<u2')
            assert int(values.max())<len(count)
            count+=np.bincount(values,minlength=len(count))
    assert int(count.sum())==meta['splits']['train']['tokens']
    assert digest.hexdigest()==meta['splits']['train']['sha256']
    def rows(ids):
        return [dict(id=int(i),token=tok.id_to_token(int(i)),count=int(count[i])) for i in ids]
    return dict(corpus=folder.name,split='train',tokens=int(count.sum()),vocabulary=len(count),
        tokenizer_sha256=meta['tokenizer_sha256'],train_sha256=digest.hexdigest(),
        zero_count=int((count==0).sum()),
        entries_below={str(n):int((count<n).sum()) for n in (10,100,1000,10000)},
        occurrence_quantiles={str(q):float(np.quantile(count,q)) for q in (0,.01,.1,.5,.9,.99,1)},
        most_frequent=rows(np.argsort(-count)[:20]),least_frequent=rows(np.argsort(count)[:30]),
        note='Counts in the full prepared corpus, not the subset sampled by a particular training run. Token strings use the tokenizer byte alphabet.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('folders',nargs='+',type=Path)
    p.add_argument('--output',required=True,type=Path)
    args=p.parse_args()
    result=[audit(folder) for folder in args.folders]
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for r in result:print(r['corpus'],r['tokens'],'tokens;',r['entries_below'],'entries below these counts')
