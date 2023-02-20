import sys
from polygonClass import Polygon

class main(object):

    def __init__(self):
        self._polygon_num:int
        self._poly_elements:str
        self._polygon_list:list[str] = []
        self._vertices_amount:int
        self._vertex_pairs:list[tuple[int,int]] =[]

    def set_polygon_num(self):
        
        self._polygon_num = int(sys.stdin.readline())
    
    def get_polygon_num(self):
        
        return self._polygon_num

    def set_poly_elements(self):
        self._poly_elements = sys.stdin.readline()
        self._polygon_list = self._poly_elements.split()
        self._vertices_amount = int(self._polygon_list[0])
    
    def get_vertices_amount(self) -> int:
        return self._vertices_amount
    

        

    def main():
        pass

    
    



