from __future__ import annotations
import sys
from fraction import Fractions

class Main(object):
    def __init__(self) -> None:
        self._data: 'list[list[int]]'
        self._num: int
        self._denom: int
        self._fraction_obj: Fractions = Fractions()

    def userFractions(self) -> None:
        '''This method takes the user input and converts it into a list of lists'''
        self.userImp = sys.stdin.readlines()
        self._data = [list(map(int, self.userImp[i].split())) for i in range(len(self.userImp))]
        
    def set_user_fractions(self, i:int) -> None:
        '''This method takes the user input and assigns it to the numerator and denominator'''
        temp = self.getData()[i]
        self._num = temp[0]
        self._denom = temp[1]

    def getNum(self) -> int:
        '''This method returns the numerator'''
        return self._num
    
    def getDenom(self) -> int:
        '''This method returns the denominator'''
        return self._denom
    
    def getData(self) -> 'list[list[int]]':
        '''This method returns the user input'''
        return self._data
    
    def MixNum(self) -> None:
        '''This method calls the mixed_frac method from the Fractions class to out put the mixed fraction'''
        for i in range(len(self.getData())):
            self.set_user_fractions(i)
            if self._denom == 0:
                return 
            else:
                self._fraction_obj.mixed_frac(self.getNum(), self.getDenom())

    @staticmethod
    def main() -> None:
        obj = Main()
        obj.userFractions()
        obj.MixNum()
        
if __name__ == "__main__":
    Main.main()