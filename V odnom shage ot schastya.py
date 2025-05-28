n = int(input())
def is_lucky(num):
    return int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5])
        
for i in range(n):
    num = int(input())
    n1 = num - 1
    n2 = num + 1
    n1 = '0' * (6 - len(str(n1))) + str(n1)
    n2 = '0' * (6 - len(str(n2))) + str(n2)
    if is_lucky(n1) or is_lucky(n2):
        print("Yes")
    else:
        print("No")
    