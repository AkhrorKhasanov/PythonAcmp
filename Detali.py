n, m = map(int, input().split())
mini = 101
for i in range(n):
    s = input()
    points = s.count('.')
    if mini > points:
        mini = points
print(mini)