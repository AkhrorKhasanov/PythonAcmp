n = int(input())
def solve(lst):
    flag = False
    res = ''
    for i in range(len(lst)):
        if lst[i]:
            flag = True
            break
    if flag and i:
        lst[0], lst[i] = lst[i], lst[0]
    for i in lst:
        res += str(i)
    return int(res)
lst = []
for i in str(n):
    lst.append(int(i))
a = sorted(lst)
b = sorted(lst, reverse=True)
print(solve(a), solve(b))