n = int(input())
lst = list(map(int, input().split()))
if n == 1:
    print(lst[0])
else:
    print(sum(lst) - n + 1)