# ============================================================
# Day-05 | 08 - Practical Examples
# ============================================================

# Concepts Used:
# - Dictionary CRUD (Create, Read, Update, Delete)
# - Nested dictionaries
# - Loops + conditions
# - Dictionary methods
# - User input


# ============================================================
# Q1 ⭐⭐ — Word Frequency Counter
# ============================================================

# Ek sentence lo aur har word kitni baar aaya
# wo dictionary me store karo.
#
# sentence = "the cat sat on the mat the cat"
#
# Expected:
#   {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

sentence = "the cat sat on the mat the cat"

# 👇 Apna solution yahan likho:


# ============================================================
# Q2 ⭐⭐ — Phone Book
# ============================================================

# User se naam lo aur phone book me number dhundo.
# Agar mila → number print karo
# Nahi mila → "Contact Not Found"
#
# phonebook = {
#     "Amit":    "9876543210",
#     "Rahul":   "9123456780",
#     "Shivaji": "9988776655"
# }

phonebook = {
    "Amit":    "9876543210",
    "Rahul":   "9123456780",
    "Shivaji": "9988776655"
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q3 ⭐⭐⭐ — Product Cart
# ============================================================

# User se product name lo aur cart me add karo.
# Agar product already cart me hai → quantity badha do.
# Warna → new entry banao with quantity 1.
# Phir cart print karo.
#
# Example Interaction:
#   Add product: apple  → cart = {"apple": 1}
#   Add product: apple  → cart = {"apple": 2}
#   Add product: banana → cart = {"apple": 2, "banana": 1}
#
# Hint: Loop me user se products lo jab tak "quit" nahi type karta.

# 👇 Apna solution yahan likho:


# ============================================================
# Q4 ⭐⭐⭐ — Student Report Card
# ============================================================

# Har student ke liye grade calculate karo aur report print karo.
# Grade:
#   >= 90 → A
#   >= 75 → B
#   >= 60 → C
#   else  → F
#
# Expected:
#   ======== REPORT CARD ========
#   Amit     : 75 marks → Grade B
#   Rahul    : 92 marks → Grade A
#   Shivaji  : 58 marks → Grade F
#   Rohit    : 83 marks → Grade B

students = {
    "Amit":    75,
    "Rahul":   92,
    "Shivaji": 58,
    "Rohit":   83
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q5 ⭐⭐⭐ — Inventory Manager
# ============================================================

# User se product aur quantity sold lo.
# Inventory update karo.
# Agar stock nahi → "Out of Stock"
# Agar product nahi → "Product Not Found"
# Phir updated inventory print karo.

inventory = {
    "laptop":   {"price": 60000, "stock": 5},
    "mouse":    {"price": 1000,  "stock": 20},
    "keyboard": {"price": 2000,  "stock": 10}
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q6 ⭐⭐⭐ — Leaderboard
# ============================================================

# scores dictionary me se Top 3 players
# descending order me print karo.
# ⚠️ sorted() use kar sakte ho.
#
# Expected:
#   1. Shivaji → 310
#   2. Rohit   → 275
#   3. Amit    → 250

scores = {
    "Amit":    250,
    "Rahul":   180,
    "Shivaji": 310,
    "Rohit":   275,
    "Priya":   120
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q7 ⭐⭐⭐⭐ — Expense Tracker
# ============================================================

# User se category aur amount lo (loop me, "done" pe exit).
# Same category ka amount add hota rahe.
# Phir:
#   - Har category ka total
#   - Grand total
# print karo.
#
# Example:
#   Category: food    Amount: 200
#   Category: travel  Amount: 500
#   Category: food    Amount: 150
#   Category: done
#
#   food   → ₹350
#   travel → ₹500
#   Total  → ₹850

# 👇 Apna solution yahan likho:


# ============================================================
# Q8 ⭐⭐⭐⭐ — Duplicate Finder
# ============================================================

# items list me se duplicate values dhundo
# aur ek dictionary me store karo:
#   key = item, value = count (sirf woh jo > 1 baar aaye)
#
# items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
#
# Expected: {'apple': 3, 'banana': 2}

items = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# 👇 Apna solution yahan likho:


# ============================================================
# Q9 ⭐⭐⭐⭐ — Config Merger
# ============================================================

# default_config aur user_config hain.
# user_config se override karo default_config ke values.
# Jo keys user_config me nahi hain woh default se rehne do.
# Final merged config print karo.
#
# Expected:
#   {
#     "theme": "light",     ← user override
#     "language": "Python", ← default
#     "font_size": 16,      ← user override
#     "debug": False,       ← default
#     "notifications": True ← user added
#   }

default_config = {
    "theme":         "dark",
    "language":      "Python",
    "font_size":     14,
    "debug":         False
}

user_config = {
    "theme":         "light",
    "font_size":     16,
    "notifications": True
}

# 👇 Apna solution yahan likho:


# ============================================================
# Q10 🧠 — Mini Contact Manager
# ============================================================

# Menu-based program:
#
#   ====== CONTACT MANAGER ======
#   1. View All Contacts
#   2. Search Contact
#   3. Add Contact
#   4. Delete Contact
#   5. Exit
#
# contacts = {
#     "Amit":    "9876543210",
#     "Rahul":   "9123456780",
#     "Shivaji": "9988776655"
# }
#
# Requirements:
#   1 → Saare contacts print karo
#   2 → Naam se number search karo
#   3 → New naam + number add karo
#   4 → Naam se contact delete karo
#   5 → Program exit karo

contacts = {
    "Amit":    "9876543210",
    "Rahul":   "9123456780",
    "Shivaji": "9988776655"
}

# 👇 Apna solution yahan likho:


# ============================================================
# ✅ Day 05 | 08 - Practical Examples Complete
# ============================================================
