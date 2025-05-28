s = input()
s1 = s[0]
s2 = s[-1]
data = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8
}
if (data[s1] + data[s2]) % 2 == 0:
    print('BLACK')
else:
    print('WHITE')