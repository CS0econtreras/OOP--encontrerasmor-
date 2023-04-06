import unittest
from main import Main
from stats import Stat
from unittest.mock import patch
from hypothesis import *
from io import StringIO
import hypothesis.strategies as some
from hypothesis import given, settings, Verbosity

class test(unittest.TestCase):
    def test_setCaseNum(self):
        obj = Main()
        obj._input = ['4 2 3 4 5']
        obj.set_testCaseNum()
        self.assertEqual(obj._num_test_cases, 4)

        obj = Main()
        obj._input = ['3 5 9 0']
        obj.set_testCaseNum()
        self.assertEqual(obj._num_test_cases, 3)

        obj = Main()
        obj._input = ['9 2 3 4 5 6 7 8 9 10']
        obj.set_testCaseNum()
        self.assertEqual(obj._num_test_cases, 9)

    def test_get_imput(self):
        obj = Main()

        with patch ('sys.stdin', open('data/sample.in')):
            obj.get_input()
            self.assertEqual(obj._input, ['2 4 10\n','9 2 5 6 4 5 9 2 1 4\n','7 6 10 1 2 5 10 9\n','1 9\n'])
        
        with patch ('sys.stdin', open('data/sample2.in')):
            obj.get_input()
            self.assertEqual(obj._input, ['3 4 5 6\n'])

        with patch ('sys.stdin', open('data/sample3.in')):
            obj.get_input()
            self.assertEqual(obj._input, ['4 5 6 7 8\n'])   

    def test_getStats(self):
        obj = Stat()
        obj.getStats([[4, 2, 3, 4, 5]])
        self.assertEqual(obj._output, 'Case 1: 2 5 3')

        obj = Stat()
        obj.getStats([[2, 10, 3]])
        self.assertEqual(obj._output, 'Case 1: 3 10 7')

        obj = Stat()
        obj.getStats([[5, 44, 15, 3, 0, 8]])
        self.assertEqual(obj._output, 'Case 1: 0 44 44')