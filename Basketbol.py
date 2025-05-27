one = 0
two = 0
for i in range(4):
    a, b = list(map(int, input().split()))
    one += a
    two += b
if one > two:
    print(1)
elif one < two:
    print(2)    
else:
    print("DRAW")  