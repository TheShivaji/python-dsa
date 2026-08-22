def linear_search(numbers, target):

    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i

    return -1


numbers = [10, 25, 7, 42, 18, 31]
target = 31

print(linear_search(numbers, target))
