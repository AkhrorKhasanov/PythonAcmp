n = int(input())
c = 0
if n > 0:
    for i in range(1, n + 1):
        c += i
elif n < 0:
    for i in range(n, 2):
        c += i
else:
    c = 1
print(c)    