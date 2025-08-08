n = int(input())
lst = list(map(int, input().split()))
c = 0
for i in range(1, n):
    if lst[i] == lst[i - 1] + 1:
        continue
    else:
        c += 1
print(c)