n = 5

for i in range(1, n + 1):
    row = ""

    # Spaces
    row += " " * (n - i)

    # Numbers
    for j in range(1, 2 * i):
        row += str(j)

    print(row)
