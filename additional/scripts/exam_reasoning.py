# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""RLVR with sampled reasoning; only the final driving-exam letter earns reward."""
import argparse
import json
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from prawko import question
from rlvr_showcase import run as rlvr

def check_exam(task,row,text):
    # Never reward a letter merely mentioned in the body of the reasoning.
    final=text.rsplit('</think>',1)[-1].strip()
    match=re.search(r'(?:^|\n)(?:Odpowiedź:\s*)?([ABC])[.!]?\s*$',final,re.I)
    prediction=match.group(1).upper() if match else None
    correct=prediction==row['answer']
    return dict(reward=float(correct),success=correct,prediction=prediction,valid_answer=prediction is not None)

def run(out,model='qwen3.5-0.8b',seconds=600,lr=1e-5,token_limit=192,thinking=False):
    original=json.loads((ROOT/'datasets/prawko-v2/data.json').read_text())
    data={split:[dict(id=r['id'],prompt=question(r)[0].replace('Odpowiedz wyłącznie literą A, B albo C.',
           'Wyjaśnij wybór w jednym krótkim zdaniu. Zakończ osobnym wierszem: Odpowiedź: A, Odpowiedź: B albo Odpowiedź: C.'),
           answer='ABC'[r['answer']]) for r in rows] for split,rows in original.items()}
    return rlvr(out,task='driving_reasoning',model_key=model,max_seconds=seconds,steps=100,
                lr=lr,beta=.001,dev_interval=20,dataset=data,verifier=check_exam,thinking=thinking,
                token_limit=token_limit,evaluation_batch_size=4,
                training_description='100 official driving questions; sampled reasoning; final-letter reward only. No reasoning targets or SFT.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True)
    p.add_argument('--model',default='qwen3.5-0.8b');p.add_argument('--seconds',type=int,default=600)
    a=p.parse_args();run(a.output,a.model,a.seconds)
