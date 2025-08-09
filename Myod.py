n, v, k = map(int, input().split())
s = v
flag = False
for i in range(1, n):
    hlp = v - i * k
    if hlp > 0:
        s += hlp
    else:
        flag = True
        break
if flag:
    print('NO', s)
else:
    print('YES', s)