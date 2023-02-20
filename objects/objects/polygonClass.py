

class convex:
    def polygon(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.coArea = 0.0
        self.j = self.n - 1



def convexArea(x, y, n):
    n = len(x)
    coArea = 0.0
    j = n - 1
    for i in range(n):
        coArea += x[i] * y[j]
        coArea -= y[i] * x[j]
        j = i
    coArea = abs(coArea) / 2.0
    return coArea

