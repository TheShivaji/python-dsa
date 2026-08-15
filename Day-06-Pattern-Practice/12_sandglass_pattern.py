n = 5

for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces , stars)

for j in range(2 , n+1):
    spaces = " " * (n - j)
    stars = "*" * (2 * j - 1)
    print(spaces , stars)
