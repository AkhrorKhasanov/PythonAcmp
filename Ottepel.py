n = int(input())
lst = list(map(int, input().split()))
c = 0
maks = 0
for i in range(n):
    if lst[i] > 0:
        c += 1
    if c > maks:
        maks = c
    if lst[i] <= 0:
        c = 0
print(maks)