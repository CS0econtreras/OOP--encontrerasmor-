import unittest
from palindrom import Palindrom

class morse_code(unittest.TestCase):
    def test_remove_alphanumeric(self):
        obj = Palindrom()

        obj.remove_alphanumeric("       ")
        self.assertEqual(obj._test_word, "")

        obj.remove_alphanumeric("!@#$%^&")
        self.assertEqual(obj._test_word, "")

        obj.remove_alphanumeric("Y% ^&* ESS")
        self.assertEqual(obj._test_word, "YESS")

    def test_set_morse_phrase(self):
        obj = Palindrom()
        
        obj._test_word = "YESS"
        obj.set_morse_phrase()
        self.assertEqual(obj._morse_phrase, "-.--.......")

        obj._test_word = "NONO"
        obj.set_morse_phrase()
        self.assertEqual(obj._morse_phrase, "-.----.---")

        obj._test_word = "EZEQUIEL"
        obj.set_morse_phrase()
        self.assertEqual(obj._morse_phrase, ".--...--.-..-....-..")

    def test_set_morse_backwards(self):
        obj = Palindrom()
        
        obj._morse_phrase = "-.--......."
        obj.set_morse_backwards()
        self.assertEqual(obj._morse_backwards, ".......--.-")

        obj._morse_phrase = "-.----.---"
        obj.set_morse_backwards()
        self.assertEqual(obj._morse_backwards, "---.----.-")

        obj._morse_phrase = ".--...--.-..-....-.."
        obj.set_morse_backwards()
        self.assertEqual(obj._morse_backwards, "..-....-..-.--...--.")

if __name__ == '__main__':
    unittest.main(verbosity=2)