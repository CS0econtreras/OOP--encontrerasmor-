import sys
from typing import List
from movies import Movie

class Main(object):
    def __init__(self) -> None:
        self._total_cost: bool
        self._movie_obj: Movie = Movie()
        self._movie_temp: str
        self._cost_temp: str
        self._movieName_cost: str

    def set_movieName_cost(self) -> None:
        '''Set a movie name and cost'''
        self._movieName_cost = sys.stdin.readline()
    
    def get_movieName_cost(self) -> str:
        '''Get movie name and cost
           Returns a string'''
        return self._movieName_cost
    
    def movie_cost(self) -> None:
        '''Get movie name and cost with the function get_movieName_cost then compare
           the length of the movie name and the cost of the movie to get the cost of the movie'''
        self._movie_obj.movie_cap(self.get_movieName_cost())
        self._movie_temp = self._movie_obj.get_movie()
        self._cost_temp = self._movie_obj.get_cost()
        if str(len(self._movie_temp)) >= self._cost_temp:
            self._total_cost = True
        else:
            self._total_cost = False

    def answer(self) -> None:
        '''prints the answer of the function movie_cost
           Returns a string'''
        if self._total_cost:
            print(self._cost_temp)
        else:
            self._movie_temp = (str(len(self._movie_temp)))
            print(self._movie_temp)

    #return self._total_cost

    @staticmethod
    def main() -> None:
        obj = Main()
        obj.set_movieName_cost()
        obj.movie_cost()
        obj.answer()
if __name__ == "__main__":
    Main.main()