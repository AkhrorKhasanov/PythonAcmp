n1, n2 = map(str, input().split())
b = 0
hlp = 0
for i in range(4):
    if n1[i] == n2[i]:
        b += 1
    if n1[i] not in n2:
        hlp += 1
print(b, 4 - hlp - b)