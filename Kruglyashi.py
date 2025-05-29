n = input()
data = {
    '0': 1,
    '6': 1,
    '8': 2,
    '9': 1,
}
c = 0
for i in n:
    if i in data:
        c += data[i]
print(c)