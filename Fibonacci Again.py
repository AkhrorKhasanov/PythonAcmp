n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    a = b = 1
    i = 1
    while i < n:
        i += 1
        a, b = b % 10, (a + b) % 10
    print(b)