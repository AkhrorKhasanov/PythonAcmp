s = input()
pos_x = s.find('x')
if pos_x == 0:
    if s[1] == '-':
        print(int(s[-1]) + int(s[2]))
    else:
        print(int(s[-1]) - int(s[2]))
elif pos_x == 4:
    if s[1] == '-':
        print(int(s[0]) - int(s[2]))
    else:
        print(int(s[0]) + int(s[2]))
else:
    if s[1] == '-':
        print(int(s[0]) - int(s[-1]))
    else:
        print(int(s[-1]) - int(s[0]))