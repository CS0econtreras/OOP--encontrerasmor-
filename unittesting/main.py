'''strip punctuation from user input
   check if the user phrase is a palindrome by reversing the morse code'''
import sys
import re
from palindrom import Palindrom

class Main(object):
    def __init__(self) -> None:
        self._is_palindrome: bool
        self._palindrome_obj: Palindrom = Palindrom()

    def set_user_phrase(self) -> None:
        '''set the user phrase
           returns nothing'''
        self._user_phrase = sys.stdin.readline()
    
    def get_user_phrase(self) -> str:
        '''returns the user phrase
           returns string'''
        return self._user_phrase

    def palindrum_check(self) -> str:
        '''Returns True if the morse code is a palindrome
           returns string 1 if true and 0 if false'''
        self._palindrome_obj.remove_alphanumeric(self.get_user_phrase())
        self._palindrome_obj.set_morse_phrase()
        self._palindrome_obj.set_morse_backwards()
        if self._palindrome_obj.get_morse_phrase() == self._palindrome_obj.get_morse_backwards() and len(self._palindrome_obj.get_morse_phrase()) > 0:
            self._is_palindrome = True
            return "1"
        else:
            self._is_palindrome = False
            return "0"
            
            
    @staticmethod
    def main() -> None:
        obj = Main()
        obj.set_user_phrase()
        print(obj.palindrum_check())
if __name__ == "__main__":
    Main.main()
