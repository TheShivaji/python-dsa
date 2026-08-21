def count_vowel(s):

    vowels = "aeiou"

    count = 0

    for i in s:
        if i.lower() in vowels:
            count += 1

    return count


s = "helloe"
print(count_vowel(s))
