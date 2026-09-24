"""Exercise Windows encoding and content-type failure cases on every platform."""
import json
import mimetypes
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from prawko import save as save_exam
from rlvr_showcase import save as save_rlvr
from visualization import server


class PortabilityTests(unittest.TestCase):
    def test_saved_outputs_and_bundled_examples_with_windows_text_defaults(self):
        original_open = Path.open

        for codepage in ('cp1250', 'cp1252'):
            def windows_open(path, mode='r', buffering=-1, encoding=None,
                             errors=None, newline=None):
                if 'b' not in mode:
                    encoding = codepage if encoding in (None, 'locale') else encoding
                    if newline is None and any(flag in mode for flag in 'wax'):
                        newline = '\r\n'
                return original_open(path, mode, buffering, encoding, errors, newline)

            with self.subTest(codepage=codepage), tempfile.TemporaryDirectory() as tmp:
                with patch.object(Path, 'open', windows_open):
                    # These are the real bundled UTF-8 files, including split byte tokens.
                    examples = server.examples()
                    self.assertEqual({r['stage'] for r in examples}, {'pretrain', 'sft', 'rlvr'})
                    self.assertIsNotNone(server.read(server.ROOT / 'datasets/wiki-tokenizer.json'))
                    payload = {'text': 'Był piękny dzień. → 東京 😀\nNastępny wiersz.'}
                    for save in (save_exam, save_rlvr):
                        output = Path(tmp) / 'result.json'
                        save(output, payload)
                        self.assertEqual(server.read(output), payload)
                        expected = json.dumps(payload, ensure_ascii=False, indent=2).encode('utf-8')
                        self.assertEqual(output.read_bytes(), expected)

    def test_browser_assets_ignore_system_mime_associations(self):
        # Simulate a Windows file association that labels JavaScript as plain text.
        with patch.dict(mimetypes.types_map, {'.js': 'text/plain', '.css': 'application/octet-stream'}):
            for route, expected in (
                ('/app.js', 'text/javascript; charset=utf-8'),
                ('/prediction.js', 'text/javascript; charset=utf-8'),
                ('/tokenizer/app.js', 'text/javascript; charset=utf-8'),
                ('/style.css', 'text/css; charset=utf-8'),
                ('/', 'text/html; charset=utf-8'),
            ):
                with self.subTest(route=route):
                    handler = object.__new__(server.Handler)
                    handler.path = route
                    handler.reply = Mock()
                    handler.send_error = Mock()
                    handler.do_GET()
                    handler.send_error.assert_not_called()
                    self.assertEqual(handler.reply.call_args.args[1], expected)
