k = int(input())
for i in range(k):
    n1, n2 = map(str, input().split())
    set1 = set(n1)
    set2 = set(n2)
    if set1 == set2:
        print('YES')
    else:
        print('NO')