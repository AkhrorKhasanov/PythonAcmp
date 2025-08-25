from math import pi, atan
xk, yk = map(float, input().split())
xc, yc, rc = map(float, input().split())
d = ((xk - xc) ** 2 + (yk - yc) ** 2) ** 0.5
if d > rc:
    a = (d ** 2 - rc ** 2) ** 0.5
    b = 2 * (pi - atan(a / rc))
    s = rc * (a + b * rc / 2)
else:
    s = pi * rc ** 2
print(format(s, '.3f'))