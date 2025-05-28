n = int(input())
lst = list(map(int, input().split()))
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(*lst[a - 1 : b])