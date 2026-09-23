import unittest
from visualization.standard_tokenizers import tokenize


class StandardTokenizerTests(unittest.TestCase):
    def test_known_text_and_unicode_round_trip(self):
        for name in ('cl100k_base', 'o200k_base'):
            with self.subTest(name=name):
                self.assertEqual(len(tokenize({'tokenizer': name, 'text': 'Hello, world!'})['ids']), 4)
                text = 'Łódź, Cześć! 🦆\n' + '<|endoftext|>'
                result = tokenize({'tokenizer': name, 'text': text})
                raw = b''.join(bytes.fromhex(t['hex']) for t in result['initial'][0])
                self.assertEqual(raw.decode(), text)
                self.assertEqual(len(result['ids']), len(result['initial'][0]))

    def test_empty_text(self):
        self.assertEqual(tokenize({'tokenizer': 'o200k_base', 'text': ''})['ids'], [])

    def test_reject_invalid_requests(self):
        for request in ({'tokenizer': 'unknown', 'text': 'test'}, {'tokenizer': 'cl100k_base', 'text': 'x' * 2001}):
            with self.assertRaises(ValueError):
                tokenize(request)
