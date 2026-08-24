def target_exists(numbers, target):

    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


numbers = [2, 5, 8, 12, 16, 23, 38, 45]
target = 23

print(target_exists(numbers, target))
