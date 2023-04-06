import sys
from typing import List

class Stat(list):
    def __init__(self) -> None:
        '''This is the constructor'''
        self._sMax: int
        self._sMin: int
        self._sRange: int
        self._temp_list: List[List[int]] = []
        self._output: str

    def getStats(self, temp_list: List[List[int]]) -> None:
        '''This method gets the stats from the input and prints max, min and range'''
        self._temp_list = temp_list
        for i in range(len(self._temp_list)):
            if self._temp_list[i][0] <= 30 and self._temp_list[i][0] > 0:
                self._sMax = max(self._temp_list[i][1:])
                self._sMin = min(self._temp_list[i][1:])
                self._sRange = self._sMax - self._sMin
                if i == 10:
                    break
                print(f"Case {i+1}: {self._sMin} {self._sMax} {self._sRange}")
        
        self._output = f"Case {i+1}: {self._sMin} {self._sMax} {self._sRange}"

