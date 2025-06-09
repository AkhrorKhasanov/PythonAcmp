import string
s = input()
res = ''
hlp = string.ascii_lowercase
c = 0
i = 0
while i < len(s):
    if s[i] == '0':
        c += 1
    else:
        letter = hlp[c]
        c = 0
        res += letter
    i += 1
print(res)