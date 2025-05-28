n = int(input())
maks = n * 6
six = n // 6
five = (n % 6) // 5
four = (n % 6 % 5) // 4
three = (n % 6 % 5 % 4) // 3
two = (n % 6 % 5 % 4 % 3) // 2
one = n % 6 % 5 % 4 % 3 % 2
minn = six + 2 * five + 3 * four + 4 * three + 5 * two + one * 6
print(minn, maks)