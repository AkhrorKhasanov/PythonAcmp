n = int(input()) 
if n > 8: 
    print(n - 8, end=' ') 
if (n - 1) % 8 != 0: 
    print(n - 1, end=' ') 
if n % 8 != 0: 
    print(n + 1, end=' ') 
if n < 57: 
    print(n + 8, end=' ')