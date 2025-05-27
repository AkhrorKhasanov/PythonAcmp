lst = list(map(int, input().split()))
lst1 = lst[:3]
lst2 = lst[3:]
lst1.sort() 
lst2.sort()
c = 0
for i in range(3):
    c += lst1[i] * lst2[i]
print(c)