n = int(input())
lst = list(map(int, input().split()))
a = b = i = 0
while lst:
    if lst[0] >= lst[-1]:
        e = lst.pop(0)
    else:
        e = lst.pop(len(lst) - 1)
    if not i % 2:
        a += e
    else:
        b += e
    i += 1
print(f"{a}:{b}")