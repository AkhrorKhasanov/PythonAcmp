s = input()
c = 0
lst = [0]
for i in s:
    if i == '1':
        c += 1
    else:
        c -= 1
    lst.append(c)
print(max(lst) - min(lst) + 1)