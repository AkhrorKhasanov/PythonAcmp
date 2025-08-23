n = int(input())
lst = list(map(int, input().split()))
a = b = 0
p = []
n = []
for i in range(len(lst)):
    if lst[i] > 0:
        a += lst[i]
        p.append(i + 1)
    elif lst[i] < 0:
        b += abs(lst[i])
        n.append(i + 1)
if a or b:
    if a > b:
        print(len(p))
        print(*p)
    else:
        print(len(n))
        print(*n)
else:
    print(0)