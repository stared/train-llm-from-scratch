"""Stream small metric records from Modal into a self-refreshing local HTML chart."""
from html import escape
import json
from pathlib import Path
import queue
import threading
import time


def reporter(channel):
    """Progress is best-effort; a chart failure must not stop model training."""
    last = {}
    def send(series, step, value):
        if channel is None:
            return
        now = time.monotonic()
        if series == 'Training loss' and now-last.get(series, 0) < 5:
            return
        last[series] = now
        try:
            channel.put(dict(series=series, step=step, value=float(value)), timeout=2)
        except Exception as error:
            print(f'Progress chart unavailable: {type(error).__name__}', flush=True)
    def preview(**event):
        if channel is not None:
            try:
                channel.put(dict(kind='preview', **event), timeout=2)
            except Exception as error:
                print(f'Example preview unavailable: {type(error).__name__}', flush=True)
    send.preview = preview
    return send


def write_live(folder, stage, events, status, started, final=None):
    from training_report import chart
    metrics = [e for e in events if 'series' in e]
    names = list(dict.fromkeys(e['series'] for e in metrics))
    charts = ''.join('<h2>'+escape(name)+'</h2>'+chart(
        [(name, [(e['step'],e['value']) for e in metrics if e['series']==name])],
        'Training updates', name) for name in names)
    elapsed = time.monotonic()-started
    meta = dict(stage=stage, status=status, elapsed_seconds=elapsed, updated_at=time.time(), events=events, final=final)
    (folder/'progress.tmp').write_text(json.dumps(meta, indent=2))
    (folder/'progress.tmp').replace(folder/'progress.json')
    body = (f'<h1>{escape(stage)} training</h1><p>{escape(status)}. Elapsed: {elapsed/60:.1f} minutes.</p>'
            '<p>Development metrics use held-out examples. Training loss and reward measure different objectives.</p>')
    if not events:
        body += '<p>Starting the worker, loading the model and evaluating the baseline. Metrics appear when evaluation finishes.</p>'
    if status in ('Failed', 'Interrupted'):
        body += '<p>No completed result was produced. See the training terminal for the error.</p>'
    body += charts
    if final:
        body += f'<p><a href="../{escape(final, quote=True)}/report.html">Open completed report and before/after answers</a></p>'
    refresh = '<meta http-equiv="refresh" content="3">' if status in ('Running','Finishing') else ''
    content = ('<!doctype html><meta charset="utf-8">'+refresh+'<title>Training progress</title>'
               '<style>body{font:16px system-ui;max-width:950px;margin:30px auto;padding:0 20px}svg{width:100%}text{font:13px system-ui}</style>'+body)
    temp = folder/'report.tmp'
    temp.write_text(content)
    temp.replace(folder/'report.html')


def run_live(worker, stage, *args):
    import modal
    folder = Path(__file__).resolve().parents[1]/'runs'/f'live-{stage}-{time.time_ns()}'
    folder.mkdir(parents=True)
    events, result, failures = [], [], []
    started = time.monotonic()
    write_live(folder, stage, events, 'Running', started)
    print('Live chart:', folder.relative_to(folder.parents[1])/'report.html', flush=True)
    print('Open during training: pnpm visualization', flush=True)
    with modal.Queue.ephemeral() as channel:
        def work():
            try:
                result.append(worker.remote(*args, progress_queue=channel))
            except BaseException as error:
                failures.append(error)
        thread = threading.Thread(target=work, daemon=True)
        thread.start()
        try:
            while thread.is_alive():
                try:
                    events.append(channel.get(timeout=1))
                except queue.Empty:
                    pass
                write_live(folder, stage, events, 'Running', started)
            thread.join()
            while (event := channel.get(block=False)) is not None:
                events.append(event)
        except BaseException:
            write_live(folder, stage, events, 'Interrupted', started)
            raise
    if failures:
        write_live(folder, stage, events, 'Failed', started)
        raise failures[0]
    name, files = result[0]
    elapsed = time.monotonic()-started
    files['client_timing.json'] = json.dumps(dict(elapsed_seconds=elapsed, includes='worker startup, model loading, training, evaluation and result transfer; image build before entrypoint excluded'))
    write_live(folder, stage, events, 'Completed', started, final=name)
    return name, files


def token_records(ids, probabilities, alternatives, tokenizer, sampling=None):
    """Lossless UTF-8 bytes for GPT-2/ByteLevel tokenizers, including split characters."""
    alphabet = list(range(33,127))+list(range(161,173))+list(range(174,256))
    chars = alphabet.copy()
    extra = 0
    for b in range(256):
        if b not in alphabet:
            alphabet.append(b); chars.append(256+extra); extra+=1
    reverse = {chr(c):b for b,c in zip(alphabet,chars)}
    def raw(i):
        return tokenizer.id_to_token(i) if hasattr(tokenizer,'id_to_token') else tokenizer.convert_ids_to_tokens(i)
    def describe(i):
        piece=raw(i)
        data=[reverse[c] for c in piece] if all(c in reverse for c in piece) else list(piece.encode())
        return dict(id=i, piece=piece, bytes=data)
    records=[]
    for j,(i,p,top) in enumerate(zip(ids,probabilities,alternatives)):
        record=dict(**describe(i), probability=p, alternatives=[dict(id=a, piece=raw(a), probability=b) for a,b in top])
        if sampling is not None: record['sampling_probability']=sampling[j]
        records.append(record)
    return records


def completion_trace(model, tokenizer, seq, attention_mask, offset):
    """Trace one already-generated completion; no sampling or gradient updates."""
    import torch
    ids=seq[0,offset:].tolist()
    stop=next((j for j,i in enumerate(ids) if i in tokenizer.all_special_ids),len(ids))
    ids=ids[:stop]
    if not ids:return []
    prefix=seq[:1,:offset+len(ids)]
    mask=torch.cat([attention_mask[:1],torch.ones((1,len(ids)),device=prefix.device,dtype=attention_mask.dtype)],1)
    with torch.no_grad():
        logits=model(input_ids=prefix,attention_mask=mask,use_cache=False,logits_to_keep=len(ids)+1).logits[0,:-1].float()
        probs=logits.softmax(-1)
        values,indices=probs.topk(5,dim=-1)
        selected=probs.gather(-1,torch.tensor(ids,device=probs.device)[:,None]).squeeze(-1).tolist()
    return token_records(ids,selected,[list(zip(a,b)) for a,b in zip(indices.tolist(),values.tolist())],tokenizer)
