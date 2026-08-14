n = 5

for i in  range(n):
  row=""
  for j in range(n):
    if(  j <= i):
      row+='*'
    else:
      row+=' '
  print(row)
