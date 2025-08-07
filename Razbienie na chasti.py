from math import ceil
n, m = map(int, input().split())
lst = [n // m for i in range(m)]
c = n % m
k = m - 1
while c:
    lst[k] += 1
    k -= 1
    c -= 1
print(*lst)