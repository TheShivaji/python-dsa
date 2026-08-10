# Count Vowels

def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)


print(count_vowels("Hello World"))
print(count_vowels("Python Programming"))
