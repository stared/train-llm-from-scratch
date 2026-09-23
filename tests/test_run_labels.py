import unittest
from pathlib import Path
from unittest.mock import patch
from visualization import server


class RunLabelTests(unittest.TestCase):
    def test_model_size_corpus_size_and_time(self):
        run = dict(model='ScratchGPT-30m', stage='pretrain', source='Wolne Lektury', seconds=600)
        server.describe_run(run, dict(source='Wolne Lektury', training_pool_tokens=101000000), Path('/unused'))
        self.assertEqual(server.run_label(run), 'ScratchGPT (30M), Wolne Lektury (101M tokens), 10 min')

    def test_exam_uses_selected_epoch_and_training_split_size(self):
        run = dict(model='Qwen/Qwen3.5-0.8B', stage='sft', exam=True, seconds=180)
        with patch.object(server, 'source_data', return_value={'train': [None]*100}):
            server.describe_run(run, {'selected_epoch': 3}, Path('/unused'))
        self.assertEqual(server.run_label(run), 'Qwen3.5 (0.8B), Polish driving exam (100 questions), epoch 3')

    def test_catalog_omits_empty_launches(self):
        empty=dict(id='live-pretrain-1',model='',stage='pretrain',status='Completed',snapshots=[])
        with patch.object(server,'examples',return_value=[]),patch.object(server,'folders',return_value=[Path('/unused/live-pretrain-1')]),patch.object(server,'live',return_value=empty):
            self.assertEqual(server.catalog(), [])

    def test_catalog_deduplicates_curated_run(self):
        run=dict(id='scratch-demo',stage='pretrain',model='ScratchGPT',status='Completed',snapshots=[{}])
        with patch.object(server,'examples',return_value=[run]),patch.object(server,'folders',return_value=[Path('/unused/scratch-demo')]):
            self.assertEqual(len(server.catalog()),1)
