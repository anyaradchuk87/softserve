from Discriminant import Discriminant
from Error import DiscrEqualZero
from Error import DiscrLessZero
from Error import AisZero

first_run = 0

while first_run < 3:
    second_run = True
    a = 0
    while second_run:
        a = int(input('Enter a != 0 (a1, a2, a3 = 1): '))
        if a == 0:
            er = AisZero(a)
            print(er)
        else:
            second_run = False

    b = int(input('Enter b (b1 = -5)(b2 = -6)(b3 = -5): '))
    c = int(input('Enter c (c1 = 7)(c2 = 9)(c3 = -3): '))

    try:
        d = Discriminant(a, b, c)
        r = d.discr()
        print(r)
    except DiscrEqualZero as obj_ex:
        print(obj_ex)
    except DiscrLessZero as obj_ex:
        print(obj_ex)

    first_run += 1
