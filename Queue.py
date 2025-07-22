k = int(input())
m = 5 * (k - 1)
if m > 12 * 60:
    print('NO')
else:
    print(m // 60, m % 60)