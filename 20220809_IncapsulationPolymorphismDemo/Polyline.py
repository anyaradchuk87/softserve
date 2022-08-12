

class Polyline:
    def __init__(self):
        self.points = []
#        self.current_position = 0

    def add(self, point):
        self.points.append(point)

    def get_sorted_points(self):
        points_copy = self.points.copy()
        points_copy.sort()
        for p in points_copy:
            yield p

    # def __iter__(self):
    #     return self
    #
    # def  __next__(self):
    #     if self.current_position >= len(self.points):
    #         raise  StopIteration
    #
    #     current_point = self.points[self.current_position]
    #     self.current_position += 1
    #
    #     return current_point


    def __iter__(self):
#        return self
        return PolylineIterator(self)

class PolylineIterator:
    def __init__(self, source):
        self.current_position = 0
        self.source = source

    def  __next__(self):
        if self.current_position >= len(self.source.points):
            raise  StopIteration

        current_point = self.source.points[self.current_position]
        self.current_position += 1

        return current_point