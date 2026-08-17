def check_unique(numbers):
    seen = []

    for num in numbers:
        if num in seen:
            return False

        seen.append(num)

    return True


numbers = [1, 2, 3, 4, 5]

print(check_unique(numbers))
