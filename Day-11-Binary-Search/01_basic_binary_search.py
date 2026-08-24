def binary_search(numbers, target):

    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


numbers = [3, 7, 12, 18, 25, 31, 42]
target = 25

print(binary_search(numbers, target))
