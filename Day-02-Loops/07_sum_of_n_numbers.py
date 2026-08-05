# Sum of First N Numbers

number = int(input("Enter a Number: "))

total = 0

for i in range(1, number + 1):
    total += i

print(f"Sum = {total}")
