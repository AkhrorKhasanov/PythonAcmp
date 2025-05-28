k, s = list(map(str, input().split()))
k = int(k)
s = s.strip()
print(s[:k - 1] + s[k:])