"""Fixed common-corpus and instruction diagnostics for a saved scratch checkpoint."""
import hashlib
import json
from pathlib import Path
import time

# Frozen before examining the longer general-instruction runs. Not a benchmark;
# these elementary facts and tasks may be represented in training data.
PROBES=[
    ('capital','Jak nazywa się stolica Polski? Odpowiedz jednym słowem.','warszawa'),
    ('reading','Przeczytaj tekst: Ola mieszka w Gdańsku, a Jan mieszka w Poznaniu. W jakim mieście mieszka Ola?','gdańsk'),
    ('copy','Napisz dokładnie: Dzień dobry!','dzień dobry'),
    ('addition','Podaj wynik: 2 + 3. Odpowiedz tylko liczbą.','5'),
    ('uppercase','Zamień na wielkie litery: kot.','KOT'),
    ('animal','Jakie zwierzę występuje w zdaniu: Mały pies śpi pod stołem? Odpowiedz jednym słowem.','pies'),
    ('subtraction','Ania miała siedem jabłek. Oddała dwa jabłka bratu. Ile jabłek jej zostało? Odpowiedz tylko liczbą.','5'),
    ('cities','Podaj trzy przykłady polskich miast.',None),
    ('email','Napisz krótki uprzejmy e-mail z prośbą o przesunięcie spotkania na jutro.',None),
    ('explanation','Wyjaśnij dziecku w dwóch zdaniach, dlaczego warto czytać książki.',None),
]

def run(base,output,corpora):
    import torch
    from tokenizers import Tokenizer
    from scratch_model import ScratchGPT,Config
    from scratch_quality import evaluate_fixed_pool,evaluate_quality,FACT_PROBES,FREE_PROMPTS
    start=time.monotonic();torch.set_num_threads(2)
    base=Path(base);out=Path(output);out.mkdir(parents=True,exist_ok=False)
    meta=json.loads((base/'result.json').read_text());model=ScratchGPT(Config(**meta['config'])).cuda()
    model.load_state_dict(torch.load(base/'best.pt',map_location='cuda',weights_only=True));model.eval()
    tok=Tokenizer.from_file(str(base/'tokenizer.json'));eod=tok.token_to_id('<|endoftext|>')
    token_hash=hashlib.sha256((base/'tokenizer.json').read_bytes()).hexdigest();common={}
    for corpus in corpora:
        metrics=evaluate_fixed_pool(model,'cuda','/persist/datasets/'+corpus)
        if metrics['tokenizer_sha256']!=token_hash:raise ValueError('Tokenizers differ')
        common[corpus]=metrics
    quality=evaluate_quality(model,tok,'cuda',out/'quality_raw.json')
    plain=evaluate_quality(model,tok,'cuda',out/'quality_plain.json',
        fact_probes=[dict(p,prompt=p['prompt'].replace("'''",'')) for p in FACT_PROBES],
        free_prompts=[p.replace("'''",'') for p in FREE_PROMPTS[:6]])
    answers=[]
    for key,prompt,reference in PROBES:
        ids=torch.tensor([tok.encode('Pytanie: '+prompt+'\nOdpowiedź:\n').ids],device='cuda');output_ids=[]
        with torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16):
            for _ in range(160):
                token=int(model(ids[:,-model.config.context:])[0].argmax())
                if token==eod:break
                output_ids.append(token);ids=torch.cat([ids,torch.tensor([[token]],device='cuda')],1)
        text=tok.decode(output_ids)
        answers.append(dict(id=key,prompt=prompt,text=text,reference=reference,terminated=token==eod,tokens=len(output_ids)))
    result=dict(base_run=base.name,base_task=meta.get('task','pretraining'),config=meta['config'],
        common=common,quality_raw=dict(correct=quality['factual_correct'],n=quality['factual_total']),
        quality_plain=dict(correct=plain['factual_correct'],n=plain['factual_total']),instruction_probes=answers,
        decoding='Greedy, <=160 tokens, stop at EOD; fixed Polish question/answer prefix',
        limitations='Small illustrative probes, not held-out knowledge or instruction benchmark. Reference strings are shown for manual inspection, not used to optimize or select checkpoints.',
        seconds=time.monotonic()-start)
    (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));return result
