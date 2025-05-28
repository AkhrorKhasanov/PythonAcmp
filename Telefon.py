a, b, c, t = list(map(int, input().split()))
if t <= a:
    print(t * b)
else:
    print(a * b + (t - a) * c)