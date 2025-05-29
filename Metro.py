n, i, j = map(int, input().split())
if j > i:
    one = j - i - 1
else:
    one = i - j - 1
two = n - one - 2
print(min(one, two))