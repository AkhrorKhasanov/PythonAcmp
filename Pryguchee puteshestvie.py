n, bx, by, l = map(int, input().split())
lst = []
flag = False
for i in range(n):
    ax, ay = map(int, input().split())
    if (ax - bx) ** 2 + (ay - by) ** 2 <= l ** 2:
        print(i + 1)
        flag = True
        break
if not flag:
    print('Yes')