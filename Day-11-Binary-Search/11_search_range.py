def search_range(numbers, target):

    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] > target:
            end = mid - 1
        elif numbers[mid] == target:
            return mid
        else:
            start = mid + 1
    return start


numbers = [1, 3, 5, 6]
target = 7

print(search_range(numbers, target))
