n = int(input())
lst = list(map(int, input().split()))
c = 3
s = 0
for i in range(n):
    if lst[i]:
        s += c
        c += 1
    else:
        c = max(3, c - 3)
print(s)