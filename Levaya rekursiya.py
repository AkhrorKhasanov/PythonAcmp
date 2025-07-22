n = int(input())
c = 0
for i in range(n):
    s = input()
    if s[3] == s[0]:
        c += 1
print(c)