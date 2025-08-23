n = int(input())
lst = list(map(int, input().split()))
data = {}
for i in range(len(lst)):
    data[lst[i]] = i + 1
data = dict(sorted(data.items()))
for k, v in data.items():
    print(v, end=' ')