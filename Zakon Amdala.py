n, p = map(int, input().split())
res = 1 / (((1 - p / 100) / n) + p / 100)
print(format(res, '.6f'))