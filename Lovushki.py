n = int(input())
x = [0]
y = [0]
s = 0
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(0)
y.append(0)
for i in range(1, n + 2):
    s += ((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5
print(format(s, '.3f'))