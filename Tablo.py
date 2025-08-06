n, m = map(int, input().split())
colors = []
for i in range(n):
    s = input()
    colors.append(s)
codes = []
for i in range(n):
    helper = list(map(int, input().split()))
    codes.append(helper)
data = {
    0: ['.'],
    1: ['.', 'B'],
    2: ['.', 'G'],
    3: ['.', 'G', 'B'],
    4: ['.', 'R'],
    5: ['.', 'R', 'B'],
    6: ['.', 'R', 'G'],
    7: ['.', 'R', 'G', 'B'],
}
flag = False
for i in range(n):
    for j in range(m):
        if colors[i][j] not in data[codes[i][j]]:
            flag = True
            break
if flag:
    print('NO')
else:
    print('YES')