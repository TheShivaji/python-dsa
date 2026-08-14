n = 5
for i in range(n):
    row = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n-1:
            row += "*"
        else:
            row += " "
    print(row)

    
