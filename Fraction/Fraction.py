class Fraction:
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den

    def __str__(self):
        return f'{self.numerator}\n\u2014\n{self.denominator}'

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __pow__(self, power):
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __int__(self):
        if self.numerator < self.denominator:
            return 0

        return self.numerator // self.denominator

    def __eq__(self, other):
        return (self.numerator / self.denominator) == (other.numerator / other.denominator)


# num < den
class ProperFraction(Fraction):
    def __init__(self, num, den):
        Fraction.__init__(self, num, den)

    def __float__(self):
        return self.numerator / self.denominator


# num > den
class ImproperFraction(Fraction):
    def __init__(self, num, den):
        Fraction.__init__(self, num, den)

    def __str__(self):
        return f'{self.numerator}\n\u2014\n{self.denominator}'

    def __float__(self):
        return float(self.numerator / self.denominator)


# has a whole part
class MixedFraction(Fraction):
    def __init__(self, whole, num, den):
        Fraction.__init__(self, num, den)
        self.whole = whole

    def __str__(self):
        return f'  {self.numerator}\n{self.whole} \u2014\n  {self.denominator}'

    def __int__(self):
        return self.whole

    def __float__(self):
        return self.whole + float(self.numerator / self.denominator)

    def __sub__(self, other):
        dr1 = ImproperFraction(self.numerator + self.whole * self.denominator, self.denominator)
        dr2 = ImproperFraction(other.numerator + other.whole * other.denominator, other.denominator)
        return dr1 - dr2

    def __add__(self, other):
        dr1 = ImproperFraction(self.numerator + self.whole * self.denominator, self.denominator)
        dr2 = ImproperFraction(other.numerator + other.whole * other.denominator, other.denominator)
        return dr1 + dr2

    def __lt__(self, other):
        if self.whole == other.whole:
            return Fraction(self.numerator, self.denominator) < \
                   Fraction(other.numerator, other.denominator)

        return self.whole < other.whole

    def __gt__(self, other):
        if self.whole == other.whole:
            return Fraction(self.numerator, self.denominator) > \
                   Fraction(other.numerator, other.denominator)

        return self.whole > other.whole

    def __eq__(self, other):
        return (self.whole == other.whole) and (Fraction(self.numerator, self.denominator) ==
                                                Fraction(other.numerator, other.denominator))
