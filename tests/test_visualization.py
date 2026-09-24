"""Data provenance and incremental live transport, without a GPU."""
import json
from pathlib import Path
import queue
import tempfile
import time
import unittest
from unittest.mock import patch, Mock
from training_progress import reporter, write_live, token_records
from visualization import server as visualization


class VisualizationTests(unittest.TestCase):
    def test_completed_run_keeps_live_id_in_either_folder_order(self):
        for stage in ('pretrain', 'sft', 'rlvr'):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as d:
                root = Path(d)
                live_folder = root/'runs'/f'live-{stage}-123'
                final_folder = root/'runs'/f'scratch-{stage}-456'
                live_folder.mkdir(parents=True)
                final_folder.mkdir()
                events = [dict(kind='preview', label='Before', step=0,
                               rows=[dict(prompt='Hello', continuation=' world')],
                               metadata=dict(model='Test model', source='Test corpus'))]
                write_live(live_folder, stage, events, 'Running', time.monotonic())
                completed = dict(id=final_folder.name, stage=stage, model='Test model',
                                 status='Completed', snapshots=[dict(rows=events[0]['rows'])])
                with patch.object(visualization, 'ROOT', root), \
                     patch.object(visualization, 'examples', return_value=[]), \
                     patch.object(visualization, 'normalize', return_value=completed):
                    with patch.object(visualization, 'folders', return_value=[live_folder]):
                        self.assertEqual(visualization.catalog()[0]['id'], live_folder.name)
                    write_live(live_folder, stage, events, 'Completed', time.monotonic(), final=final_folder.name)
                    for order in ([final_folder, live_folder], [live_folder, final_folder]):
                        with patch.object(visualization, 'folders', return_value=order):
                            items = visualization.catalog()
                            self.assertEqual(len(items), 1)
                            self.assertEqual(items[0]['id'], live_folder.name)
                            self.assertEqual(items[0]['status'], 'Completed')
                            handler = object.__new__(visualization.Handler)
                            handler.path = '/api/run?id='+items[0]['id']
                            handler.json = Mock()
                            handler.do_GET()
                            self.assertEqual(handler.json.call_args.args[0]['status'], 'Completed')
                    # Results without a live record still use their own folder ID.
                    with patch.object(visualization, 'folders', return_value=[final_folder]):
                        self.assertEqual(visualization.catalog()[0]['id'], final_folder.name)

    def test_replies_disable_browser_caching(self):
        handler = object.__new__(visualization.Handler)
        handler.send_response = Mock()
        handler.send_header = Mock()
        handler.end_headers = Mock()
        handler.wfile = Mock()
        handler.reply(b'content', 'text/javascript')
        handler.send_header.assert_any_call('Cache-Control', 'no-store')

    def test_local_report_is_rendered_without_writing_html(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)
            records={'style_result':dict(model='Example',examples=1,teacher='authored'),
                     'dataset':{},'loss':[dict(step=1,loss=2)],
                     'base':[dict(prompt='<question>',answer='before')],
                     'finetuned':[dict(prompt='<question>',answer='after')]}
            for name,value in records.items():
                (folder/(name+'.json')).write_text(json.dumps(value), encoding='utf-8', newline='\n')
            report=visualization.render_report(folder)
            self.assertIn('&lt;question&gt;',report)
            self.assertIn('before',report)
            self.assertIn('after',report)
            self.assertFalse((folder/'report.html').exists())

    def test_app_routes_use_source_files(self):
        for route, marker in [('/', b'/app.js'), ('/tokenizer', b'/tokenizer/app.js'),
                              ('/tokenizer/app.js', b"fetch('/api/tokenizer')"),
                              ('/reports', b'/reports/app.js')]:
            handler=object.__new__(visualization.Handler)
            handler.path=route
            handler.reply=Mock()
            handler.send_error=Mock()
            handler.do_GET()
            handler.send_error.assert_not_called()
            self.assertIn(marker, handler.reply.call_args.args[0])

    def test_report_routes_exclude_private_files(self):
        for route in ['/reports/../package.json', '/reports/../../runs/private.json', '/runs/private.json']:
            handler=object.__new__(visualization.Handler)
            handler.path=route
            handler.send_error=Mock()
            handler.do_GET()
            handler.send_error.assert_called_once_with(404)

    def test_live_previews_coexist_with_metrics_and_disconnect(self):
        q=queue.Queue();send=reporter(q)
        send('Development loss',0,8.)
        send.preview(label='Before',step=0,split='fixed prompts',rows=[dict(prompt='Hi',continuation=' there')],metadata=dict(model='Test model'))
        events=[q.get(),q.get()]
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)
            write_live(folder,'pretrain',events,'Running',time.monotonic())
            value=visualization.live(folder)
            self.assertEqual(value['model'],'Test model')
            self.assertEqual(value['curves'][0]['points'],[[0,8.]])
            self.assertEqual(value['snapshots'][0]['rows'][0]['continuation'],' there')
            raw=json.loads((folder/'progress.json').read_text(encoding='utf-8'));raw['updated_at']=0
            (folder/'progress.json').write_text(json.dumps(raw), encoding='utf-8', newline='\n')
            self.assertEqual(visualization.live(folder)['status'],'Disconnected')

    def test_examples_are_complete_and_pairs_match(self):
        examples=visualization.examples()
        self.assertEqual({x['stage'] for x in examples},{'pretrain','sft','rlvr'})
        for run in examples:
            self.assertTrue(run['curves'])
            before=run['snapshots'][0]['rows']
            key='id' if 'id' in before[0] else 'prompt'
            for snap in run['snapshots']:
                self.assertEqual([r[key] for r in snap['rows']],[r[key] for r in before])
                for row in snap['rows']:
                    if run.get('exam'):
                        self.assertEqual(len(row['probabilities']), 3)
                        self.assertAlmostEqual(sum(row['probabilities']), 1, places=5)
                    else:
                        self.assertTrue(row['tokens'])
                        decoded = bytes(b for t in row['tokens'] for b in t['bytes']).decode(errors='replace')
                        self.assertEqual(decoded, row.get('continuation', row.get('text')))
                        for token in row['tokens']:
                            self.assertGreaterEqual(token['probability'], 0)
                            self.assertLessEqual(token['probability'], 1)
            if run['stage']!='pretrain':self.assertTrue(run['training'])
        self.assertTrue(next(x for x in examples if x['stage']=='rlvr')['rollouts'])

    def test_byte_tokens_preserve_split_polish_character(self):
        class Tokenizer:
            def id_to_token(self,i):return ['Ġ','Å','Ĥ'][i]
        rows=token_records([0,1,2],[.2,.3,.4],[[(0,.2)]]*3,Tokenizer())
        self.assertEqual(bytes(b for r in rows for b in r['bytes']).decode(),' ł')

    def test_catalog_does_not_follow_symlinks(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'runs').mkdir();(root/'elsewhere').mkdir()
            (root/'runs/scratch-link').symlink_to(root/'elsewhere',target_is_directory=True)
            with patch.object(visualization,'ROOT',root):self.assertEqual(visualization.folders(),[])
