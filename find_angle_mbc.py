import math

AB = float(input())
BC = float(input())

print(str(round(math.degrees(math.atan(AB/BC)))) + '\xb0')