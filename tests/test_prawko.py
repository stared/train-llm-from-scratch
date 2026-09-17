import itertools
import json
from pathlib import Path
import unittest
from difflib import SequenceMatcher

from prawko import question
from prepare_prawko import normalize


class PrawkoTests(unittest.TestCase):
    def test_option_permutations_preserve_answer(self):
        row = dict(question='Test?', options=['first', 'second', 'third'], answer=1)
        for order in itertools.permutations(range(3)):
            prompt, answer = question(row, order)
            self.assertEqual(order[answer], 1)
            self.assertIn(f'{"ABC"[answer]}. second', prompt)

    def test_split_and_similarity_isolation(self):
        data = json.loads(Path('datasets/prawko-v2/data.json').read_text())
        self.assertEqual({k: len(v) for k,v in data.items()}, dict(train=100, dev=25, test=40))
        self.assertEqual(len({r['id'] for rows in data.values() for r in rows}),165)
        for left, right in itertools.combinations(data.values(), 2):
            for a in left:
                for b in right:
                    self.assertLess(max(SequenceMatcher(None, normalize(a['question']), normalize(b['question'])).ratio(),
                                       SequenceMatcher(None, normalize(b['question']), normalize(a['question'])).ratio()), .72)

    def test_expanded_data_preserves_holdouts(self):
        original=json.loads(Path('datasets/prawko-v2/data.json').read_text())
        extended=json.loads(Path('datasets/prawko-v2/extended.json').read_text())
        self.assertEqual(len(extended['train']),289)
        for split in ('dev','test'):
            self.assertEqual(extended[split],original[split])
        train_ids={r['id'] for r in extended['train']}
        self.assertTrue({r['id'] for r in original['train']}<=train_ids)
        for row in extended['train']:
            self.assertEqual(len(row['options']),3)
            self.assertIn(row['answer'],range(3))
            for held in extended['dev']+extended['test']:
                self.assertNotEqual(row['id'],held['id'])
                a,b=normalize(row['question']),normalize(held['question'])
                self.assertLess(max(SequenceMatcher(None,a,b).ratio(),SequenceMatcher(None,b,a).ratio()),.72)


if __name__ == '__main__':
    unittest.main()
