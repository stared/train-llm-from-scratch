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


if __name__ == '__main__':
    unittest.main()
