n = int(input())
one = 0
two = 0 
for i in range(n):
    num = int(input())
    if num == 0:
        one += 1
    elif num == 1:
        two += 1
print(min(one, two))