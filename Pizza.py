n = int(input())
def solve(n):
    if n == 1:
        return 2
    return solve(n - 1) + n
print(solve(n))