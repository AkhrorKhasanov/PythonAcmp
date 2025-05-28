n = int(input())
lst = list(map(int, input().split()))
lst1 = []
lst2 = []
for i in lst:
    if i % 2 == 0:
        lst1.append(i)
    else:
        lst2.append(i)
print(*lst2)
print(*lst1)
if len(lst1) >= len(lst2):
    print("YES")    
else:
    print("NO")