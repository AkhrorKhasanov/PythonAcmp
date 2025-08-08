n, m = map(int, input().split())
lst = list(map(int, input().split()))
hlp = []
for i in lst:
    if i > 0:
        hlp.append(i)
hlp = sorted(hlp, reverse=True)
c = 0
for i in range(len(hlp)):
    if i + 1 > m:
        break
    c += hlp[i]
print(c)