class DiscrLessZero(Exception):
    def __init__(self, discriminant):
        self.discriminant = discriminant

    def __str__(self):
        return f'This coefficient\'s values give Discriminant {self.discriminant} < 0!' \
               f' There are no valid roots!'


class DiscrEqualZero(Exception):
    def __init__(self, discriminant):
        self.discriminant = discriminant

    def __str__(self):
        return f'This coefficient\'s values give Discriminant = {self.discriminant}!' \
               f' Only one root!'


class AisZero(Exception):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'This coefficient a = {self.a} cann\'t be 0!'
