def selection_sort(numbers):

    for i in range(0, len(numbers)):
        smallest_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[smallest_index]:
                smallest_index = j
        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

    return numbers


numbers = [29, 10, 14, 37, 13]

print(selection_sort(numbers))
