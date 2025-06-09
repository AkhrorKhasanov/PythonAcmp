a, b, c = map(int, input().split())
A, B, C = map(int, input().split())
x = sorted([a, b, c])
y = sorted([A, B, C])
if x == y:
    print("Boxes are equal")
elif all(x[i] >= y[i] for i in range(3)):
    print("The first box is larger than the second one")
elif all(x[i] <= y[i] for i in range(3)):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
