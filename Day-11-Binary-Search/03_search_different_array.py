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

numbers = [4, 9, 15, 21, 28, 36, 47, 59, 72]
target =30

print(binary_search(numbers, target))
