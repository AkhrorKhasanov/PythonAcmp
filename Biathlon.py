a = b = c = d = e = 0
for i in range(5):
    x, y = map(int, input().split())
    if x > 85 and (x - 100) * (x - 100) + y * y <= 100:
        a += 1
    elif x > 60 and (x - 75) * (x - 75) + y * y <= 100:
        b += 1
    elif x > 35 and (x - 50) * (x - 50) + y * y <= 100:
        c += 1
    elif x > 10 and (x - 25) * (x - 25) + y * y <= 100:
        d += 1
    elif x >= -10 and x * x + y * y <= 100:
        e += 1
lst = [a, b, c, d, e]
res = 0
for i in lst:
    if i > 0:
        res += 1
print(res)