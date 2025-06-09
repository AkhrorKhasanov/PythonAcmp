a, b, c, d = map(int, input().split())
lst = []
for i in range(-100, 101):
    k = a * i ** 3 + b * i ** 2 + c * i + d
    if not k:
        lst.append(i)
lst.sort()
print(*lst)    