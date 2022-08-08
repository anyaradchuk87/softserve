from Fraction import ProperFraction
from Fraction import ImproperFraction
from Fraction import MixedFraction
from Fraction import Fraction


dr1 = ProperFraction(3, 5)
dr2 = ProperFraction(4, 7)
print(dr1 < dr2)
print(dr1 > dr2)

dr3 = MixedFraction(1, 2, 5)
print(dr3)
print(dr1)
print(dr2)
print(dr3)

dr4 = ProperFraction(3, 10)
dr5 = ProperFraction(2, 13)
dr6 = dr4 + dr5

print(dr6)

print(dr1 - dr2)
print(dr1 ** 2)

print(int(dr1))

dr7 = ImproperFraction(4, 3)
print(int(dr7))

print(float(dr1))
dr3 = MixedFraction(1, 2, 5)
print(float(dr3))
print(dr3)

dr8 = MixedFraction(2, 3, 8)
dr9 = MixedFraction(1, 2, 5)
print(dr8 - dr9)
print(dr8 + dr9)

dr10 = ProperFraction(2, 4)
dr11 = Fraction(4, 8)
print(dr10 == dr11)

dr12 = MixedFraction(2, 2, 4)
dr13 = MixedFraction(2, 4, 8)
print(dr12 == dr13)