n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
maks = -1
for i in range(n):
    hlp = l1[i] * l2[i]
    if maks < hlp:
        maks = hlp
        k = i + 1
print(k)