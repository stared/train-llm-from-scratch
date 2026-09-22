# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Local, read-only workshop viewer. No model or Modal account required."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import time
from urllib.parse import urlsplit, parse_qs
import webbrowser
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_RUNS = {
    'pretrain': 'scratch-wolne-lektury-30m-1789676785288825614',
    'sft': 'prawko-sft-1789672433144290591',
    'rlvr': 'rlvr-train-six_words-1789672431850535000',
}


def read(path, default=None):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return default


def series(name, rows, x, y):
    return dict(name=name, points=[[r[x], r[y]] for r in rows if x in r and y in r])


def source_data(folder, r):
    data = read(folder/'data.json')
    if data:
        return data
    # Match the recorded data hash before displaying a training example.
    import hashlib
    for p in (ROOT/'datasets/prawko-v2').glob('*.json'):
        if hashlib.sha256(p.read_bytes()).hexdigest() == r.get('data_sha256'):
            return read(p, {})
    return {}


def question(row):
    return row['question']+'\n'+'\n'.join(f'{a}. {b}' for a, b in zip('ABC', row['options']))


def normalize(folder):
    """Only expose curated fields; never serve arbitrary files from a run."""
    r = read(folder/'execution.json') or read(folder/'result.json')
    if not r:
        raise ValueError('Run has no completed result')
    out = dict(id=folder.name, status='Completed', model=r.get('model_spec', {}).get('id', r.get('model', 'ScratchGPT')),
               source=r.get('training_data', r.get('source', '')), snapshots=[], curves=[], training=[], rollouts=[],
               seconds=r.get('training_seconds'), cost=r.get('estimated_compute_usd'), xLabel='Updates')
    def snapshot(file, label, step, split='dev'):
        rows = read(folder/('visualization_'+file+'.json'), [])
        if out.get('exam'):
            rows = read(folder/(file+'.json'), [])
        rows = [row for row in rows if row.get('tokens') or row.get('probabilities')]
        if rows:
            out['snapshots'].append(dict(label=label, step=step, split=split, rows=rows))
    if (folder/'samples_before.json').exists():
        out['stage'] = 'pretrain'
        h, c = read(folder/'history.json', []), read(folder/'checkpoints.json', [])
        out['curves'] = [series('Training loss', h, 'step', 'loss'), series('Development loss',
            [dict(step=0, loss_nats=r['before']['dev']['loss_nats'])]+c+[dict(step=r['steps'],loss_nats=r['final']['dev']['loss_nats'])], 'step', 'loss_nats')]
        snapshot('samples_before', 'Before training', 0, 'fixed prompts')
        for v in c:
            snapshot('samples_step_'+str(v['step']), 'Update '+str(v['step']), v['step'], 'fixed prompts')
        snapshot('samples_final', 'Final checkpoint', r['steps'], 'fixed prompts')
        snapshot('samples_selected', 'Selected checkpoint', r['best_step'], 'fixed prompts')
        out['score'] = dict(label='Test loss', before=r['before']['test']['loss_nats'], after=r['selected']['test']['loss_nats'])
        out['source'] = 'Wolne Lektury' if 'wl-' in str(r.get('data', '')) or 'lektury' in folder.name else r.get('source', 'Polish Wikipedia')
    elif (folder/'rollouts.json').exists():
        out['stage'] = 'rlvr'
        data = source_data(folder, r)
        out['source'] = f"{r.get('task', 'verifiable rewards').replace('_',' ').capitalize()}, {len(data.get('train', []))} training prompts"
        by_id = {v['id']: v for v in data.get('train', [])}
        c = read(folder/'checkpoint_selection.json', {}).get('checkpoints', [])
        final=read(folder/'checkpoint_selection.json', {}).get('final')
        if final and (not c or c[-1]['step']!=r['steps']): c=c+[dict(step=r['steps'],**final)]
        h = read(folder/'rollouts.json', [])
        out['curves'] = [dict(name='Development success', points=[[0, r['before']['dev']['successes']/r['before']['dev']['n']]]+
            [[v['step'], v['successes']/v['n']] for v in c]),
            dict(name='Rollout reward', points=[[v['step']+1, sum(s['reward'] for s in v['scores'])/len(v['scores'])] for v in h])]
        snapshot('before_dev', 'Before training', 0)
        for v in c:
            filename='checkpoint_dev_'+str(v['step'])
            if not (folder/(filename+'.json')).exists() and v['step']==r['steps']:filename='checkpoint_dev_final'
            snapshot(filename, 'Update '+str(v['step']), v['step'])
        snapshot('after_dev', 'Selected checkpoint', r.get('selected_step', read(folder/'checkpoint_selection.json', {}).get('best_step', r['steps'])))
        for v in h[::max(1, len(h)//24)]:
            row = by_id.get(v['ids'][0], {})
            out['rollouts'].append(dict(step=v['step']+1, prompt=row.get('prompt', v['ids'][0]), rows=[
                dict(text=t, **s, advantage=a) for t, s, a in zip(v['texts'][:4], v['scores'][:4], v['advantages'][:4])]))
        out['training'] = [dict(prompt=v['prompt'], target='Reward from the checker; no target answer.') for v in data.get('train', [])[:3]]
        out['score'] = dict(label='Test constraints', before=r['before']['test']['successes'], after=r['after']['test']['successes'], n=r['after']['test']['n'])
    elif (folder/'before_test.json').exists() and r.get('method') in ('sft', 'rlvr'):
        out['stage'] = 'sft' if r['method']=='sft' else 'rlvr'
        out['exam'] = True
        c = read(folder/'checkpoints.json', [])
        out['curves'] = [dict(name='Development accuracy', points=[[0,r['before']['dev']['accuracy']]]+
            [[v['steps'], v['accuracy']] for v in c])]
        snapshot('before_dev', 'Before training', 0)
        for v in c:
            snapshot('dev_epoch_'+str(v['epoch']), 'Epoch '+str(v['epoch']), v['steps'])
        snapshot('after_dev', 'Selected checkpoint', r.get('selected_steps', 0))
        out['score'] = dict(label='Test answers', before=r['before']['test']['correct'], after=r['after']['test']['correct'], n=r['after']['test']['n'])
        data = source_data(folder, r)
        out['source'] = f"{len(data.get('train', []))} Polish Driving Licence Exam questions"
        out['training'] = [dict(prompt=question(v), target='ABC'[v['answer']]) for v in data.get('train', [])[:3]]
        by_id = {v['id']:v for v in data.get('train', [])}
        h = read(folder/'history.json', [])
        for i, v in enumerate(h):
            if 'samples' not in v or i % max(1, len(h)//24): continue
            row = by_id.get(v['ids'][0])
            if row:
                row = {**row, 'options':[row['options'][j] for j in v['orders'][0]]}
                out['rollouts'].append(dict(step=i+1, prompt=question(row), rows=[dict(text='ABC'[a], reward=b, advantage=c)
                    for a,b,c in zip(v['samples'][0],v['rewards'][0],v['advantages'][0])]))
    else:
        raise ValueError('Unsupported run')
    if len(out['snapshots']) < 2:
        raise ValueError('Run needs before/after examples with probabilities')
    key = 'id' if 'id' in out['snapshots'][0]['rows'][0] else 'prompt'
    shared = set.intersection(*(set(row[key] for row in s['rows']) for s in out['snapshots']))
    if not shared:
        raise ValueError('Run needs matching examples across checkpoints')
    # Keep the first fixed, fully traced examples, not selected successes.
    for s in out['snapshots']:
        s['rows'] = [row for row in s['rows'] if row[key] in shared][:8]
    return out


def live(folder):
    r = read(folder/'progress.json', {})
    events = r.get('events', [])
    metrics = [v for v in events if 'series' in v]
    previews = [v for v in events if v.get('kind')=='preview']
    stale = r.get('status')=='Running' and time.time()-r.get('updated_at', 0)>30
    stage = 'rlvr' if r.get('stage')=='exam-rlvr' else r.get('stage')
    metadata = next((v.get('metadata', {}) for v in previews if v.get('metadata')), {})
    result = dict(id=folder.name, stage=stage, status='Disconnected' if stale else r.get('status', 'Starting'),
        model=metadata.get('model', 'Loading model'), source=metadata.get('source', ''),
        exam=r.get('stage') in ('sft','exam-rlvr'), seconds=r.get('elapsed_seconds'), xLabel='Updates',
        curves=[series(n, [v for v in metrics if v['series']==n], 'step', 'value') for n in dict.fromkeys(v['series'] for v in metrics)],
        snapshots=[{**{k:v for k,v in e.items() if k in ('label','step','rows','split')},'label':preview_label(e)} for e in previews if e.get('rows')],
        training=metadata.get('training', []), rollouts=[v['rollout'] for v in previews if v.get('rollout')])
    if r.get('final') and re.fullmatch(r'[A-Za-z0-9_-]+', r['final']):
        try:
            result = {**normalize(ROOT/'runs'/r['final']), 'id':folder.name}
        except (ValueError, KeyError):
            result['status']='Finishing'
    return result


def preview_label(event):
    label=event.get('label','').lower()
    if label.startswith('before'): return 'Before training'
    if label.startswith(('after','selected')): return 'Selected checkpoint'
    if 'final' in label: return 'Final checkpoint'
    if label.startswith('dev epoch'): return label.removeprefix('dev ').capitalize()
    return 'Update '+str(event.get('step',0))


def examples():
    return read(ROOT/'visualization/examples.json', [])


def folders():
    runs = ROOT/'runs'
    patterns = ('live-*','scratch-*','prawko-sft-*','prawko-rlvr-*','rlvr-train-*')
    return sorted({p for pattern in patterns for p in runs.glob(pattern) if p.is_dir() and not p.is_symlink()},
                  key=lambda p:p.stat().st_mtime, reverse=True)


def catalog():
    items = [dict(id='example-'+r['stage'],stage=r['stage'],model=r['model'],status='Completed') for r in examples()]
    recent=folders()[:80]
    linked={read(p/'progress.json',{}).get('final') for p in recent if p.name.startswith('live-')}
    counts={}
    for p in recent:
        try:
            if p.name in linked: continue
            if p.name.startswith('live-'):
                r=live(p)
            else:
                r=normalize(p)
            counts[r['stage']]=counts.get(r['stage'],0)+1
            if counts[r['stage']]<=10:
                items.append(dict(id=p.name, stage=r['stage'], model=r['model'],status=r['status'],label=p.name))
        except (ValueError, KeyError, OSError):
            continue
    return items


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url=urlsplit(self.path)
        try:
            if url.path=='/api/info':
                return self.json({'app':'ai-from-scratch-visualization'})
            if url.path=='/api/runs':
                return self.json(catalog())
            if url.path=='/api/run':
                name=parse_qs(url.query).get('id',[''])[0]
                if name.startswith('example-'):
                    value=next((r for r in examples() if name=='example-'+r['stage']),None)
                    if value: return self.json(value)
                allowed={p.name:p for p in folders()}
                if name not in allowed: return self.send_error(404)
                folder=allowed[name]
                return self.json(live(folder) if name.startswith('live-') else normalize(folder))
            files={'/':'visualization/index.html','/app.js':'visualization/app.js','/style.css':'visualization/style.css','/tokenizer':'results/tokenizer.html'}
            if url.path not in files: return self.send_error(404)
            path=ROOT/files[url.path]
            content=path.read_bytes()
            mime='text/html' if path.suffix=='.html' else ('text/css' if path.suffix=='.css' else 'text/javascript')
            self.reply(content,mime+'; charset=utf-8')
        except (OSError, ValueError, KeyError, TypeError):
            self.json({'error':'Run is not ready yet. Retry after the next checkpoint.'},503)

    def json(self, obj, status=200):
        self.reply(json.dumps(obj,ensure_ascii=False).encode(), 'application/json; charset=utf-8', status)

    def reply(self, body, mime, status=200):
        self.send_response(status)
        self.send_header('Content-Type',mime)
        self.send_header('Content-Length',str(len(body)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self,*args): pass


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--port',type=int,default=5173)
    p.add_argument('--no-browser',action='store_true')
    p.add_argument('--export-examples',action='store_true',help='Rebuild curated examples from recorded local runs')
    a=p.parse_args()
    if a.export_examples:
        records=[normalize(ROOT/'runs'/name) for name in EXAMPLE_RUNS.values()]
        (ROOT/'visualization/examples.json').write_text(json.dumps(records,ensure_ascii=False,separators=(',',':'))+'\n')
        print('Exported three recorded runs; no model inference performed.')
    else:
        try:
            server=ThreadingHTTPServer(('127.0.0.1',a.port),Handler)
        except OSError:
            url=f'http://127.0.0.1:{a.port}'
            try:
                with urlopen(url+'/api/info',timeout=2) as response:
                    ours=json.load(response).get('app')=='ai-from-scratch-visualization'
            except (OSError,ValueError): ours=False
            if not ours: p.exit(1,f'Port {a.port} is in use. Try --port {a.port+1}.\n')
            print('Workshop visualization: '+url+' (already running)',flush=True)
            if not a.no_browser:webbrowser.open(url)
            raise SystemExit(0)
        url=f'http://127.0.0.1:{server.server_port}'
        print('Workshop visualization: '+url,flush=True)
        if not a.no_browser: webbrowser.open(url)
        try: server.serve_forever()
        except KeyboardInterrupt: pass
        finally: server.server_close()
