a, b = map(int, input().split())
l = int(str(a)[-1])
if l in [0, 1, 5, 6]:
    print(l)
elif l == 2:
    if b % 4 == 0:
        print(6)
    elif b % 4 == 1:
        print(2)
    elif b % 4 == 2:
        print(4)
    else:
        print(8)
elif l == 3:
    if b % 4 == 0:
        print(1)
    elif b % 4 == 1:
        print(3)
    elif b % 4 == 2:
        print(9)
    else:
        print(7)
elif l == 4:
    if b % 2 == 0:
        print(6)
    elif b % 2 == 1:
        print(4)
elif l == 7:
    if b % 4 == 0:
        print(1)
    elif b % 4 == 1:
        print(7)
    elif b % 4 == 2:
        print(9)
    else:
        print(3)
elif l == 8:
    if b % 4 == 0:
        print(6)
    elif b % 4 == 1:
        print(8)
    elif b % 4 == 2:
        print(4)
    else:
        print(2)
elif l == 9:
    if b % 2 == 0:
        print(1)
    elif b % 2 == 1:
        print(9)
    