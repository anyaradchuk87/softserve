from Polyline import Polyline

class Point2D:
    def __init__(self, x, y):
        print(f'ctor Point2D({x}, {y})')
        self.x = x
        self.y = y

    def __del__(self):
        print(f'dtor Point2D({self.x}, {self.y})')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x}, {self.y})'

    # "<"
    def __lt__(self, other):
        return (self.x + self.y) > (other.x + other.y)

    def __add__(self, other):
        result = Polyline()
        result.add(self)
        result.add(other)

        return result