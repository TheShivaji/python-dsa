def count_consonants(s):
    vowels_skip = "aeiou"


    count = 0

    for char in s:
        if char in vowels_skip:
            continue

        if char.isalpha():
            count += 1

    return count


s = "hello#$@$111111111"

print(count_consonants(s))
