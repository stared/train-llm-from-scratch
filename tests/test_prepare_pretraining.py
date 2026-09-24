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
            prep.prepare('wolne-lektury')
        volume.batch_upload.assert_not_called()

    def test_missing_remote_uploads_all_files(self):
        volume = Mock()
        volume.read_file.side_effect = FileNotFoundError
        modal = MagicMock()
        modal.Volume.from_name.return_value = volume
        upload = modal.enable_output.return_value
        volume.batch_upload.return_value = upload
        with patch.object(prep, 'ROOT', self.root), patch.dict('sys.modules', {'modal':modal}):
            prep.prepare('wolne-lektury')
        self.assertEqual(upload.__enter__.return_value.put_file.call_count, 5)


class SejmPreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_chunks_reproduce_text_verbatim(self):
        import prepare_sejm_scratch as sejm
        text = ''.join(f'Poseł {i}:\r\nTekst  wystąpienia {i}.\r\n\r\n' for i in range(400)) + 'bez końca linii'
        source = self.root/'sejm.txt'
        source.write_bytes(text.encode('utf-8'))
        with patch.object(sejm, 'CHUNK_CHARS', 200), patch.object(sejm, 'HARD_LIMIT_CHARS', 800):
            parts = list(sejm.chunks(source))
        self.assertEqual(''.join(parts), text)
        self.assertGreater(len(parts), 50)
        self.assertTrue(all(p.endswith('\r\n\r\n') for p in parts[:-1]))

    def test_zip_archive_reads_member_verbatim(self):
        import zipfile
        import prepare_sejm_scratch as sejm
        text = 'Marszałek:\r\n\r\nProszę o zajęcie miejsc.\n'
        with zipfile.ZipFile(self.root/'sejm.zip', 'w') as z:
            z.writestr('sejm.txt', text.encode('utf-8'))
        self.assertEqual(''.join(sejm.chunks(self.root/'sejm.zip')), text)

    def test_missing_local_text_downloads_pinned_archive(self):
        import download_scratch_corpus
        import prepare_sejm_scratch as sejm
        downloaded = []
        with patch.object(prep, 'ROOT', self.root), patch.object(sejm, 'DEFAULT_SOURCE', self.root/'absent.txt'), \
                patch.object(download_scratch_corpus, 'download', lambda item, folder: downloaded.append(item['url'])):
            source = prep.sejm_source(None)
        self.assertEqual(downloaded, ['https://pliki.danieljanus.pl/sejm.zip'])
        self.assertEqual(source, self.root/'datasets/local/scratch-corpora/sejm/sejm.zip')

    def test_sejm_is_prepared_locally_without_modal(self):
        modal = Mock()
        prepared = []
        def fake_prepare(source, tokenizer, output):
            prepared.append(Path(source))
            output.mkdir(parents=True)
            (output/'tokenizer.json').write_bytes(b'{}')
            meta = {'tokenizer_sha256': hashlib.sha256(b'{}').hexdigest(), 'splits': {}}
            for split in ('train', 'dev', 'test'):
                (output/f'{split}.bin').write_bytes(b'\x01\x00')
                meta['splits'][split] = {'tokens': 1, 'sha256': hashlib.sha256(b'\x01\x00').hexdigest()}
            (output/'tokens.json').write_text(json.dumps(meta))
        with patch.object(prep, 'ROOT', self.root), patch('prepare_sejm_scratch.prepare', fake_prepare), \
                patch.dict('sys.modules', {'modal': modal}):
            prep.prepare('sejm', source=self.root/'sejm.txt')
        self.assertEqual(prepared, [self.root/'sejm.txt'])
        self.assertTrue((self.root/'datasets/local/sejm-scratch-v1/tokens.json').exists())
        modal.Volume.from_name.assert_not_called()
