s = input()
p1 = 0
p2 = 1
while p1 + p2 <= len(s):
    p3 = p1 + p2
    print(s[p3 - 1], end='')
    p1 = p2
    p2 = p3