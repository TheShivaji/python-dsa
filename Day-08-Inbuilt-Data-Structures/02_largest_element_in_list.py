numbers = [3, 8, 2, 10, 5]
largest_num = 0
for num in numbers:
    if num > abs(largest_num):
        largest_num = num

print(largest_num)
