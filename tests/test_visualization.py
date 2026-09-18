"""Data provenance and incremental live transport, without a GPU."""
import json
from pathlib import Path
import queue
import tempfile
import time
import unittest
from unittest.mock import patch
from training_progress import reporter, write_live, token_records
import visualization


class VisualizationTests(unittest.TestCase):
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
            raw=json.loads((folder/'progress.json').read_text());raw['updated_at']=0
            (folder/'progress.json').write_text(json.dumps(raw))
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
