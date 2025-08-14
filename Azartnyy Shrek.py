n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(2 * sum(lst[-n // 2:]) - sum(lst))