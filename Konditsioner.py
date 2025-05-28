room, cond = list(map(int, input().split()))
mode = input()
if mode == 'heat':
    if cond > room:
        print(cond)
    else:
        print(room) 
elif mode == 'freeze':
    if cond < room:
        print(cond)
    else:
        print(room)
elif mode == 'auto':
    print(cond) 
elif mode == 'fan':
    print(room)