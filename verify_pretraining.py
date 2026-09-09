# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Audit completed scratch experiments from saved artifacts, without loading weights.

This checks arithmetic, provenance, recorded selection/reload evidence and quality
metrics. It does not independently rerun neural inference or validate facts in free
text. --require-weights additionally requires local best.pt and final.pt files.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def repetition(text):
    words=re.findall(r'\w+',text.casefold(),flags=re.UNICODE)
    grams=[tuple(words[i:i+4]) for i in range(max(0,len(words)-3))]
    counts=Counter(grams)
    return dict(words=len(words),word_4grams=len(grams),
                repeated_word_4gram_fraction=(len(grams)-len(counts))/len(grams) if grams else 0.,
                most_common_word_4gram_count=max(counts.values(),default=0))


def audit(path,require_weights=False):
    result=read(path/'execution.json');checks=[];errors=[]
    def check(condition,label):
        (checks if condition else errors).append(label)
    def close(a,b,tol=1e-7):
        return isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isfinite(a) and math.isfinite(b) and math.isclose(a,b,rel_tol=tol,abs_tol=tol)
    c=result['config'];w=c['width'];h=c['hidden'];layers=c['layers']
    expected=c['vocab_size']*w+layers*(4*w*w+3*w*h+2*w)+w
    check(result['parameters']==expected,'Parameter count equals tied-embedding/RMSNorm/SwiGLU architecture formula')
    expected_tokens=result['steps']*result['batch_size']*c['context']
    check(result['tokens_seen']==expected_tokens,'Tokens seen equals steps × batch × context')
    check(close(result['exposure_ratio'],result['tokens_seen']/result['training_pool_tokens']),'Exposure ratio arithmetic')
    check(result['training_pool_tokens']==result['data']['splits']['train']['tokens'],'Training pool size matches corpus manifest')
    check(bool(result.get('source')) and 'random' in result.get('initialization','').casefold(),'Explicit source and random-initialization labels')
    if 'source_label' in result['data']:
        check(result['source']==result['data']['source_label'],'Source label equals dataset manifest')
    tokenizer_path=path/'tokenizer.json'
    check(hashlib.sha256(tokenizer_path.read_bytes()).hexdigest()==result['data']['tokenizer_sha256'],'Local tokenizer SHA256 matches dataset manifest')
    tokenizer=read(tokenizer_path)
    check(len(tokenizer['model']['vocab'])==c['vocab_size']==result['data']['vocab_size'],'Tokenizer/config/manifest vocabulary counts agree')
    checkpoints=read(path/'checkpoints.json')
    choices=[(0,result['before']['dev']['loss_nats'])]+[(r['step'],r['loss_nats']) for r in checkpoints]+[(result['steps'],result['final']['dev']['loss_nats'])]
    best_step,best_loss=min(choices,key=lambda row:row[1])
    check(close(result['selected']['dev']['loss_nats'],best_loss),'Selected dev loss is minimum of initialization, periodic and final evaluations')
    check(result['best_step']==best_step,'Best step follows strict improvement with earliest tie')
    for stage in ('before','final','selected'):
        for split,metric in result[stage].items():
            check(math.isfinite(metric['loss_nats']) and metric['loss_nats']>=0 and metric['tokens']>0,f'{stage}/{split}: finite nonnegative loss and positive eval token count')
            metric_path=path/f'{stage}_{split}.json'
            if metric_path.exists():check(read(metric_path)==metric,f'{stage}/{split}: standalone metric equals execution record')
    for row in read(path/'history.json'):
        check(row['tokens_seen']==row['step']*result['batch_size']*c['context'],f"History step{row['step']}: token arithmetic")
    selected_samples=read(path/'samples_selected.json')
    check(read(path/'reload_samples.json')==selected_samples,'Fresh-process reload samples exactly equal selected samples')
    check(result.get('fresh_process_reload_matches') is True,'Execution marks successful fresh-process reload')
    quality_files=sorted(set(path.glob('quality_*.json'))|({path/'quality.json'} if (path/'quality.json').exists() else set()))
    for quality_path in quality_files:
        q=read(quality_path);name=quality_path.name
        check(q['model_parameters']==expected and q['context']==c['context'],f'{name}: model parameters/context match run')
        facts=q['facts'];check(q['factual_total']==len(facts),f'{name}: factual denominator')
        correct=0
        for index,fact in enumerate(facts):
            scores=fact['scores'];values=[r['mean_log_probability'] for r in scores]
            valid=len(scores)==len(fact['candidates']) and all(math.isfinite(v) for v in values)
            check(valid,f'{name}: fact{index} finite score per candidate')
            if not valid:continue
            predicted=max(range(len(values)),key=values.__getitem__)
            check(fact['predicted']==predicted,f'{name}: fact{index} argmax')
            is_correct=predicted==fact['correct'];correct+=is_correct
            check(fact['is_correct']==is_correct,f'{name}: fact{index} correctness')
            for candidate,score in zip(fact['candidates'],scores):
                check(candidate==score['candidate'] and close(score['sum_log_probability'],score['mean_log_probability']*score['tokens']),f'{name}: fact{index} candidate identity and likelihood arithmetic')
        check(q['factual_correct']==correct,f'{name}: factual numerator')
        recomputed=[]
        for index,row in enumerate(q['free_generations']):
            actual=repetition(row['continuation']);recomputed.append(actual['repeated_word_4gram_fraction'])
            check(all(close(row[k],v,tol=1e-12) for k,v in actual.items()),f'{name}: generation{index} word/repetition statistics')
            check(row['generated_tokens']==q['max_new_tokens'],f'{name}: generation{index} declared generation length')
        check(bool(recomputed) and close(q['mean_repeated_word_4gram_fraction'],sum(recomputed)/len(recomputed),tol=1e-12),f'{name}: mean repetition recomputed')
        if result['data'].get('quality_fact_probes')==[] or 'wolne lektury' in result['source'].casefold():
            check(q['factual_total']==0,f'{name}: factual probes disabled for non-Wikipedia corpus')
    common_path=path/'common_wiki_eval.json'
    if common_path.exists():
        common=read(common_path)
        check('Full Wikipedia' in common['source'],'Common Wiki evaluation explicitly labels separate corpus')
        check(common['tokenizer_sha256']==result['data']['tokenizer_sha256'],'Common Wiki evaluation uses matching tokenizer')
        wiki_manifest=ROOT/'data/wiki-scratch-v1/tokens.json'
        if wiki_manifest.exists():check(common['tokenizer_sha256']==read(wiki_manifest)['tokenizer_sha256'],'Common Wiki tokenizer matches local full-corpus manifest')
        for split in ('dev','test'):
            check(common[split]['tokens']==16384 and math.isfinite(common[split]['loss_nats']) and common[split]['loss_nats']>=0,f'Common Wiki {split}: fixed-window schema and finite loss')
    weights={name:(path/name).is_file() and (path/name).stat().st_size>0 for name in ('best.pt','final.pt')}
    if require_weights:
        for name,present in weights.items():check(present,f'Local nonempty {name} exists')
    report=dict(run=path.name,model=result['model'],source=result['source'],tokenizer_origin=result['data'].get('tokenizer_origin','Original Wikipedia-trained BPE'),
        audited_at_utc=datetime.now(timezone.utc).isoformat(),passed=not errors,
        checks_passed=len(checks),checks=checks,errors=errors,local_weights=weights,require_weights=require_weights,
        quality_files=[p.name for p in quality_files],common_wiki_evaluation_present=common_path.exists(),
        limitations=['No weights are deserialized; local existence checks do not prove tensor contents.',
                     'Reload equality verifies recorded fresh-process outputs; this audit does not rerun inference.',
                     'Factual candidate arithmetic is checked, not semantic correctness of generated prose.',
                     'Common Wikipedia metrics are schema/provenance checked, not recomputed.'])
    (path/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs',nargs='*',type=Path)
    p.add_argument('--require-weights',action='store_true')
    a=p.parse_args();paths=a.runs or sorted(x.parent for x in (ROOT/'runs').glob('scratch-*/execution.json'))
    failed=[]
    for path in paths:
        if not (path/'execution.json').exists():
            print('SKIP incomplete',path.name);continue
        try:
            r=audit(path,a.require_weights)
        except (OSError,KeyError,ValueError,TypeError) as exc:
            print('ERROR',path.name,str(exc));failed.append(path.name);continue
        print('PASS' if r['passed'] else 'FAIL',path.name,r['checks_passed'],'checks',r['local_weights'])
        if not r['passed']:
            print(json.dumps(r['errors'],indent=2));failed.append(path.name)
    if failed:raise SystemExit(1)
