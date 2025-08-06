n = int(input())
a = 1
b = 1
c = 2
while b < n:
    a, b = b, a + b
    c += 1
if b == n:
    print(1)
    print(c)
else:
    print(0)