# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Independently audit saved prawko metrics, training isolation and RLVR rewards."""
import argparse
import hashlib
import json
import math
from pathlib import Path


def verify(path):
    path = Path(path)
    read = lambda name: json.loads((path/name).read_text())
    result = read('execution.json' if (path/'execution.json').exists() else 'result.json')
    data = read('data.json')
    assert hashlib.sha256((path/'data.json').read_bytes()).hexdigest() == result['data_sha256']
    ids = [r['id'] for rows in data.values() for r in rows]
    assert len(ids) == len(set(ids))
    phases = ['before'] + (['after'] if 'after' in result else []) + (['final'] if 'final' in result else [])
    for phase in phases:
        for split in ('train', 'dev', 'test', 'test_rotated'):
            rows = read(f'{phase}_{split}.json')
            source = data[split.replace('_rotated', '')]
            assert [r['id'] for r in rows] == [r['id'] for r in source]
            for row, original in zip(rows, source):
                order = (1, 2, 0) if split.endswith('rotated') else (0, 1, 2)
                assert row['answer'] == 'ABC'[order.index(original['answer'])]
                assert row['question'] == original['question']
                assert row['options'] == [original['options'][i] for i in order]
                assert row['correct'] == (row['answer'] == row['prediction'])
                assert row['prediction'] == 'ABC'[max(range(3), key=lambda i: row['probabilities'][i])]
                assert all(0 <= p <= 1 for p in row['probabilities'])
                assert abs(sum(row['probabilities']) - 1) < 1e-6
            metric = result[phase][split]
            assert len(rows) == metric['n']
            assert sum(r['correct'] for r in rows) == metric['correct']
            assert metric['accuracy'] == metric['correct']/metric['n']
            mean = sum(r['probabilities']['ABC'.index(r['answer'])] for r in rows)/len(rows)
            assert abs(mean-metric['mean_correct_probability']) < 1e-7
    audit = dict(data_hash_matches=True, all_metrics_recomputed=True, split_ids_disjoint=True)
    if 'after' in result:
        lookup = {r['id']: r for r in data['train']}
        history = read('history.json')
        assert result['steps'] == len(history)
        for step in history:
            assert math.isfinite(step['loss']) and math.isfinite(step['gradient_norm'])
            for qid, order, answer in zip(step['ids'], step['orders'], step['answers']):
                assert sorted(order) == [0, 1, 2]
                assert answer == order.index(lookup[qid]['answer'])
            if result['method'] == 'rlvr':
                assert math.isfinite(step['kl']) and step['kl'] >= -1e-5
                for answer, samples, rewards, advantages in zip(step['answers'],step['samples'],step['rewards'],step['advantages']):
                    assert len(samples) == len(rewards) == len(advantages) == 4
                    assert rewards == [float(s == answer) for s in samples]
                    assert all(abs(a-(reward-(sum(rewards)-reward)/3)) < 1e-6 for a,reward in zip(advantages,rewards))
        candidates = [dict(epoch=0,steps=0,**result['before']['dev'])] + read('checkpoints.json')
        selected = max(candidates, key=lambda c: (c['correct'], c['mean_correct_probability']))
        assert result['selected_epoch'] == selected['epoch']
        assert result['selected_steps'] == selected['steps']
        assert result['after']['dev']['correct'] == selected['correct']
        selected_history = history[:selected['steps']]
        before_reload = read('after_test.json')[:8]
        reloaded = read('reload.json')
        assert len(reloaded) == len(before_reload) == 8
        assert [(r['id'],r['prediction']) for r in reloaded] == [(r['id'],r['prediction']) for r in before_reload]
        audit.update(all_training_ids_isolated=True, dev_selection_recomputed=True,
                     reload_predictions_match=True,
                     selected_training_questions=len({i for h in selected_history for i in h['ids']}),
                     selected_presentations=sum(len(h['ids']) for h in selected_history))
        if result['method'] == 'rlvr':
            audit.update(all_sample_rewards_and_advantages_recomputed=True,
                         selected_sampled_actions=audit['selected_presentations']*4)
    (path/'local_verification.json').write_text(json.dumps(audit,indent=2))
    print(path.name, json.dumps(audit))
    return audit


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('runs', nargs='+')
    a = p.parse_args()
    for run in a.runs:
        verify(run)
