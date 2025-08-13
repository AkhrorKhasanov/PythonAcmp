n = int(input())
lst = list(map(int, input().split()))
ind = lst.index(1)
res = lst[ind:] + lst[:ind]
print(*res)