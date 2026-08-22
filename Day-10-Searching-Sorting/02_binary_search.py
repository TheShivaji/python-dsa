def binary_search(numbers, target):

    start = 0
    end = len(numbers) - 1

    while start <= end:

        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return -1


numbers = [3, 7, 12, 18, 25, 31, 42, 56, 70]

target = 42

print(binary_search(numbers, target))
