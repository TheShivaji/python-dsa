# Find the Largest Number

def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)


numbers = [12, 45, 7, 89, 33]
print("Numbers:", numbers)
print("Largest number:", find_largest(numbers))
