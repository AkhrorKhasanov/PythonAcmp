n, k = map(int, input().split())
p = 1
c = 0
while n:
    num = n % k
    p *= num
    c += num
    n //= k
print(p - c)
