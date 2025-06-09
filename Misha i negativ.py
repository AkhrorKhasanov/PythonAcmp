n, m = map(int, input().split())
lst1 = []
for i in range(n):
    s = input()
    lst1.append(s)
kksiz = input()
lst2 = []
for i in range(n):
    s = input()
    lst2.append(s)
c = 0
for i in range(n):
    for j in range(m):
        if lst1[i][j] == lst2[i][j]:
            c += 1
print(c)