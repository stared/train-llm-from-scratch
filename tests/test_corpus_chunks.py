import unittest
from corpus_chunks import chunk_tokens


class CorpusChunksTest(unittest.TestCase):
    def test_line_boundaries_and_exact_target_coverage(self):
        ids=list(range(23))
        blocks,forced=chunk_tokens(ids,8,[4,8,12,16,20])
        self.assertEqual([x for b in blocks for x in b[1:]],ids[1:])
        self.assertTrue(all(len(b)<=9 for b in blocks))
        self.assertTrue(all(b[-1]+1 in [4,8,12,16,20] for b in blocks[:-1]))
        self.assertEqual(forced,0)

    def test_long_line_fallback_retains_every_target(self):
        ids=list(range(20))
        blocks,forced=chunk_tokens(ids,4,[])
        self.assertEqual([x for b in blocks for x in b[1:]],ids[1:])
        self.assertGreater(forced,0)

    def test_legacy_fixed_chunks(self):
        ids=list(range(1026))
        blocks,_=chunk_tokens(ids)
        self.assertEqual(blocks,[ids[i:i+257] for i in range(0,len(ids)-1,256)])
