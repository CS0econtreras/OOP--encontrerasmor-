import unittest
from main import Main

class TestPalindrom(unittest.TestCase):
    def test_palindrum_check(self):
        obj = Main()

        obj._user_phrase = "JFJWJF hdk #$#^&^#7678678 H34GR H"
        self.assertEqual(obj.palindrum_check(), "0")

        obj._user_phrase = "footstool"
        self.assertEqual(obj.palindrum_check(), "1")

        obj._user_phrase = "Ezequiel"
        self.assertEqual(obj.palindrum_check(), "0")


if __name__ == '__main__':
    unittest.main(verbosity=2)
