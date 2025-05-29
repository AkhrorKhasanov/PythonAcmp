s = input()
lst = []
c = 0
for i in s:
    if i == '0':
        c += 1
    else:
        lst.append(c)
        c = 0
lst.append(c)
print(max(lst))