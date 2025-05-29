from math import pi
s, r1 = map(float, input().split())
res = (r1 ** 2 - s / pi) ** 0.5
print(f"{res:.3f}")