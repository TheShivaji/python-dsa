n = 5

for i in range(n, 0, -1):
    row = ""

    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            row += "*"
        else:
            row += " "

    print(row)
