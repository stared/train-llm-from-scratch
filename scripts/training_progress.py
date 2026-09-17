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
    return send


def write_live(folder, stage, events, status, started, final=None):
    from training_report import chart
    names = list(dict.fromkeys(e['series'] for e in events))
    charts = ''.join('<h2>'+escape(name)+'</h2>'+chart(
        [(name, [(e['step'],e['value']) for e in events if e['series']==name])],
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
    print(f'Open during training: uv run scripts/view_results.py {stage}', flush=True)
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
