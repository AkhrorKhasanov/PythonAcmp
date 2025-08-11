n = int(input())
N, a, b, c = map(int, input().split())
if n == 2:
    print(min(a, b, c))
else:
    print(max(a + b + c - 2 * N, 0))