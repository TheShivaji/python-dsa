n = 6
number = 1

for i in range(1 , n+1):
    row = ""
    for j in range(1 , n+1):
        if(j<=i):
            row += str(number) + " "
            number+=1
        else:
            row+=" "

    print(row)
