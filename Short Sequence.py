n = int(input())
i = 0
k = 0
while True:
    if i == n:
        break
    k += 1
    for j in range(1, k + 1):
        for z in range(len(str(j))):
            i += 1
            if i == n:
                res = str(j)[z]
                break
        if i == n:
            break
print(res)