n, v, l = map(int, input().split())
lst = list(map(int, input().split()))
s = l * 60 / v
for i in range(len(lst)):
    if i % 2:
        s += lst[i]
print(format(s, '.2f'))