rows = 4
columns = 6

for i in range(rows):
    row = ""
    for j in range(columns):
        if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
            row += "*"
        else:
            row += " "

    print(row)

# Revision Q2 — Increasing Triangle

n = 5

for i in range(n):
    row = ""
    for j in range(n):
        if j <= i:
            row += "*"
    print(row)


# Revision Q3 — Pyramid

n = 5

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)

    print(spaces ,stars)



#Revision Q4 — Inverted Pyramid

n = 5
for i in range(n , 0 , -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)

    print(spaces , stars)


#Revision Q5 — Floyd's Triangle

n = 5

number = 1;

for i in range (1 , n+1):
    row=""
    for j in range(1 , n+1):
        if j<=i:
            row+=str(number) + " "
            number=number+1
    print(row)

