# ============================================================
#          Day-04 | 04 - List Methods
# ============================================================


# Q1 ⭐ — append()
# languages = ["Python", "JavaScript", "Java"]
# List ke end me "C++" add karo.
# Expected: ["Python", "JavaScript", "Java", "C++"]

languages = ["Python", "JavaScript", "Java"]

languages.append("C++")

print(languages)



# -------------------------------------------------------

# Q2 ⭐ — append() Multiple Times
# numbers = []
# 10, 20, 30, 40, 50 ko one-by-one list me add karo.
# Expected: [10, 20, 30, 40, 50]

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)

print(numbers)



# -------------------------------------------------------

# Q3 ⭐⭐ — insert()
# languages = ["Python", "Java", "C++"]
# JavaScript ko index 1 par insert karo.
# Expected: ["Python", "JavaScript", "Java", "C++"]

languages = ["Python", "Java", "C++"]

languages.insert(1 , "JavaScript")

print(languages)


# -------------------------------------------------------

# Q4 ⭐⭐ — remove()
# languages = ["Python", "JavaScript", "Java", "C++"]
# Java ko remove karo.
# Expected: ["Python", "JavaScript", "C++"]

languages = ["Python", "JavaScript", "Java", "C++"]

languages.remove("Java")

print(languages)



# -------------------------------------------------------

# Q5 ⭐⭐ — pop()
# numbers = [10, 20, 30, 40, 50]
# Last element remove karo aur removed value bhi print karo.
# Expected:
#   Removed: 50
#   Remaining: [10, 20, 30, 40]

numbers = [10, 20, 30, 40, 50]

removed = numbers.pop()
remaining = numbers

print("Removed :" , removed)
print("Remaining :" , remaining)



# -------------------------------------------------------

# Q6 ⭐⭐ — pop(index)
# languages = ["Python", "JavaScript", "Java", "C++", "Go"]
# Index 2 wala element remove karo.
# Expected: ["Python", "JavaScript", "C++", "Go"]

languages = ["Python", "JavaScript", "Java", "C++", "Go"]

removed = languages.pop(2)
remaining = languages

print("Removed :" , removed)
print("Remaining :" , remaining)


# -------------------------------------------------------

# Q7 ⭐⭐ — extend()
# backend = ["Node.js", "Express"]
# frontend = ["React", "Next.js"]
# frontend ki values ko backend list me add karo.
# Expected: ["Node.js", "Express", "React", "Next.js"]

backend = ["Node.js", "Express"]
frontend = ["React", "Next.js"]

backend.extend(frontend)

print(backend)



# -------------------------------------------------------

# Q8 ⭐⭐ — sort()
# numbers = [50, 10, 40, 20, 30]
# Ascending order me sort karo.
# Expected: [10, 20, 30, 40, 50]

numbers = [50, 10, 40, 20, 30]

numbers.sort()
print(numbers)



# -------------------------------------------------------

# Q9 ⭐⭐⭐ — reverse()
# languages = ["Python", "JavaScript", "Java", "C++"]
# List ko reverse karo.
# Expected: ["C++", "Java", "JavaScript", "Python"]

languages = ["Python", "JavaScript", "Java", "C++"]

languages.reverse()
print(languages)



# -------------------------------------------------------

# Q10 ⭐⭐⭐ — clear()
# cart = ["Laptop", "Mouse", "Keyboard"]
# Cart completely empty karo.
# Expected: []

cart = ["Laptop", "Mouse", "Keyboard"]

cart.clear()
print(cart)


