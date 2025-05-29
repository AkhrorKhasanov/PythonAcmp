n = int(input())
lst = list(map(int, input().split()))
k = int(input())
c = 0
for i in range(n):
    if lst[i] >= k:
        c += k
    else:
        c += lst[i]
print(c)