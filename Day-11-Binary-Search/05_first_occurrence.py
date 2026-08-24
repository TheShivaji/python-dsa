def first_occurrence(numbers, target):

    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            first = mid
            end = mid - 1

        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return first


numbers = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(first_occurrence(numbers, target))
