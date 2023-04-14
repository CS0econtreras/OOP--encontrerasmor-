import unittest
from main import Main
from cups import Cups
from unittest.mock import patch
from hypothesis import *
from io import StringIO
import hypothesis.strategies as some
from hypothesis import given, settings, Verbosity

class test(unittest.TestCase):

    #test read_input using mock'''
    @patch('sys.stdin', StringIO('3\nred 10\n10 blue\ngreen 7\n'))
    def test_read_input_data(self):
        obj = Main()
        obj.read_input()
        self.assertEquals(obj._data, [['red', '10'],['10', 'blue'],['green', '7']])