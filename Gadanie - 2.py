from math import gcd
n = int(input())
c = 0
for i in range(1, n):
    if gcd(i, n) == 1:
        c += 1
print(c)