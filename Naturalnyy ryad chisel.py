n = input()
s = ''
for i in range(1, 10001):
    if n in s:
        break
    for j in range(len(str(i))):
        if n in s:
            break
        s += str(i)[j]
print(len(s) - len(n) + 1)