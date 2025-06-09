n, m = map(int, input().split())
if n == 0 and m > 0:
    print("Impossible") 
elif n == 0 and m == 0:
    print("0 0")
elif m == 0:
    print(n, n)
else:
    min_price = n + max(0, m - n)
    max_price = n + m - 1
    print(min_price, max_price)
