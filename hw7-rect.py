import math


def get_point():
    input_number = input('Vvedit koordinaty:')
    while not input_number.isnumeric():
        input_number = input('Vvedit koordinaty:')
    else:
        point = input_number


def get_rect_set(rec, point1, point2):
    if point2[0] < point1[0] and point2[1] < point1[1]:
        for i in range(point1[0], point2[0] - 1, -1):
            for j in range(point1[1], point2[1] - 1, -1):
                rec.add((i, j))
    elif point2[1] < point1[1]:
        for i in range(point1[0], point1[1] + 1):
            for j in range(point2[0], point2[1] - 1, -1):
                rec.add((i, j))
    elif point2[0] < point1[0]:
        for i in range(point1[0], point2[0] - 1, -1):
            for j in range(point1[1], point2[1] + 1):
                rec.add((i, j))
    else:
        for i in range(point1[0], point2[0] + 1):
            for j in range(point1[1], point2[1] + 1):
                rec.add((i, j))
    return rec


def find_square(point1, point2):
    square = abs((point2[0] - point1[0]) * (point2[1] - point1[1]))

    return square


point1 = get_point(4, 2)

point2 = get_point(0, 6)

point3 = get_point(7, 0)

point4 = get_point(2, 8)

point5 = get_point(3, 5)

point6 = get_point(9, 9)

point7 = get_point(8, 4)

point8 = get_point(5, 2)

rec1 = set([])
rec2 = set([])
rec3 = set([])
rec4 = set([])

get_rect_set(rec1, point1, point2)
get_rect_set(rec2, point3, point4)
get_rect_set(rec3, point5, point6)
get_rect_set(rec4, point7, point8)

square1 = find_square(point1, point2)
square2 = find_square(point3, point4)
square3 = find_square(point5, point6)
square4 = find_square(point7, point8)

per13 = rec1 & rec3
per24 = rec2 & rec4
per = per13 & per24
print(per13)
print(per24)
print(per)

main_set = [rec1, rec2, rec3, rec4]
print(set.intersection(*main_set))