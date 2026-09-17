# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Audit saved scratch post-training metrics and development-based selection."""
import argparse
import json
import math
from pathlib import Path


def verify(folder):
    folder=Path(folder)
    read=lambda name:json.loads((folder/name).read_text())
    r=read('execution.json');data=read('data.json')
    ids=[row['id'] for rows in data.values() for row in rows]
    assert len(ids)==len(set(ids))
    def exam_metric(filename,split,rotated=False):
        rows=read(filename);source=data[split]
        assert [row['id'] for row in rows]==[row['id'] for row in source]
        order=(1,2,0) if rotated else (0,1,2)
        for row,original in zip(rows,source):
            assert row['question']==original['question']
            assert row['options']==[original['options'][i] for i in order]
            assert row['answer']=='ABC'[order.index(original['answer'])]
            assert row['prediction']=='ABC'[max(range(3),key=lambda i:row['probabilities'][i])]
            assert row['correct']==(row['answer']==row['prediction'])
            assert all(0<=v<=1 for v in row['probabilities'])
            # Scratch evaluations use bf16 probabilities; summation can round.
            assert abs(sum(row['probabilities'])-1)<.015
        return dict(n=len(rows),correct=sum(row['correct'] for row in rows),
            accuracy=sum(row['correct'] for row in rows)/len(rows),
            correct_probability=sum(row['probabilities']['ABC'.index(row['answer'])] for row in rows)/len(rows))
    def compare(actual,recorded):
        assert actual.keys()==recorded.keys()
        assert all(abs(actual[k]-recorded[k])<1e-8 for k in actual)
    if r['task']=='exam':
        for split,metric in r['before'].items():
            compare(exam_metric('before_'+split+'.json',split.replace('_rotated',''),split.endswith('rotated')),metric)
    for stage in r['stages']:
        method=stage['method'];history=read(method+'_history.json')
        assert all(math.isfinite(h['training_loss']) for h in history)
        if r['task']=='exam':
            for split,metric in stage['after'].items():
                compare(exam_metric(method+'_after_'+split+'.json',split.replace('_rotated',''),split.endswith('rotated')),metric)
            candidates=[(0,exam_metric(method+'_dev_initial.json','dev'))]
            for h in history:
                metric=exam_metric(f"{method}_dev_{h['step']}.json",'dev');compare(metric,h['dev'])
                candidates.append((h['step'],metric))
            candidates.append((stage['steps'],exam_metric(method+'_final_dev.json','dev')))
            best=max(candidates,key=lambda item:(item[1]['correct'],item[1]['correct_probability']))
            assert best[0]==stage['selected_step'];compare(best[1],stage['after']['dev'])
        else:
            assert math.isfinite(stage['after']['test']['loss'])
            assert stage['after']['dev']['loss']<=min(h['dev']['loss'] for h in history)+1e-8
            before=read('samples_before.json');after=read(method+'_samples_after.json')
            assert [x['id'] for x in before]==[x['id'] for x in after]
            for a,b in zip(before,after):
                assert a['prompt']==b['prompt'] and a['reference']==b['reference']
                assert 0<=b['tokens']<=192
    if r['task']=='exam':
        assert r['reload_matches']
        saved=read(r['stages'][-1]['method']+'_after_test.json');reload=read('reload.json')
        assert [(x['id'],x['prediction']) for x in saved]==[(x['id'],x['prediction']) for x in reload]
    print('PASS',folder.name,r['task'])
    return dict(split_ids_disjoint=True,exam_metrics_recomputed=r['task']=='exam',
        development_selection_checked=True,
        limitations='No new inference. Text losses cannot be recomputed without model weights; RLVR sampled actions were not persisted by this research runner.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('runs',nargs='+')
    for run in parser.parse_args().runs:verify(run)
