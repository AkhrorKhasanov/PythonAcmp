n, k1, k2 = map(int, input().split())
lst = list(map(int, input().split()))
def solve(n, k):
    c = 0
    while n:
        c += n % k
        n //= k
    return c
res = []
for i in lst:
    s = solve(i, k1) * solve(i, k2)
    res.append(s)
res.sort()
print(*res)