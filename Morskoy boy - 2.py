n, m = map(int, input().split())
lst = ['.' * (m + 2)]
for i in range(n):
    s = input()
    lst.append('.' + s + '.')
lst.append('.' * (m + 2))
c = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if lst[i][j] == '.' and lst[i - 1][j] == '.' and lst[i + 1][j] == '.' and lst[i][j - 1] == '.' and lst[i][j + 1] == '.':
            c += 1
print(c)