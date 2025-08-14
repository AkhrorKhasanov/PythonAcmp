n = int(input())
lst = list(map(int, input().split()))
k = int(input())
lst2 = list(map(int, input().split()))
data = {}
for i in range(1, n + 1):
    data[i] = 0
for i in range(k):
    data[lst2[i]] += 1
for i in range(n):
    if data[i + 1] > lst[i]:
        print('yes')
    else:
        print('no')