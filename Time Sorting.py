n = int(input())
lst = []
for i in range(n):
    h, m, s = map(int, input().split())
    lst.append(h * 3600 + m * 60 + s)
lst.sort()
for i in lst:
    print(f"{i // 3600} {(i // 60) % 60} {i % 60}")