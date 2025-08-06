n = int(input())
e = '7182818284590452353602875'
if n == 0:
    print(3)
elif n == 25:
    print('2.' + e)
elif n == 1:
    print('2.7')
else:
    hlp = int(e[n])
    hlp2 = int(e[n - 1])
    if hlp >= 5:
        hlp2 += 1
    print('2.' + e[:n - 1] + str(hlp2))
