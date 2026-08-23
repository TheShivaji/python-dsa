def pratice_linear(numbers, target):
    return_value = []
    for i in range(0, len(numbers)):
        if numbers[i] == target:
                return_value.append(i)

    return return_value


numbers = [5, 2, 8, 2, 9, 2, 4]
target = 2
print(pratice_linear(numbers, target))
