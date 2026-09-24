"""Check the data transport used by the visualization app."""
import json
from pathlib import Path
import queue
import tempfile
import time
import unittest
from training_progress import reporter, write_live


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

    def test_live_updates_save_only_data(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            events=[dict(series='Loss',step=0,value=9.),dict(series='Loss',step=10,value=4.)]
            write_live(folder,'pretrain',events,'Running',time.monotonic())
            payload=json.loads((folder/'progress.json').read_text(encoding='utf-8'))
            self.assertEqual(payload['events'],events)
            self.assertEqual(payload['status'],'Running')
            write_live(folder,'pretrain',events,'Completed',time.monotonic(),final='scratch-demo')
            payload=json.loads((folder/'progress.json').read_text(encoding='utf-8'))
            self.assertEqual(payload['final'],'scratch-demo')
            self.assertEqual(payload['status'],'Completed')
            self.assertEqual([p.name for p in folder.iterdir()],['progress.json'])
