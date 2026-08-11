# ============================================================
#          Day-04 | 02 - Accessing Elements
# ============================================================


# Q1 — First Element ⭐
# languages = ["Python", "JavaScript", "Java", "C++", "Go"]
# First element print karo.
# Expected: Python



languages = ["Python", "JavaScript", "Java", "C++", "Go"]

print(languages[0])



# -------------------------------------------------------

# Q2 — Last Element ⭐
# Same list se last element print karo.
# Expected: Go

print(languages[-1])



# -------------------------------------------------------

# Q3 — Third Element ⭐
# Third element access karo.
# Expected: Java

print(languages[2])



# -------------------------------------------------------

# Q4 — Second-Last Element ⭐⭐
# Negative indexing use karke second-last element print karo.
# ⚠️ Positive index use nahi karna.
# Expected: C++

print(languages[-2])



# -------------------------------------------------------

# Q5 — First 3 Elements ⭐⭐
# numbers = [10, 20, 30, 40, 50]
# First 3 elements access karo.
# Expected: [10, 20, 30]

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

# -------------------------------------------------------

# Q6 — Specific Elements ⭐⭐
# colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
# Print: Red, Blue, Purple

colors = ["Red", "Green", "Blue", "Yellow", "Purple"]

print(colors[::2])

# -------------------------------------------------------

# Q7 — Negative Indexing Practice ⭐⭐
# items = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
# Negative indexing se print karo:
#   - Last item
#   - Third-last item
#   - First item

items = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

print(items[-1])
print(items[-3])
print(items[0])


# -------------------------------------------------------

# Q8 — User Choice ⭐⭐⭐
# languages = ["Python", "JavaScript", "TypeScript", "Java", "C++"]
# User se index lo aur us index par jo language hai wo print karo.
# ⚠️ Abhi invalid index handling ki zarurat nahi.
# Example:
#   Enter index: 2
#   TypeScript

languages = ["Python", "JavaScript", "TypeScript", "Java", "C++"]

user_index = int(input("Enter index: "))

print(languages[user_index])



# -------------------------------------------------------

# Q9 — Reverse Access ⭐⭐⭐
# numbers = [10, 20, 30, 40, 50]
# Negative indexing use karke poori list ko reverse order me print karo.
# Expected:
#   50
#   40
#   30
#   20
#   10

numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])

# -------------------------------------------------------

# Q10 — Challenge 🧠
# students = ["Amit", "Rahul", "Shivaji", "Rohit", "Akash"]
# Sirf indexing use karke print karo:
#   First Student: Amit
#   Middle Student: Shivaji
#   Last Student: Akash

students = ["Amit", "Rahul", "Shivaji", "Rohit", "Akash"]

print("First Student:",students[0])
print("Middle Student:",students[2])
print("Last Student:",students[-1])


