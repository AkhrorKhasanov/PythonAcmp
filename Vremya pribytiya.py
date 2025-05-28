s = input()
t = input()
h = int(s[:2])
m = int(s[3:])
ind = t.index(' ')
h2 = int(t[:ind])
m2 = int(t[ind + 1:])
m3 = (m + m2) % 60
h3 = (h + h2 + (m + m2) // 60) % 24
if h3 < 10:
    h3 = '0' + str(h3)
else:
    h3 = str(h3)
if m3 < 10:
    m3 = '0' + str(m3)
else:
    m3 = str(m3)
print(h3 + ':' + m3)