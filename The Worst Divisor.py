n = input()
c = 0
for i in range(len(str(n)) - 1, -1, -1):
    if str(n)[i] != '0':
        break
    c += 1
print('1' + c * '0')