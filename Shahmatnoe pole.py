x1, y1, x2, y2 = map(int, input().split())
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('YES')
else:
    print('NO')