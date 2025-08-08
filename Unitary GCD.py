from math import gcd
n, m = map(int, input().split())
print('1' * gcd(n, m))