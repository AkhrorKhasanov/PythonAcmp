import sys
s1, s2 = map(str, input().split())
s1 = s1.lower()
s2 = s2.lower()
data1 = {}
data2 = {}
def help_me(s, data):
    for i in s:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    return data
data1 = help_me(s1, data1)
data2 = help_me(s2, data2)
data1 = dict(sorted(data1.items()))
data2 = dict(sorted(data2.items()))
for i in data1:
    if i not in data2:
        print('No')
        sys.exit()
    if data1[i] != data2[i]:
        print('No')
        sys.exit()
for i in data2:
    if i not in data1:
        print('No')
        sys.exit()
    if data1[i] != data2[i]:
        print('No')
        sys.exit()
print('Yes')