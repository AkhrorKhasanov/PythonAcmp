n, m = map(int, input().split())
data = {}
mini = m * 1000 + 1
for i in range(n):
    s = input()
    lst = list(map(int, input().split()))
    data[s] = sum(lst)
    if mini > sum(lst):
        mini = sum(lst)
for k, v in data.items():
    if v == mini:
        print(k)
        break
