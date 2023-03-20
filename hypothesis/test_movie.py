import unittest
from movies import Movie

class TestMovie(unittest.TestCase):
    def test_movie_cap(self):
        obj = Movie()

        obj.movie_cap("yes 3")
        self.assertEqual(obj._movie, "yes")
        self.assertEqual(obj._cost, "3")

        obj.movie_cap("nooooo 4")
        self.assertEqual(obj._movie, "nooooo")
        self.assertEqual(obj._cost, "4")

        obj.movie_cap("yessirr 7")
        self.assertEqual(obj._movie, "yessirr")
        self.assertEqual(obj._cost, "7")


