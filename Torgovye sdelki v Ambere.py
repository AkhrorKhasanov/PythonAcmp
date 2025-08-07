n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())
def solve(n, p):
    c = 0
    while n >= p:
        c += n % p
        n //= p
    c += n
    return c
if solve(n1, p1) == solve(n2, p2):
    print(solve(n1, p1))
else:
    print(0)