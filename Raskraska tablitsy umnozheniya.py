n, m = map(int, input().split())
red = green = blue = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        num = i * j
        if not num % 5:
            blue += 1
        if not num % 3 and num % 5:
            green += 1
        if not num % 2 and num % 3 and num % 5:
            red += 1
black = n * m - red - green - blue
print(f"RED : {red}")
print(f"GREEN : {green}")
print(f"BLUE : {blue}")
print(f"BLACK : {black}")