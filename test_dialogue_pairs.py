import unittest
from dialogue_pairs import parse, convert, key


class DialogueTest(unittest.TestCase):
    def test_adjacent_both_directions_and_boundaries(self):
        scenes=parse('A: First.\nB: Second.\nA: Third.\n\nC: Separate.\nD: Reply.')
        rows=convert(scenes,0)['train']
        self.assertEqual(len(rows),6)
        self.assertEqual({(r['prompt'],r['answer']) for r in rows},
                         {('First.','Second.'),('Second.','First.'),('Second.','Third.'),
                          ('Third.','Second.'),('Separate.','Reply.'),('Reply.','Separate.')})
        self.assertTrue(all([m['role'] for m in r['messages']]==['user','assistant'] for r in rows))

    def test_no_shared_lines_across_split(self):
        scenes=parse('A: Shared.\nB: One.\n\nC: shared.\nD: Two.\n\nE: Isolated.\nF: Three.')
        result=convert(scenes,.5)
        texts=lambda rows:{key(r[k]) for r in rows for k in ('prompt','answer')}
        self.assertTrue(result['train'] and result['validation'])
        self.assertFalse(texts(result['train']) & texts(result['validation']))

    def test_merge_and_deduplicate(self):
        scenes=parse('A: First part.\nA: Second part.\nB: Reply.\n\nA: First part.\nA: Second part.\nB: Reply.')
        self.assertEqual(len(convert(scenes,0)['train']),2)
        self.assertEqual(scenes[0][0]['text'],'First part.\nSecond part.')

    def test_reject_ambiguous_line(self):
        with self.assertRaises(ValueError):parse('Unlabelled quote')


if __name__=='__main__':unittest.main()
