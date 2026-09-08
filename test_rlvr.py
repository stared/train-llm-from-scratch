import unittest
from rlvr import reward, advantages


class RewardTest(unittest.TestCase):
    def test_exact_verifier(self):
        self.assertEqual(reward(' 42\n', 20, 22), 1.)
        for text in ['41', '42 or 43', 'The answer is 42', '042', '4.2e1', '42\n0', '__import__("os")']:
            self.assertEqual(reward(text, 20, 22), 0.)

    def test_leave_one_out(self):
        self.assertEqual(advantages([1., 0., 0., 0.]), [1., -1/3, -1/3, -1/3])
        self.assertEqual(advantages([1., 1., 1., 1.]), [0., 0., 0., 0.])
        self.assertEqual(advantages([0., 0., 0., 0.]), [0., 0., 0., 0.])
        with self.assertRaises(ValueError):
            advantages([1.])


if __name__ == '__main__':
    unittest.main()
