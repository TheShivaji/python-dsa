numbers = [1, 2, 3, 4, 5, 6]

Even = 0
Odd = 0

for num in numbers:
    if num % 2 == 0:
        Even = Even+1
    else:
        Odd =Odd+1
print(Even)
print(Odd)
