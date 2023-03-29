
class Fractions:
    def __init__(self) -> None:
        self._intPart: int
        self._remPart: int
        self._mixFrac: int

    def mixed_frac(self, n:int, d:int) -> None:
        '''This method takes the numerator and denominator and returns the mixed fraction'''
        self._intPart = n//d
        self._remPart = n%d
        print(f"{self._intPart} {self._remPart} / {d}")