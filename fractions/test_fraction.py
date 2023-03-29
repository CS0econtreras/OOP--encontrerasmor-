import unittest
from main import Main
from fraction import Fractions
from unittest.mock import patch
from hypothesis import *

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
        
