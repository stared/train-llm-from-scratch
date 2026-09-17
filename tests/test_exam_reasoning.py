import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('exam_reasoning',Path(__file__).resolve().parents[1]/'additional/scripts/exam_reasoning.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class ExamReasoningChecks(unittest.TestCase):
    def test_only_final_answer_counts(self):
        check=lambda text:module.check_exam('exam',{'answer':'B'},text)
        self.assertTrue(check('A jest błędne.\n</think>\nOdpowiedź: B')['success'])
        self.assertTrue(check('B')['success'])
        self.assertFalse(check('Odpowiedź: B\nJednak wybieram A.')['success'])
        self.assertFalse(check('Rozważam B, ale nie wiem.')['valid_answer'])
        self.assertFalse(check('Odpowiedź: A')['success'])
        self.assertFalse(check('Odpowiedź: BB')['valid_answer'])
        self.assertFalse(check('Odpowiedź: B albo C')['valid_answer'])
