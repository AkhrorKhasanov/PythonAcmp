n, m = map(int, input().split())
if not m:
    print('NO')
else:
    print(str(n)[:-1] + str(int(str(n)[-1]) + 1))