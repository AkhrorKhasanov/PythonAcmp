n = int(input())
lst = []
c = 0
for i in range(n):
    s = input()
    c += s.count('C')
    lst.append(s)
res = []
d = 0
for i in range(n):
    hlp = ''
    for j in range(n):
        if d < c // 2:
            if lst[i][j] == 'C':
                d += 1
            hlp += '1'
        else:
            hlp += '2'
    res.append(hlp)
for i in res:
    print(i)
        