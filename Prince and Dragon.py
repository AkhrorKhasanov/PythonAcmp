from math import ceil
n, m, k = map(int, input().split())
if n >= m:
    print(1)
elif n <= k:
    print('NO')
else:
    print(ceil((m - k) / (n - k)))
