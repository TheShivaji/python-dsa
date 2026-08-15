n = 10

for i in range(1 , n+1):
  row=""
  for j in range (1 , n+1):
    if(j<=i):
      row+=str(j)
    else:
      row+=" "
  print(row)


