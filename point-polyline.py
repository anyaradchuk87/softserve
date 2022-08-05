class Point2D:
    def __init__(self, x, y):
        print(f'konstructor Point2D({x}, {y})')
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x}, {self.y})'


class Polyline:
    def __init__(self):
        self.points = []
        self.current_position = 0

    def add(self, point):
        self.points.append(point)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position >= len(self.points):
            raise StopIteration

        current_point = self.points[self.current_position]
        self.current_position += 1

        return current_point


p1 = Point2D(2, 4)  #student
p2 = Point2D(4, 6)
p3 = Point2D(8, 2)
p4 = Point2D(10, 4)


pl1 = Polyline()   #group
pl1.add(p1)
pl1.add(p2)
pl1.add(p3)
pl1.add(p4)
print(p1)
for p in pl1:
    print(p, end=' - ')
print()