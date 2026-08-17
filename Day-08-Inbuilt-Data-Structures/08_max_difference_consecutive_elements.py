numbers = [10, 3, 8, 20, 5]

max_difference = 0

for i in range(len(numbers) - 1):
    current_dif = numbers[i] - numbers[i + 1]

    if abs(current_dif) > max_difference:
        max_difference = current_dif


print(max_difference)
