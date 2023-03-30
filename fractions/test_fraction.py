import unittest
from main import Main
from fraction import Fractions
from unittest.mock import patch
from hypothesis import *
from io import StringIO


class testfraction(unittest.TestCase):

    def test_mixed_frac(self):
        obj = Fractions()
        
        obj.mixed_frac(1, 2)
        self.assertEqual(obj._intPart, 0)
        self.assertEqual(obj._remPart, 1)

        obj.mixed_frac(5, 3)
        self.assertEqual(obj._intPart, 1)
        self.assertEqual(obj._remPart, 2)

        obj.mixed_frac(9, 4)
        self.assertEqual(obj._intPart, 2)
        self.assertEqual(obj._remPart, 1)

    '''testing string output'''
    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        obj = Fractions()
        obj.mixed_frac(12, 3)
        self.assertEqual(mock_stdout.getvalue(),'4 0 / 3\n')

        obj = Fractions()
        obj.mixed_frac(27, 12)
        self.assertEqual(mock_stdout.getvalue(),'4 0 / 3\n2 3 / 12\n')

        obj = Fractions()
        obj.mixed_frac(67, 19)
        self.assertEqual(mock_stdout.getvalue(),'4 0 / 3\n2 3 / 12\n3 10 / 19\n')
    
