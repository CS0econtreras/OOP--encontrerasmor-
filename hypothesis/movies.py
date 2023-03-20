import sys
from typing import List, Any
class Movie:
    def __init__(self) -> None:
        self._movie:str
        self._temp1: List[str]
        self._cost: str
        self._real_cost: bool
    
    def movie_cap(self, temp1:str ) -> None:
        '''Gets the line and splits it into two parts
        then assigns the first part to the variable movie and the second part to the variable cost'''
        self._temp1 = temp1.split()
        self._movie = self._temp1[0]
        self._cost = (self._temp1[1])
        '''print(self._movie)
        print(self._cost)'''

    def get_movie(self) -> str:
        '''Get movie name
           Returns a string'''
        return self._movie
    
    def get_cost(self) -> str:
        '''Get cost of the movie
           Returns a float'''
        return self._cost
    