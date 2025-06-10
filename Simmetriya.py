x1, y1, x2, y2 = map(int, input().split())
xa, ya = map(int, input().split())
if x1 == x2:
    print(2 * x1 - xa, ya)
elif y1 == y2:
    print(xa, 2 * y1 - ya)