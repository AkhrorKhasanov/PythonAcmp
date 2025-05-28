n = int(input())
c = 0
while True:
    if n == 1:
        break
    if n % 2 == 1:
        c += 1
    n //= 2
print(c + 1)