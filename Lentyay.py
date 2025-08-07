n = int(input())
one = []
two = []
for i in range(n):
    a, b = map(int, input().split())
    one.append(a)
    two.append(b)
if n == 1:
    print('YES')
else:
    if max(one) <= min(two):
        print('YES')
    else:
        print('NO')