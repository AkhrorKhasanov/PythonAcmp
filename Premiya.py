n, k = map(str, input().split())
n = int(n)
if n == 100:
    base = 12
else:
    base = n % 10 + 2
c = 0
s = str(k)
data = {
    'A': 10,
    'B': 11,
    'C': 12,
}
for i in range(len(s)):
    if s[i] not in data:
        c += int(s[i]) * base ** (len(s) - i - 1)
    else:
        c += int(data[s[i]]) * base ** (len(s) - i - 1)
print(c)