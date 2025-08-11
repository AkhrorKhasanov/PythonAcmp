s = input()
hlp1 = 'ABCDEFGH'
hlp2 = '12345678'
if not (len(s) == 5 and s[0] in hlp1 and s[1] in hlp2 and s[2] == '-' and s[3] in hlp1 and s[4] in hlp2):
    print('ERROR')
else:
    data = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
    }
    x1, x2 = data[s[0]], data[s[3]]
    y1, y2 = int(s[1]), int(s[4])
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('YES')
    else:
        print('NO')