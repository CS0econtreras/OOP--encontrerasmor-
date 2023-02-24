import sys
from polygonClass import convex_polygon

class main(object):

    def __init__(self):
        self._convx_poly: convex_polygon
        self._polygon_num:int
        self._poly_elements:str
        self._polygon_list:list[str] = []
        self._vertices_amount:int
        self._vertex_pairs:list[tuple[int,int]] = []

    def set_polygon_num(self):
         self._polygon_num = int(sys.stdin.readline())
    
    def get_polygon_num(self) -> int:
        return self._polygon_num

    def get_poly_list(self) -> list:
        return self._polygon_list
    
    def get_vertices_amount(self) -> int:
        return self._vertices_amount
    
    def get_vertex_pairs(self) -> list:
        return self._vertex_pairs
    
    def new_polygon(self):
        new_polygon = convex_polygon()
        new_polygon.set_area(self.get_vertices_amount(), self.get_vertex_pairs())
        print(new_polygon.get_area())

    def set_poly_elements(self):
        self._poly_elements = sys.stdin.readline()
        self._polygon_list = self._poly_elements.split()
        self._vertices_amount = int(self._polygon_list[0])
        self._vertex_pairs = []

    def answer(self):
        self.set_polygon_num()
        for i in range(self.get_polygon_num()):
            self.set_poly_elements()
            for j in range(self.get_vertices_amount()):
                temp_list = self.get_poly_list()
                x = int(temp_list[(2*j)+1])
                y = int(temp_list[(2*j)+2])
                self._vertex_pairs.append((x,y))
            temp_list = [] 
            self.new_polygon()   

    @staticmethod
    def main() -> None:
        obj = main()
        obj.answer()

if __name__ == "__main__":
    main.main()
