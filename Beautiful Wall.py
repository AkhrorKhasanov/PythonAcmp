k = int(input())
n = int(k ** 0.5) + 1
mini = 1000000000
for i in range(1, n + 1):
    var = k // i
    let = abs(var - i) + k - var * i
    if let < mini:
        mini = let
        h, w = i, var
print(h, w)