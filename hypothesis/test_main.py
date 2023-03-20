import unittest
from unittest.mock import patch
from main import Main
import sys
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.strategies import text


class testCost(unittest.TestCase):
    def test_movieCost(self):
        obj = Main()

        obj._movieName_cost = "yes 3"
        obj.movie_cost()
        self.assertEqual(obj._total_cost, True)

        obj._movieName_cost = "nooooo 4"
        obj.movie_cost()
        self.assertEqual(obj._total_cost, True)

        obj._movieName_cost = "yahooo 7"
        obj.movie_cost()
        self.assertEqual(obj._total_cost, False)

    def test_answer(self):
        obj = Main()

        obj._total_cost = True
        obj._cost_temp = "3"
        obj.answer()
        self.assertEqual(obj._cost_temp, "3")

        obj._total_cost = False
        obj._movie_temp = "yessir"
        obj.answer()
        self.assertEqual(obj._movie_temp, "6")

        obj._total_cost = False
        obj._movie_temp = "yes"
        obj._cost_temp = "3"
        obj.answer()
        self.assertEqual(obj._cost_temp, "3")

    def test_set_movieName_cost(self):
        obj = Main()

        with patch('sys.stdin', open('data/1.in')):
            obj.set_movieName_cost()
            self.assertEqual(obj._movieName_cost, "GoneWithTheWind 13.341")
        
        with patch('sys.stdin', open('data/2.in')):
            obj.set_movieName_cost()
            self.assertEqual(obj._movieName_cost, "Gigi 93.7")

        with patch('sys.stdin', open('data/3.in')):
            obj.set_movieName_cost()
            self.assertEqual(obj._movieName_cost, "PieHard 3.14159265358979323846")
    

    @given(text())
    def test_movieName_cost(self, movieName_cost):
        obj = Main()
        obj._movieName_cost = movieName_cost
        self.assertEqual(obj._movieName_cost, movieName_cost)
        print (obj._movieName_cost)
        print (movieName_cost)
    

                
if __name__ == '__main__':
    unittest.main(verbosity=2)