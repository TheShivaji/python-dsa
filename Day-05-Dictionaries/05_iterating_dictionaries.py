# ============================================================
# Day-05 | 05 - Iterating Dictionaries
# ============================================================

# Dictionary par loop chalane ke 3 tarike:
#
#   for key in d:           → keys par loop
#   for key in d.keys():    → keys par loop (explicit)
#   for val in d.values():  → values par loop
#   for k, v in d.items():  → key aur value dono
#
# Example:
#   for k, v in person.items():
#       print(k, "→", v)


# ============================================================
# Q1 ⭐ — Print All Keys
# ============================================================

# for loop use karke saari keys print karo (ek-ek line pe).
#
# Expected:
#   name
#   age
#   city

person = {"name": "Shivaji", "age": 21, "city": "Mumbai"}

# 👇 Apna solution yahan likho:
for key in person:
    print(key)


# ============================================================
# Q2 ⭐ — Print All Values
# ============================================================

# Same dictionary — sirf values print karo.
#
# Expected:
#   Shivaji
#   21
#   Mumbai

# 👇 Apna solution yahan likho:
for val in person.values():
    print(val)


# ============================================================
# Q3 ⭐⭐ — Print Key → Value Pairs
# ============================================================

# items() use karke sab print karo in this format:
#   name → Shivaji
#   age  → 21
#   city → Mumbai

# 👇 Apna solution yahan likho:
for key, val in person.items():
    print(f"{key} → {val}")


# ============================================================
# Q4 ⭐⭐ — Count Keys
# ============================================================

# Loop lagao aur count karo ki dictionary me kitni keys hain.
# ⚠️ len() use nahi karna.
#
# Expected: 5

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "version": "2.0",
    "ssl": False
}

# 👇 Apna solution yahan likho:
count = 0
for key in config:
    count += 1
print(count)


# ============================================================
# Q5 ⭐⭐ — Sum of Values
# ============================================================

# Loop use karke saare values ka sum nikalo.
# ⚠️ sum() use nahi karna.
#
# Expected: 450

scores = {"Math": 90, "Python": 95, "DSA": 85, "English": 80, "Science": 100}

# 👇 Apna solution yahan likho:
total_sum = 0
for val in scores.values():
    total_sum += val
print(total_sum)


# ============================================================
# Q6 ⭐⭐ — Find Highest Score
# ============================================================

# Loop use karke highest marks wala subject aur uske marks print karo.
# ⚠️ max() use nahi karna.
#
# Expected:
#   Science → 100

# 👇 Apna solution yahan likho (same scores dict):
highest_score = 0
top_subject = ""
for subject, score in scores.items():
    if score > highest_score:
        highest_score = score
        top_subject = subject
print(f"{top_subject} → {highest_score}")


# ============================================================
# Q7 ⭐⭐⭐ — Filter by Value
# ============================================================

# Sirf woh products print karo jinka price 5000 se zyada ho.
#
# Expected:
#   laptop → 60000
#   monitor → 15000

products = {
    "mouse": 800,
    "laptop": 60000,
    "keyboard": 1500,
    "monitor": 15000,
    "usb_hub": 600
}

# 👇 Apna solution yahan likho:
for product, price in products.items():
    if price > 5000:
        print(f"{product} → {price}")


# ============================================================
# Q8 ⭐⭐⭐ — Search by Value
# ============================================================

# User se ek city name lo.
# Woh city jis employee ki hai uska naam print karo.
# Agar nahi mila → "No employee found in that city"
#
# employees = {
#     "Amit": "Mumbai",
#     "Rahul": "Delhi",
#     "Shivaji": "Pune",
#     "Rohit": "Mumbai"
# }
#
# Example:
#   Enter city: Mumbai   → Amit, Rohit

employees = {
    "Amit": "Mumbai",
    "Rahul": "Delhi",
    "Shivaji": "Pune",
    "Rohit": "Mumbai"
}

# 👇 Apna solution yahan likho:
# search_city = input("Enter city: ")
# found = False
# for emp, city in employees.items():
#     if city == search_city:
#         print(emp)
#         found = True
# if not found:
#     print("No employee found in that city")


# ============================================================
# Q9 ⭐⭐⭐ — Formatted Report
# ============================================================

# Loop se har student ka formatted report print karo:
#
# Expected:
#   -------------------------
#   Student  : Amit
#   Marks    : 75
#   Grade    : C
#   -------------------------
#   (grade: >=90 A, >=75 B, >=60 C, else F)

students = {
    "Amit": 75,
    "Rahul": 92,
    "Shivaji": 58,
    "Rohit": 83
}

# 👇 Apna solution yahan likho:
for student, mark in students.items():
    print("-" * 25)
    print(f"Student  : {student}")
    print(f"Marks    : {mark}")
    
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Grade    : {grade}")
print("-" * 25)


# ============================================================
# Q10 🧠 — Invert a Dictionary
# ============================================================

# keys aur values ko swap karo using a loop.
# (keys ban jaye values, values ban jaye keys)
#
# original   = {"a": 1, "b": 2, "c": 3}
# Expected   = {1: "a", 2: "b", 3: "c"}

original = {"a": 1, "b": 2, "c": 3}

# 👇 Apna solution yahan likho:
inverted = {}
for key, val in original.items():
    inverted[val] = key
print(inverted)


# ============================================================
# ✅ Day 05 | 05 - Iterating Dictionaries Complete
# ============================================================
