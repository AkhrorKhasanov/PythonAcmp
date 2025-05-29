n = int(input())
# 0 1 1 2 3 5 8 13
a0 = 0
a1 = 1
if n == 0:
    print(a0)
elif n == 1:    
    print(a1)
else:
    for i in range(2, n + 1):
        a2 = a0 + a1
        a0 = a1
        a1 = a2
    print(a2)
