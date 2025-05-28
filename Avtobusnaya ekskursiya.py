n = int(input())
lst = list(map(int, input().split()))
flag = False
for i in range(n):
    if lst[i] <= 437:
        flag = True
        break
if flag:
    print("Crash " + str(i + 1))
else:   
    print("No crash")