import unittest
from examples import TASKS, dataset, score


class ExamplesTest(unittest.TestCase):
    def test_splits_and_answers(self):
        for task in TASKS:
            train, test = dataset(task, 'train'), dataset(task, 'test')
            self.assertFalse({r['prompt'] for r in train} & {r['prompt'] for r in test})
            self.assertEqual(train, dataset(task, 'train'))
            for row in train + test:
                self.assertTrue(score(task, row['answer'], row['answer'])['correct'])

    def test_extraction_requires_schema_and_values(self):
        answer = '{"id":1,"item":"pen","quantity":2}'
        self.assertTrue(score('extraction', '{"quantity": 2, "id": 1, "item": "pen"}', answer)['correct'])
        self.assertFalse(score('extraction', '{"id":true,"item":"pen","quantity":2}', answer)['correct'])
        self.assertFalse(score('extraction', '{}', answer)['format_valid'])
        self.assertFalse(score('extraction', answer + ' extra', answer)['correct'])

    def test_format_is_not_correctness(self):
        self.assertEqual(score('polish', '17', '18'), {'correct': False, 'format_valid': True})
        self.assertFalse(score('routing', 'The answer is K1', 'K1')['correct'])


if __name__ == '__main__':
    unittest.main()
