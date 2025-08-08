n = float(input())
c = 0
s = 0
i = 1
while n > s:
    c += 1
    s += 1 / (i + 1)
    i += 1
print(f"{c} card(s)")