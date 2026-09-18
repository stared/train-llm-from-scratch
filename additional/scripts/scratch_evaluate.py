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
    ('wiki_training_form_warsaw','Opisz: Warszawa.',None),
    ('wiki_training_form_mickiewicz','Opisz: Adam Mickiewicz.',None),
    ('wiki_training_form_poland','Wyjaśnij hasło: Polska.',None),
    ('wiki_form_krakow','Opisz: Kraków.',None),
    ('wiki_new_wording_warsaw','Czym jest Warszawa? Odpowiedz krótko.',None),
    ('wiki_new_wording_mickiewicz','Kim był Adam Mickiewicz?',None),
    ('wiki_new_wording_poland','W jakiej części Europy znajduje się Polska?',None),
    ('wiki_new_wording_krakow','Co wiesz o Krakowie?',None),
]

def run(base,output,corpora,checkpoint='best.pt',extended=False,known_fact_probes=None,known_fact_training_data=None):
    import torch
    from tokenizers import Tokenizer
    from scratch_model import ScratchGPT,Config
    from scratch_quality import evaluate_fixed_pool,evaluate_quality,FACT_PROBES,FREE_PROMPTS
    start=time.monotonic();torch.set_num_threads(2)
    base=Path(base);out=Path(output);out.mkdir(parents=True,exist_ok=False)
    meta=json.loads((base/'result.json').read_text());model=ScratchGPT(Config(**meta['config'])).cuda()
    saved=torch.load(base/checkpoint,map_location='cpu',weights_only=True)
    model.load_state_dict(saved.get('model',saved));del saved
    model.eval()  # Pretraining final.pt also contains optimizer/RNG state; evaluate only its weights.
    tok=Tokenizer.from_file(str(base/'tokenizer.json'));eod=tok.token_to_id('<|endoftext|>')
    token_hash=hashlib.sha256((base/'tokenizer.json').read_bytes()).hexdigest();common={}
    for corpus in corpora:
        metrics=evaluate_fixed_pool(model,'cuda','/persist/datasets/'+corpus)
        if metrics['tokenizer_sha256']!=token_hash:raise ValueError('Tokenizers differ')
        common[corpus]=metrics
    extended_common={}
    if extended:
        for corpus in corpora:
            metrics=evaluate_fixed_pool(model,'cuda','/persist/datasets/'+corpus,batch_count=128,batch_size=32,seed=20260918)
            if metrics['tokenizer_sha256']!=token_hash:raise ValueError('Tokenizers differ')
            extended_common[corpus]=metrics
    quality=evaluate_quality(model,tok,'cuda',out/'quality_raw.json')
    plain=evaluate_quality(model,tok,'cuda',out/'quality_plain.json',
        fact_probes=[dict(p,prompt=p['prompt'].replace("'''",'')) for p in FACT_PROBES],
        free_prompts=[p.replace("'''",'') for p in FREE_PROMPTS[:6]])
    continuations=[]
    for name in ['Warszawa','Kraków','Polska','Adam Mickiewicz']:
        for prefix in [name, "'''"+name+"'''"]:
            for document_start in [False,True]:
                for temperature in [0,.8]:
                    ids=torch.tensor([([eod] if document_start else [])+tok.encode(prefix).ids],device='cuda');generated=[]
                    with torch.random.fork_rng(devices=[torch.cuda.current_device()]),torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16):
                        torch.manual_seed(20260908)
                        for _ in range(96):
                            logits=model(ids[:,-model.config.context:])[0]
                            if temperature==0:token=int(logits.argmax())
                            else:
                                logits=logits/temperature;threshold=logits.topk(50).values[-1]
                                token=int(torch.multinomial(logits.masked_fill(logits<threshold,-float('inf')).softmax(-1),1))
                            if token==eod:break
                            generated.append(token);ids=torch.cat([ids,torch.tensor([[token]],device='cuda')],1)
                    continuations.append(dict(prompt=prefix,document_start=document_start,temperature=temperature,top_k=50 if temperature else None,
                        seed=20260908,text=tok.decode(generated),tokens=len(generated),terminated=token==eod))
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
    known_scores={}
    if known_fact_probes:
        raw=Path(known_fact_probes).read_bytes();probes=json.loads(raw);records={}
        training_hash=None
        if known_fact_training_data:
            training_raw=Path(known_fact_training_data).read_bytes()
            training_hash=hashlib.sha256(training_raw).hexdigest()
            originals={r['id']:r for r in json.loads(training_raw)['train']}
            for rows in probes.values():
                for row in rows:
                    original=originals[row['id'].split(':known-')[0]]
                    assert original['answer']==row['answer']
                    row['prompt']=original['prompt']
        normalize=lambda s:' '.join(s.casefold().split()).strip(' .!?,;:')
        for split,rows in probes.items():
            records[split]=[]
            for row in rows:
                ids=torch.tensor([tok.encode('Pytanie: '+row['prompt']+'\nOdpowiedź:\n').ids],device='cuda');generated=[]
                with torch.no_grad(),torch.autocast('cuda',dtype=torch.bfloat16):
                    for _ in range(64):
                        token=int(model(ids[:,-model.config.context:])[0].argmax())
                        if token==eod:break
                        generated.append(token);ids=torch.cat([ids,torch.tensor([[token]],device='cuda')],1)
                text=tok.decode(generated)
                records[split].append(dict(**row,text=text,exact=normalize(text)==normalize(row['answer']),tokens=len(generated),terminated=token==eod))
            correct=sum(r['exact'] for r in records[split]);known_scores[split]=dict(correct=correct,n=len(rows),accuracy=correct/len(rows))
        condition='original training prompts' if known_fact_training_data else 'unseen prompt templates'
        known_scores.update(probes_sha256=hashlib.sha256(raw).hexdigest(),training_data_sha256=training_hash,prompt_condition=condition,
            meaning=f'Known training facts, {condition}; exact normalized answer matching, not an unseen-knowledge benchmark')
        (out/'known_facts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    result=dict(base_run=base.name,base_task=meta.get('task','pretraining'),checkpoint=checkpoint,config=meta['config'],known_fact_recall=known_scores,
        common=common,extended_common=extended_common,continuation_decoding=continuations,quality_raw=dict(correct=quality['factual_correct'],n=quality['factual_total']),
        quality_plain=dict(correct=plain['factual_correct'],n=plain['factual_total']),instruction_probes=answers,
        decoding='Greedy, <=160 tokens, stop at EOD; fixed Polish question/answer prefix',
        limitations='Small illustrative probes, not held-out knowledge or instruction benchmark. Reference strings are shown for manual inspection, not used to optimize or select checkpoints.',
        seconds=time.monotonic()-start)
    (out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));return result
