# ============================================================
# Day-04 | 07 - List Comprehension
# ============================================================

# Syntax:
# [expression for item in iterable]
# [expression for item in iterable if condition]


# ============================================================
# Q1 ⭐ — Basic Comprehension
# ============================================================

# Create a new list containing the same numbers.
#
# numbers = [1, 2, 3, 4, 5]
# Expected: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]

new_list = [num for num in numbers]

print("Q1:", new_list)


# ============================================================
# Q2 ⭐⭐ — Squares
# ============================================================

# Create a new list containing the square of each number.
#
# numbers = [1, 2, 3, 4, 5]
# Expected: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print("Q2:", squares)


# ============================================================
# Q3 ⭐⭐ — Double Numbers
# ============================================================

# Multiply every number by 2.
#
# numbers = [1, 2, 3, 4, 5]
# Expected: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]

doubled_numbers = [num * 2 for num in numbers]

print("Q3:", doubled_numbers)


# ============================================================
# Q4 ⭐⭐ — Even Numbers
# ============================================================

# Create a new list containing only even numbers.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]

print("Q4:", even_numbers)


# ============================================================
# Q5 ⭐⭐ — Odd Numbers
# ============================================================

# Create a new list containing only odd numbers.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected: [1, 3, 5, 7, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Q5:", odd_numbers)


# ============================================================
# Q6 ⭐⭐⭐ — Squares of Even Numbers
# ============================================================

# Create a list containing the squares of only even numbers.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Expected: [4, 16, 36]

numbers = [1, 2, 3, 4, 5, 6]

even_squares = [num ** 2 for num in numbers if num % 2 == 0]

print("Q6:", even_squares)


# ============================================================
# Q7 ⭐⭐⭐ — Positive Numbers
# ============================================================

# Create a list containing only positive numbers.
# Zero should not be included.
#
# numbers = [-10, 5, -3, 20, 0, 15, -7]
# Expected: [5, 20, 15]

numbers = [-10, 5, -3, 20, 0, 15, -7]

positive_numbers = [num for num in numbers if num > 0]

print("Q7:", positive_numbers)


# ============================================================
# Q8 ⭐⭐⭐ — Convert Strings to Uppercase
# ============================================================

# Convert all names to uppercase.
#
# names = ["shivaji", "rahul", "amit"]
# Expected: ["SHIVAJI", "RAHUL", "AMIT"]

names = ["shivaji", "rahul", "amit"]

uppercase_names = [name.upper() for name in names]

print("Q8:", uppercase_names)


# ============================================================
# Q9 ⭐⭐⭐ — Length Filter
# ============================================================

# Keep only names whose length is greater than 5.
#
# names = ["Ram", "Shivaji", "Amit", "Rahul", "Alexander"]
# Expected: ["Shivaji", "Alexander"]

names = ["Ram", "Shivaji", "Amit", "Rahul", "Alexander"]

long_names = [name for name in names if len(name) > 5]

print("Q9:", long_names)


# ============================================================
# Q10 🧠 — Even Squares
# ============================================================

# Filter even numbers and calculate their squares
# using a single list comprehension.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected: [4, 16, 36, 64, 100]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [num ** 2 for num in numbers if num % 2 == 0]

print("Q10:", even_squares)


# ============================================================
# ✅ Day 04 | List Comprehension Complete
# ============================================================