n = int(input())
flag = False
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    flag = True
if flag:
    if n >= 1000:
        print('12/09/' + str(n))
    elif n >= 100:
        print('12/09/0' + str(n))
    elif n >= 10:
        print('12/09/00' + str(n))
    else:
        print('12/09/000' + str(n))
else:
    if n >= 1000:
        print('13/09/' + str(n))
    elif n >= 100:
        print('13/09/0' + str(n))
    elif n >= 10:
        print('13/09/00' + str(n))
    else:
        print('13/09/000' + str(n))