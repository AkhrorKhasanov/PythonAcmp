m, n = map(int, input().split())
lst = [0 for i in range(10)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d = i * j
        while d:
            lst[d % 10] += 1
            d //= 10
for i in lst:
    print(i)