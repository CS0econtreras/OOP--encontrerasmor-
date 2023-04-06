from __future__ import annotations
import sys
from stats import Stat
class Main(object):

    def __init__(self) -> None:
        '''This is the constructor'''
        self._temp_list: list[list[int]] = []
        self._num_test_cases: int
        self._input: list[str] = []
        self._obj_stat: Stat = Stat()
        
    def get_input(self) -> None:
        '''This method gets the input from the user'''
        self._input = sys.stdin.readlines()

    def set_testCaseNum(self) -> None:
        '''This method sets the number of test cases'''
        self._temp_list = [list(map(int, self._input[i].split())) for i in range(len(self._input))]
        for i in range (len(self._temp_list)):
            self._num_test_cases = self._temp_list[i][0]

def Class() -> None:
    '''This is the main function'''
    main = Main()
    main.get_input()
    main.set_testCaseNum()
    main._obj_stat.getStats(main._temp_list)
    
    

if __name__ == "__main__":
    Class()
