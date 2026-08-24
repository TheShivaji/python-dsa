def target_not(numbers, target):

    s = 0
    e = len(numbers) - 1

    while s <= e:
        m = (s + e) // 2

        if numbers[m] == target:
            return m
        elif numbers[m] > target:
            e = m - 1
            print(e)
        else:
            s = m + 1
            print(numbers[s])
    return -1


numbers = [5, 11, 18, 24, 31, 40, 52, 67]
target = 50
print(target_not(numbers, target))
