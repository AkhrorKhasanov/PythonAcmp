n = int(input())
lst = list(map(int, input().split()))
maks = 0
for i in range(n - 2):
    c = lst[i] + lst[i + 1] + lst[i + 2]
    if c > maks:
        maks = c
print(max(maks, lst[n - 1] + lst[n - 2] + lst[0], lst[n - 1] + lst[0] + lst[1]))