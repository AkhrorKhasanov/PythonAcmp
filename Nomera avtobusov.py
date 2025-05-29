n = int(input())
hlp = 'ABCEHKMOPTXY'
hlp2 = '0123456789'
for i in range(n):
    s = input()
    if len(s) == 6 and s[0] in hlp and s[1] in hlp2 and s[2] in hlp2 and s[3] in hlp2 and s[4] in hlp and s[5] in hlp:
        print('Yes')
    else:
        print('No')
    