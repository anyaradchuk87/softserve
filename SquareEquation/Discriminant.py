from Error import DiscrLessZero
from Error import DiscrEqualZero


class Discriminant:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discr(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        if discr < 0:
            return DiscrLessZero(self)
        elif discr == 0:
            res = (- self.b) / (2 * self.a)

            return f'{DiscrEqualZero(self)}, x = {res}'

        res1 = (- self.b + discr ** 0.5) / (2 * self.a)
        res2 = (- self.b - discr ** 0.5) / (2 * self.a)

        return f'The roots are valid. x1 = {res1}, x2 = {res2}'

    def __str__(self):
        return f'{(self.b ** 2 - 4 * self.a * self.c)}'
