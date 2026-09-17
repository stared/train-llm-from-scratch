"""Preparation must reject damaged data and avoid re-uploading matching files."""
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import MagicMock, Mock, patch
import prepare_pretraining as prep


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root/'datasets/local/wl-scratch-v1'
        self.folder.mkdir(parents=True)
        metadata = {'tokenizer_sha256': hashlib.sha256(b'{}').hexdigest(), 'splits': {}}
        (self.folder/'tokenizer.json').write_bytes(b'{}')
        for split in ('train','dev','test'):
            (self.folder/f'{split}.bin').write_bytes(b'\x01\x00')
            metadata['splits'][split] = {'tokens': 1, 'sha256': hashlib.sha256(b'\x01\x00').hexdigest()}
        (self.folder/'tokens.json').write_text(json.dumps(metadata))

    def test_corrupt_tokens_rejected(self):
        prep.validate(self.folder)
        (self.folder/'train.bin').write_bytes(b'\x02\x00')
        with self.assertRaisesRegex(ValueError, 'Checksum'):
            prep.validate(self.folder)

    def test_matching_remote_skips_upload(self):
        volume = Mock()
        volume.read_file.return_value = [(self.folder/'tokens.json').read_bytes()]
        volume.listdir.return_value = [SimpleNamespace(path=f'/datasets/wl-scratch-v1/{f}', size=(self.folder/f).stat().st_size) for f in prep.FILES]
        modal = Mock()
        modal.Volume.from_name.return_value = volume
        with patch.object(prep, 'ROOT', self.root), patch.dict('sys.modules', {'modal':modal}):
            prep.prepare('literature')
        volume.batch_upload.assert_not_called()

    def test_missing_remote_uploads_all_files(self):
        volume = Mock()
        volume.read_file.side_effect = FileNotFoundError
        modal = MagicMock()
        modal.Volume.from_name.return_value = volume
        upload = modal.enable_output.return_value
        volume.batch_upload.return_value = upload
        with patch.object(prep, 'ROOT', self.root), patch.dict('sys.modules', {'modal':modal}):
            prep.prepare('literature')
        self.assertEqual(upload.__enter__.return_value.put_file.call_count, 5)
