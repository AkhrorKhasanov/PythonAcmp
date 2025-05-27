from math import ceil
l, w, h = list(map(int, input().split()))
res = 2 * h * (w + l)
print(ceil(res / 16))
