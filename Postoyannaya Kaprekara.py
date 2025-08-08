n = input()
lst = [n]
def add_zero(n):
    while len(n) < 4:
        n = '0' + n
    return n
def help_me(lst):
    n = ''
    for i in lst:
        n += str(i)
    return add_zero(n)
def solve(n):
    hlp = []
    for i in n:
        hlp.append(int(i))
    l1 = sorted(hlp)
    l2 = sorted(hlp, reverse=True)
    return add_zero(str(int(help_me(l2)) - int(help_me(l1))))
c = 0
while lst[-1] != solve(lst[-1]):
    c += 1
    lst.append(solve(lst[-1]))
print(lst[-1])
print(c) 