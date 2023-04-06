import unittest
from main import Main
from stats import Stat
from unittest.mock import patch
from io import StringIO
from hypothesis import strategies as some
from hypothesis import given


class test(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_getStats(self, mock_stdout):
        obj = Stat()
        obj.getStats([[4, 2, 3, 4, 5], [3, 5, 9, 0]])
        self.assertEqual(mock_stdout.getvalue(),'Case 1: 2 5 3\nCase 2: 0 9 9\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_getStatsAgain(self, mock_stdout):
        obj = Stat()
        obj.getStats([[2, 10, 3], [3, 4, 9, 7]])
        self.assertEqual(mock_stdout.getvalue(),'Case 1: 3 10 7\nCase 2: 4 9 5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_getStatsAgain2(self, mock_stdout):
        obj = Stat()
        obj.getStats([[5, 44, 15, 3, 0, 8], [4, 6, 7, 3, 1], [3, 5, 9, 0]])
        self.assertEqual(mock_stdout.getvalue(),'Case 1: 0 44 44\nCase 2: 1 7 6\nCase 3: 0 9 9\n')
    
    @given(l = some.lists(some.integers(), min_size=1, max_size=10)) 
    def test_something(self, l)-> None:
        obj = Stat()
        obj.getStats([[4, 2, 3, 4, 5], [3, 5, 9, 0]])
        self.assertEqual(obj._temp_list , [[4, 2, 3, 4, 5], [3, 5, 9, 0]])