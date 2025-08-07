n, k = map(str, input().split())
n = int(n)
k = len(k)
p = 1
if n % k:
    for i in range(n, n % k - 1, -k):
        p *= i
else:
    for i in range(n, k - 1, -k):
        p *= i
print(p)