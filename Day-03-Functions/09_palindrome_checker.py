# Palindrome Checker

def is_palindrome(text):
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


print(is_palindrome("madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))
