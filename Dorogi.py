n = int(input())
c = 0
for i in range(n):
    lst = list(map(int, input().split()))
    for j in lst:
        if j:
            c += 1
print(c // 2)