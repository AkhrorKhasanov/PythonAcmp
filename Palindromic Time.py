from datetime import datetime
s = input()
t1 = datetime.strptime(s, "%H:%M").time()
lst = []
for i in range(3):
    for j in range(6):
        hlp = f"{i}{j}:{j}{i}"
        lst.append(hlp)
lst = lst[:-2]
flag = None
for i in lst:
    t2 = datetime.strptime(i, "%H:%M").time()
    if t2 > t1:
        print(i)
        flag = True
        break
if not flag:
    print(lst[0])