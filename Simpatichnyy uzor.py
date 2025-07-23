lst = []
for i in range(4):
    s = input()
    lst.append(s)
flag = False
for i in range(3):
    for j in range(3):
        if lst[i][j] == lst[i][j + 1] == lst[i + 1][j] == lst[i + 1][j + 1]:
            flag = True
            break
if flag:
    print('No')
else:
    print('Yes')