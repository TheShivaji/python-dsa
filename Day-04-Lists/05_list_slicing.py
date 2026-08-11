# ============================================================
#          Day-04 | 05 - List Slicing
# ============================================================


# Q1 ⭐ — First 3
# numbers = [10, 20, 30, 40, 50]
# Slicing se [10, 20, 30] nikalo.

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])



# -------------------------------------------------------

# Q2 ⭐ — Last 3
# Same list se slicing use karke [30, 40, 50] nikalo.

print(numbers[2:])

# -------------------------------------------------------

# Q3 ⭐⭐ — Middle Elements
# numbers = [10, 20, 30, 40, 50, 60]
# Slicing se [20, 30, 40, 50] nikalo.

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:5])



# -------------------------------------------------------

# Q4 ⭐⭐ — First Half
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[0:4])



# -------------------------------------------------------

# Q5 ⭐⭐ — Second Half
# Same list se [5, 6, 7, 8] nikalo.

print(numbers[4:])


# -------------------------------------------------------

# Q6 ⭐⭐ — Every Second Element
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Output: [1, 3, 5, 7]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[::2])


# -------------------------------------------------------

# Q7 ⭐⭐ — Reverse List
# numbers = [10, 20, 30, 40, 50]
# Slicing se reverse karo: [50, 40, 30, 20, 10]

numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])


# -------------------------------------------------------

# Q8 ⭐⭐⭐ — Reverse Every Second Element
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected: [8, 6, 4, 2]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(numbers[7:0:-2])



# -------------------------------------------------------

# Q9 ⭐⭐⭐ — Copy Using Slicing
# languages = ["Python", "JavaScript", "Java", "C++"]
# Slicing ka use karke new list copy banao.
# Then: copy_languages.append("Go")
# Check karo ki original list me "Go" add hua ya nahi.
# Expected:
#   Original: ["Python", "JavaScript", "Java", "C++"]
#   Copy:     ["Python", "JavaScript", "Java", "C++", "Go"]
# 🧠 Observe: slicing se banayi copy aur original alag behave karti hain.

languages = ["Python", "JavaScript", "Java", "C++"]

copy = languages[::]

copy.append("Go")
print(languages)
print(copy)



# -------------------------------------------------------

# Q10 🧠 Challenge — Custom Slice
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Slicing use karke [20, 40, 60, 80] nikalo.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1::2])


