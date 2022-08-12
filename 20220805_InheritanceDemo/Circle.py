from Point import Point2D

class Circle(Point2D):
    def __init__(self, x, y, r):
        Point2D.__init__(self, x, y)
        print(f'ctor Circle({x}, {y}, {r})')
        self.r = r

    def __del__(self):
        print(f'dtor Circle({self.x}, {self.y}, {self.r})')

        #super().__del__()
        Point2D.__del__(self)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.r})'