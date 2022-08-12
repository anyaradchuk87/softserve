from Polyline import Polyline

class Point2D:
    def __init__(self, x, y):
        print(f'ctor Point2D({x}, {y})')
        self.__x = x
        self.__y = y

    @staticmethod
    def is_valid(x, y):
        return x >= 0 and y >= 0

    @staticmethod
    # factory method
    def create(x, y):
        if not Point2D.is_valid(x, y):
            return None

        result = Point2D(x, y)

        return result

    def __del__(self):
        print(f'dtor Point2D({self.__x}, {self.__y})')

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        # validation
        if x < 0:
            return

        self.__x = x

    def set_y(self, y):
        # validation
        if y < 0:
            return

        self.__y = y

    def move(self, dx, dy):
        print(f'Move: Point2D({self.__x}, {self.__y})')
        self.__x += dx
        self.__y += dy

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    # "<"
    def __lt__(self, other):
        return (self.__x + self.__y) > (other.__x + other.__y)

    def __add__(self, other):
        result = Polyline()
        result.add(self)
        result.add(other)

        return result