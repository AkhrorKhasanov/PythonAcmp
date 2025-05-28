s = input()
lst = [1, 0, 0]
for i in range(len(s)):
    if s[i] == 'A':
        lst[0], lst[1] = lst[1], lst[0]
    elif s[i] == 'B':
        lst[1], lst[2] = lst[2], lst[1]
    elif s[i] == 'C':
        lst[0], lst[2] = lst[2], lst[0]
print(lst.index(1) + 1)