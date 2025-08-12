s = input()
def solve(s, c):
    if len(s) < 2:
        return s, c
    k = 0
    for i in s:
        k += int(i)
    k = str(k)
    c += 1
    return solve(k, c)
res = solve(s, 0)
print(res[0], res[1])