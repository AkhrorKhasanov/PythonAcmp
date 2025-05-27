from math import log2
n = int(input())
if n <= 0:
    print("NO")
elif log2(n).is_integer():
    print("YES")
else:
    print("NO")
