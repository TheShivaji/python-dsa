# ============================================================
# Day-05 | 07 - Dictionary Comprehension
# ============================================================

# Dictionary Comprehension = ek line me dictionary banana
#
# Syntax:
#   {key_expr: val_expr for item in iterable}
#   {key_expr: val_expr for item in iterable if condition}
#
# Example:
#   squares = {n: n**2 for n in range(1, 6)}
#   → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# Q1 ⭐ — Basic Comprehension
# ============================================================

# 1 se 5 tak numbers ki dictionary banao
# jisme key = number, value = same number.
#
# Expected: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# 👇 Apna solution yahan likho:


# ============================================================
# Q2 ⭐⭐ — Squares
# ============================================================

# 1 se 6 tak har number ka square dictionary banao.
#
# Expected: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# 👇 Apna solution yahan likho:


# ============================================================
# Q3 ⭐⭐ — String Length Map
# ============================================================

# words list se ek dictionary banao:
#   key = word, value = length of word
#
# Expected: {'Python': 6, 'DSA': 3, 'Dictionary': 10, 'Code': 4}

words = ["Python", "DSA", "Dictionary", "Code"]

# 👇 Apna solution yahan likho:


# ============================================================
# Q4 ⭐⭐ — Uppercase Keys
# ============================================================

# original dict ke keys ko uppercase karo using comprehension.
#
# original = {"name": "Shivaji", "age": 21, "city": "Mumbai"}
# Expected  = {"NAME": "Shivaji", "AGE": 21, "CITY": "Mumbai"}

original = {"name": "Shivaji", "age": 21, "city": "Mumbai"}

# 👇 Apna solution yahan likho:


# ============================================================
# Q5 ⭐⭐ — Filtered Dictionary (Value Filter)
# ============================================================

# Sirf woh items rakho jinka price 1000 se zyada ho.
#
# Expected: {'laptop': 60000, 'monitor': 15000}

products = {
    "mouse": 800,
    "laptop": 60000,
    "usb": 400,
    "monitor": 15000,
    "cable": 200
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q6 ⭐⭐⭐ — Invert Dictionary using Comprehension
# ============================================================

# Keys aur values swap karo using comprehension.
#
# original = {1: "one", 2: "two", 3: "three"}
# Expected = {"one": 1, "two": 2, "three": 3}

original = {1: "one", 2: "two", 3: "three"}

# 👇 Apna solution yahan likho:


# ============================================================
# Q7 ⭐⭐⭐ — Passing Students Only
# ============================================================

# Sirf woh students rakho jiske marks >= 60 hain.
#
# Expected: {'Rahul': 82, 'Shivaji': 91, 'Rohit': 70}

marks = {
    "Amit": 45,
    "Rahul": 82,
    "Shivaji": 91,
    "Priya": 38,
    "Rohit": 70
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q8 ⭐⭐⭐ — Grade Assignment
# ============================================================

# Comprehension use karke har student ka grade assign karo:
#   >= 90 → "A"
#   >= 75 → "B"
#   >= 60 → "C"
#   else  → "F"
#
# Expected:
#   {'Amit': 'F', 'Rahul': 'B', 'Shivaji': 'A', 'Priya': 'F', 'Rohit': 'C'}

# 👇 Apna solution yahan likho (same marks dict):


# ============================================================
# Q9 ⭐⭐⭐ — Even Squares Only
# ============================================================

# 1 se 10 tak sirf even numbers ke squares ki dictionary banao.
#
# Expected: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 👇 Apna solution yahan likho:


# ============================================================
# Q10 🧠 — Two-List to Dictionary
# ============================================================

# Do lists hain: ek keys ki, ek values ki.
# zip() aur comprehension use karke dictionary banao.
#
# keys   = ["name", "age", "city", "job"]
# values = ["Shivaji", 21, "Mumbai", "Developer"]
#
# Expected:
#   {'name': 'Shivaji', 'age': 21, 'city': 'Mumbai', 'job': 'Developer'}

keys   = ["name", "age", "city", "job"]
values = ["Shivaji", 21, "Mumbai", "Developer"]

# 👇 Apna solution yahan likho:


# ============================================================
# ✅ Day 05 | 07 - Dictionary Comprehension Complete
# ============================================================
