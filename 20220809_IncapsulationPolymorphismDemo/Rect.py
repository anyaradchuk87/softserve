from Point import Point2D

class Rect (Point2D):
    def __init__(self, x, y, x2, y2):
        #Point2D.__init__(self, x, y)
        super().__init__(x, y)
        print(f'ctor Rect({x}, {y}, {x2}, {y2})')

        self.__x2 = x2
        self.__y2 = y2

    def move(self, dx, dy):
        print(f'Move: Rect({self.get_x()}, {self.get_y()}, {self.__x2}, {self.__y2})')
        super().move(dx, dy)
        self.__x2 += dx
        self.__y2 += dy

    def __str__(self):
        # base_result =  super().__str__()
        # return f'{base_result} - ({self.__x2}, {self.__y2})'
        return f'({self.get_x()}, {self.get_y()}, {self.__x2}, {self.__y2})'

    def __del__(self):
        print(f'dtor Rect({self.get_x()}, {self.get_y()}, {self.__x2}, {self.__y2})')
        #Point2D.__del__(self$)
        super().__del__()

