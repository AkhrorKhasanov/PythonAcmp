n = int(input())
t = bin(n)[2:]
def solve(smth):
    while len(smth) < len(t):
        smth = '0' + smth
    return smth
maksi = n
for i in range(len(t)):
    t = solve(t[-1] + t[:-1])
    res = int(t, 2)
    if res > maksi:
        maksi = res
print(maksi)