import re
import sys

translate_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '0': '-----' 
        }

class Palindrom:
    def __init__(self) -> None:
        self._test_word: str
        self._morse_phrase: str
        self._morse_backwards: str
    
    def get_test_word(self) -> str:
        '''returns the user phrase'''
        return self._test_word

    def remove_alphanumeric(self, s:str) -> None:
        '''strip punctuation from user input
        returns nothing'''
        self._test_word = s
        self._test_word = re.sub('[^a-zA-Z0-9]+', '', self.get_test_word())
        self._test_word.replace(" ", "")

    def set_morse_phrase(self) -> None:
        '''set the morse code
        returns nothing'''
        self._morse_phrase = ""
        for i in (self.get_test_word().rstrip()):
            self._morse_phrase += translate_dict[i.upper()]
        #print(self._morse_phrase)

    def get_morse_phrase(self) -> str:
        '''Returns the morse code
        returns morse code string'''
        return self._morse_phrase
    
    def get_morse_backwards(self) -> str:
        '''Returns the morse code backwards
        returns morse code backwards string'''
        return self._morse_backwards

    def set_morse_backwards(self) -> None:
        '''Returns True if the morse code is a palindrome
        returns nothing'''
        self._morse_backwards = self.get_morse_phrase()[::-1]