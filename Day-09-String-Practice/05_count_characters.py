def count_characters(s):
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count


s = "Hello World"

print(count_characters(s))
