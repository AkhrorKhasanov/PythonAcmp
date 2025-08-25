p, k = map(int, input().split())
def solve(n):
    c = 0
    while n > 2:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        c += 1
    return c
s = 0
for i in range(p, k + 1):
    s += solve(i)
print(s)