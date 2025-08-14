import string
import sys
s = input()
lst = list(s)
lst.sort()
data = {}
hlp = string.ascii_uppercase
for i in range(len(s)):
    l = hlp.index(s[i])
    if l > i:
        print('NO')
        sys.exit()
for i in range(len(s)):
    if s[i] in data:
        data[s[i]].append(i + 1)
    else:
        data[s[i]] = [i + 1]
data = dict(sorted(data.items()))
res = []
for k, v in data.items():
    res.extend(v)
print('YES')
print(*res)