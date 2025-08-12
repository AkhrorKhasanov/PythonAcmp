n = int(input())
lst = list(map(int, input().split()))
data = {}
for i in lst:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1
hlp = []
maksi = 0
c = 0
for k, v in data.items():
    if v > maksi:
        maksi = v
        res = k
for k, v in data.items():
    if v == maksi:
        c += 1
if c > 1:
    print(0)
else:
    print(res)