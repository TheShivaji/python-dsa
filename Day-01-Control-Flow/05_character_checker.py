# Character Checker

ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

elif ch.isdigit():
    print("Digit")

else:
    print("Special Character")
