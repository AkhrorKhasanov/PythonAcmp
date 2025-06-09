x, y = map(int, input().split())
if x * y == 1:
    print(0)
elif x == 1 or y == 1:
    print(1)
else:
    if x == y:
        print(2)
    else:
        print(1)