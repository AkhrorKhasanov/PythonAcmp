s = input()
c1 = c2 = 0
for i in range(len(s)):
    if i % 2:
        c1 += int(s[i])
    else:
        c2 += int(s[i])
if (c2 - c1) % 11:
    print('NO')
else:
    print('YES')