# /// script
# requires-python = ">=3.14"
# dependencies = ["torch==2.14.0", "transformers==5.16.1", "peft==0.20.0", "accelerate==1.14.0"]
# ///
"""Probe repetitive openings in a saved dialogue adapter; no training."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))

import argparse
import json
from pathlib import Path

PROMPTS = [
    ('statement', 'Cześć, właśnie wróciłem z pracy.'),
    ('statement', 'Dzisiaj wszystko idzie nie tak.'),
    ('statement', 'Nie wiem, co chcę robić w życiu.'),
    ('statement', 'Kupiłem drogi sweter, a wszyscy się ze mnie śmieją.'),
    ('statement', 'Mój komputer znowu się zawiesił.'),
    ('statement', 'Mam dla ciebie dobrą wiadomość.'),
    ('statement', 'Dobra, jedziemy. Samochód już czeka.'),
    ('statement', 'Stary, chyba trochę przesadziłeś.'),
    ('question', 'Nie wiem, co chcę robić w życiu. Od czego zacząć?'),
    ('question', 'Kupiłem drogi sweter, a wszyscy się ze mnie śmieją. Co robić?'),
    ('question', 'Dlaczego mój komputer znowu się zawiesił?'),
    ('question', 'Co robimy wieczorem?'),
]


def probe(adapter_dir, output, device='cuda'):
    import torch
    from peft import PeftModel
    from style_workshop import setup, generate
    run = Path(adapter_dir)
    spec = json.loads((run / 'style_result.json').read_text())
    tokenizer, stop, load, _ = setup(spec['model'], device)
    model = PeftModel.from_pretrained(load(), run / 'adapter')
    rows = []
    for seed in (42, 123):
        torch.manual_seed(seed)
        for start in range(0, len(PROMPTS), 4):
            batch = PROMPTS[start:start+4]
            answers = generate(model, tokenizer, stop, [p for _, p in batch], device,
                               sample=True, temperature=.7, top_p=.8, top_k=20,
                               repetition_penalty=1.1, max_tokens=96)
            for (kind, prompt), answer in zip(batch, answers):
                rows.append(dict(kind=kind, prompt=prompt, seed=seed, answer=answer,
                                 contains_phrase='zamieniam się w' in answer.casefold(),
                                 starts_with_phrase=answer.strip().casefold().startswith('zamieniam się w')))
    result = dict(model=spec['model_spec'], training_data=spec['teacher'],
                  data_sha256=spec['data_sha256'], adapter_run=run.name, adapter_scale=1.0,
                  evaluation_only=True, batch_size=4,
                  decoding=dict(temperature=.7, top_p=.8, top_k=20, repetition_penalty=1.1,
                                max_new_tokens=96, seeds=[42,123]), rows=rows)
    result['counts'] = {kind: dict(total=sum(r['kind']==kind for r in rows),
                                  contains_phrase=sum(r['kind']==kind and r['contains_phrase'] for r in rows),
                                  starts_with_phrase=sum(r['kind']==kind and r['starts_with_phrase'] for r in rows))
                        for kind in ('statement','question')}
    out = Path(output)
    out.mkdir(parents=True, exist_ok=False)
    (out/'probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--adapter-dir',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--device',default='cuda',choices=['cuda','cpu','mps'])
    a=p.parse_args()
    probe(a.adapter_dir,a.output,a.device)
