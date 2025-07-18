import math
def find_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

sx, sy = map(int, input().split())
ix, iy = map(int, input().split())
num = int(input())
result = num + 1
found = False
for i in range(num):
    ux, uy = map(int, input().split())
    ds = find_distance(sx, sy, ux, uy)
    di = find_distance(ix, iy, ux, uy)
    if di / 2.0 >= ds:
        if i + 1 < result:
            result = i + 1
            found = True
if found:
    print(result)
else:
    print("NO")
