n, m = map(int, input().split())
lst = list(map(int, input().split()))
mini = max(lst)
maksi = sum(lst) - n + 1
if mini <= m <= maksi:
    print('yes')
else:
    print('no')