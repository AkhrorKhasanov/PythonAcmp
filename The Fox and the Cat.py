n = int(input())
i = 0
while (n - 3 * i) % 5 != 0:
    i += 1
print((n - 3 * i) // 5, i)