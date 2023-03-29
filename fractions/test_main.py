import unittest
from main import Main
from fraction import Fractions
from unittest.mock import patch
from hypothesis import *

class testMain(unittest.TestCase):
    def test_set_user_fractions(self):
        obj = Main()

        obj._data = [[1, 2]]
        obj.set_user_fractions(0)
        self.assertEqual(obj._num, 1)

        obj._data = [[9, 4]]
        obj.set_user_fractions(0)
        self.assertEqual(obj._num, 9)

        obj._data = [[9, 4]]
        obj.set_user_fractions(0)
        self.assertEqual(obj._denom, 4)

    def test_user_fractions(self):
        obj = Main()

        with patch ('sys.stdin', open('data/data.in')):
            obj.userFractions()
            self.assertEqual(obj._data, [[27, 12], [2460000, 98400], [3, 4000], [0, 0]])
            
        with patch ('sys.stdin'):
            obj.userFractions()
            self.assertEqual(obj._data, [])

        with patch ('sys.stdin', open('data/data2.in')):
            obj.userFractions()
            self.assertEqual(obj._data, [[3, 4000], [7, 5]])

    def test_MixNum(self):
        obj = Main()

        with patch ('sys.stdin', open('data/data.in')):
            obj.userFractions()
            obj.MixNum()
            self.assertEqual(obj._data, [[27, 12], [2460000, 98400], [3, 4000], [0, 0]])

        with patch ('sys.stdin', open('data/data.in')):
            obj.userFractions()
            obj.MixNum()
            self.assertEqual(obj._num, 0)
            self.assertEqual(obj._denom, 0)

        with patch ('sys.stdin', open('data/data2.in')):
            obj.userFractions()
            obj.MixNum()
            self.assertEqual(obj._num, 7)
            self.assertEqual(obj._denom, 5)
