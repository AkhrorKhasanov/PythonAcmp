s, p = map(int, input().split())
for i in range(1, 1001):
    flag = False
    for j in range(1, 1001):
        if i + j == s and i * j == p:
            print(i, j)
            flag = True
            break
    if flag:
        break