n, m, y, x = map(int, input().split())
if y % 2 == 1:
    print((y - 1) * m + x - 1)
else:
    print(y * m - x)