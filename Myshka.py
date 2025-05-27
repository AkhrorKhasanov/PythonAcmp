w, h, r = list(map(int, input().split()))
if r * 2 <= w and r * 2 <= h:
    print("YES")    
else:
    print("NO")