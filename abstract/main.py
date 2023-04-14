from typing import Any, List
import sys
from kattis import Kattis
from cups import Cups
from abc import ABC, abstractmethod

class Main(Kattis):
    """
    Solution class for Kattis problem main
    """
    def __init__(self, imput_source: Any = sys.stdin) -> None:

        super().__init__(imput_source)
        self._data: list[list[str]] = []
        self._cup_list: List[Cups] = []
        self._answer : List[str] = []
        self._obj_cup: Cups
        self.read_input()

    def read_input(self) -> None:
        """
        Reads the data from the given source
        :return: None
        """
        data = self._input_source.readlines()
        data.pop(0)
        self._data = [list(map(str, data[i].split()))for i in range(len(data))]
        self.solve()
        self.answer()
        self.print_answer()
        

    @property
    def data(self) -> List[List[str]]:
        """
        Returns the data
        :return: data
        """
        return self._data

    def answer(self) -> List[Cups]:
        """
        Returns the answer
        :return: answer
        """
        self._cup_list.sort(key=lambda x: x._radious, reverse=False)
        return self._cup_list

    def solve(self) -> None:
        """
        Solves the problem
        :return: None
        """
        for i in range(len(self._data)):
            if self._data[i][0].isdigit() == True:
                self._obj_radius = int(self._data[i][0]) * .5
                self._obj_color = self._data[i][1]
            else:
                self._obj_radius = int(self._data[i][1])
                self._obj_color = self._data[i][0]
            self._cup_list.append(Cups(self._obj_radius, self._obj_color))


    def print_answer(self) -> None:
        """
        Prints the answer
        :return: None
        """
        for i in range(len(self._cup_list)):
            print(self._cup_list[i]._color)

if __name__ == "__main__":
    main = Main()
