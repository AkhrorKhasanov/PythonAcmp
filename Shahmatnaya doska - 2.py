n, m, i, j, c = map(int, input().split())
if not (n * m) % 2:
    print('equal')
else:
    if (i + j) % 2:
        if c == 1:
            print('black')
        else:
            print('white')
    else:
        if c == 1:
            print('white')
        else:
            print('black')