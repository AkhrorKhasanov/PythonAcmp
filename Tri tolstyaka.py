lst = list(map(int, input().split()))
flag = True
for i in range(len(lst)):
    if not 94 <= lst[i] <= 727:
        flag = False
        break
if flag:
    print(max(lst))
else:
    print('Error')
    