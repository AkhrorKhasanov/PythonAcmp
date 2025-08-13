n = int(input())
c = 0
data = {}
for i in range(n):
    m = int(input())
    c += m
    for j in range(m):
        num, name = map(str, input().split())
        num = float(num)
        data[name] = num
data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print(c)
for k, v in data.items():
    print(f"{format(v, '.2f')} {k}")