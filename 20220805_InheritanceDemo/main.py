from Circle import Circle
from Point import Point2D
from Polyline import Polyline

p1 = Point2D(2, 4)
p2 = Point2D(12, 14)
p3 = Point2D(21, 6)
p4 = Point2D(12, 34)

print(p1)

pl1 = Polyline()
pl1.add(p1)
pl1.add(p2)
pl1.add(p3)
pl1.add(p4)

print('-------------------------')

for p in pl1:
    print(p, end=' - ')
print()

print('-------------------------')
for p in pl1.get_sorted_points():
    print(p, end=' ')
print()

p6 = Point2D(3, 8)
p7 = Point2D(8, 4)

pl2 = p6 + p7

print('-------------------------')
print('pl2:')
for p in pl2:
    print(p, end=' ')
print()


print('-------------------------')

c1 = Circle(12, 4, 3)

print(c1)

c1.move(2, 3)

print(c1)
