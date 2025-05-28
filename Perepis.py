n = int(input())
maks = -1
c = -1
for i in range(n):
    a, b = list(map(int, input().split()))
    if b == 1:
        if a > maks:
            c = i + 1
            maks = a
print(c)