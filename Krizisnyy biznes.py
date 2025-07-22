n, s = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
i = 0
while lst:
    if sum(lst[:n - i]) <= s:
        res = n - i
        break
    i += 1
if not lst:
    res = 0
print(res)