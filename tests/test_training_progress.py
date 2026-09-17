"""Check progress transport, safe HTML and selection of running versus saved results."""
import json
from pathlib import Path
import queue
import tempfile
import time
import unittest
from unittest.mock import patch
from training_progress import reporter, write_live
import view_results


class ProgressTests(unittest.TestCase):
    def test_metric_transport_and_loss_throttle(self):
        channel = queue.Queue()
        send = reporter(channel)
        send('Training loss',25,3.2)
        send('Training loss',50,3.1)
        send('Development loss',50,3.5)
        self.assertEqual(channel.qsize(),2)
        self.assertEqual(channel.get()['value'],3.2)
        self.assertEqual(channel.get()['series'],'Development loss')

    def test_live_html_refresh_and_completed_link(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            events=[dict(series='Loss <test>',step=0,value=9.),dict(series='Loss <test>',step=10,value=4.)]
            write_live(folder,'pretrain',events,'Running',time.monotonic())
            text=(folder/'report.html').read_text()
            self.assertIn('http-equiv="refresh"',text)
            self.assertIn('Loss &lt;test&gt;',text)
            self.assertIn('<polyline',text)
            write_live(folder,'pretrain',events,'Completed',time.monotonic(),final='scratch-demo')
            text=(folder/'report.html').read_text()
            self.assertNotIn('http-equiv="refresh"',text)
            self.assertIn('../scratch-demo/report.html',text)

    def test_viewer_prefers_fresh_running_chart_and_explicit_example(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);folder=root/'runs/live-pretrain-1';folder.mkdir(parents=True)
            write_live(folder,'pretrain',[],'Running',time.monotonic())
            with patch.object(view_results,'ROOT',root):
                self.assertEqual(view_results.choose('pretrain'),folder/'report.html')
                self.assertEqual(view_results.choose('pretrain',True),root/'results/literature-training.html')
                payload=json.loads((folder/'progress.json').read_text());payload['updated_at']=0
                (folder/'progress.json').write_text(json.dumps(payload))
                self.assertEqual(view_results.choose('pretrain'),root/'results/literature-training.html')
                payload['status']='Failed'
                (folder/'progress.json').write_text(json.dumps(payload))
                self.assertEqual(view_results.choose('pretrain'),folder/'report.html')
