import unittest
from rlvr_tasks import check, expression, make_data, TASKS


class Verifiers(unittest.TestCase):
    def test_stories(self):
        row = {'anchors': ['robot', 'ghost']}
        self.assertTrue(check('six_words', row, 'Lonely robot befriended the forgotten ghost.')['success'])
        for text in ['', 'robot ghost', 'robot robot ghost ghost robot ghost', 'robotic ghosts haunt a silent house', 'Lonely robot befriended the forgotten ghost. 123']:
            self.assertFalse(check('six_words', row, text)['success'])

    def test_math(self):
        row = {'numbers': [3, 3, 8], 'target': 48}
        self.assertTrue(check('countdown', row, '(3+3)*8')['success'])
        for text in ['48', '3*8*2', '(3+3)*8=48', '__import__("os")', '3**8', '3//8', '3/0', 'True', '3.0+3+8', '-3+3+8']:
            self.assertFalse(check('countdown', row, text)['success'])
        self.assertEqual(expression('8/(3-2)')[0], 8)

    def test_maze(self):
        row = dict(grid=['S#G.', '....', '....', '....'], start=[0, 0], goal=[0, 2], reference='DRRU')
        self.assertTrue(check('maze', row, 'DRRU')['success'])
        for text in ['RR', 'U', 'DRR', 'DRRUU', 'Here: DRRU', 'DR RU', 'DRRU'*10]:
            self.assertFalse(check('maze', row, text)['success'])

    def test_generated_splits(self):
        for task in TASKS:
            data = make_data(task)
            prompts = [r['prompt'] for rows in data.values() for r in rows]
            self.assertEqual(len(prompts), len(set(prompts)))
            self.assertEqual(data, make_data(task))
            if task != 'six_words':
                for rows in data.values():
                    for row in rows:
                        self.assertTrue(check(task, row, row['reference'])['success'])


if __name__ == '__main__':
    unittest.main()
