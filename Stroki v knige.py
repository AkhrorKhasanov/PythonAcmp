from math import ceil
k, n = list(map(int, input().split()))
res1 = ceil(n / k)
if n % k == 0:
    res2 = n - (res1 - 1) * k
else:
    res2 = n % k
print(res1, res2)