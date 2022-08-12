from Circle import Circle
from Point import Point2D
from Polyline import Polyline
from Rect import Rect

# overloading
def get_min(*args):
    print(f'type(args): {type(args)}')
    min = None
    for a in args:
        if min == None or a < min:
            min = a

    return min

min1 = get_min(2, 4, -2, 100, -3)

print(f'min1: {min1}')

min2 = get_min(2, 110, -130)

print(f'min2: {min2}')

x = 10
y = 20

p1 = Point2D.create(x, y)
if not p1:
    print(':(')

p2 = Point2D(12, 14)
p3 = Point2D(21, 6)
p4 = Point2D(12, 34)

print('----------------------')

print(p1)

#p1.__x = 12
p1.set_x(-12)

print(p1)

print('----------------------')

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

r1 = Rect(10, 12, 31, 40)

print(r1)
r1.move(3, -2)
print(r1)

pict = [r1, c1, p1]

print('==========================')

for f in pict:
    print(f)

print('==========================')

# move() for pict
for f in pict:
    f.move(5, 4)


for f in pict:
    print(f)

print('==========================')