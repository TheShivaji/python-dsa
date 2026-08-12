# ============================================================
# Day-05 | 03 - Modifying Elements
# ============================================================

# Dictionary ko modify karne ke tarike:
#
#   Add new key:      dict["new_key"] = value
#   Update value:     dict["key"] = new_value
#   Delete key:       del dict["key"]
#   Remove & return:  dict.pop("key")
#   Clear all:        dict.clear()


# ============================================================
# Q1 ⭐ — Update a Value
# ============================================================

# student dictionary me "marks" ko 85 se 92 karo.
# Phir updated dictionary print karo.
#
# Expected: {'name': 'Amit', 'age': 20, 'marks': 92}

student = {"name": "Amit", "age": 20, "marks": 85}

# 👇 Apna solution yahan likho:
student["marks"] = 92
print(student)

# ============================================================
# Q2 ⭐ — Add a New Key
# ============================================================

# profile dictionary me ek naya key "email" add karo
# with value "shivaji@gmail.com".
# Phir print karo.

profile = {"name": "Shivaji", "age": 21}

# 👇 Apna solution yahan likho:
profile["email"] = "shivaji@gmail.com"
print(profile)


# ============================================================
# Q3 ⭐⭐ — Delete a Key using del
# ============================================================

# product dictionary se "discount" key delete karo.
# Phir updated dictionary print karo.
#
# Expected: {'name': 'Laptop', 'price': 60000}

product = {"name": "Laptop", "price": 60000, "discount": 5}

# 👇 Apna solution yahan likho:
del product["discount"]
print(product)


# ============================================================
# Q4 ⭐⭐ — pop() Method
# ============================================================

# inventory dictionary se "tablet" ko pop() se remove karo.
# Remove hui value ko ek variable me store karo aur print karo.
# Phir updated dictionary bhi print karo.
#
# Expected:
#   Removed: 8
#   {'laptop': 10, 'mouse': 25}

inventory = {"laptop": 10, "mouse": 25, "tablet": 8}

# 👇 Apna solution yahan likho:
removed_val = inventory.pop("tablet")
print("Removed:", removed_val)
print(inventory)


# ============================================================
# Q5 ⭐⭐ — Add Multiple Keys at Once
# ============================================================

# user dictionary me ek hi line me teen naye keys add karo:
#   "email"   → "rahul@gmail.com"
#   "city"    → "Delhi"
#   "country" → "India"
#
# Hint: update() method use karo
# Phir final dictionary print karo.

user = {"name": "Rahul", "age": 22}

# 👇 Apna solution yahan likho:
user.update({"email": "rahul@gmail.com", "city": "Delhi", "country": "India"})
print(user)


# ============================================================
# Q6 ⭐⭐ — User-Driven Update
# ============================================================

# User se product name aur new price input lo.
# Agar product exist karta hai → price update karo.
# Warna → "Product not found"
#
# products = {
#     "laptop": 60000,
#     "mouse": 1000,
#     "keyboard": 2000
# }

products = {
    "laptop": 60000,
    "mouse": 1000,
    "keyboard": 2000
}

# 👇 Apna solution yahan likho:
# prod_name = input("Product Name: ")
# if prod_name in products:
#     new_price = int(input("New Price: "))
#     products[prod_name] = new_price
#     print(products)
# else:
#     print("Product not found")


# ============================================================
# Q7 ⭐⭐⭐ — Conditional Add
# ============================================================

# User se ek key aur value lo.
# Agar key already exist karta hai → "Key already exists, not updated"
# Agar nahi hai → add karo aur "Added successfully" print karo.
#
# settings = {"theme": "dark", "language": "Python"}

settings = {"theme": "dark", "language": "Python"}

# 👇 Apna solution yahan likho:
# new_key = input("Enter key: ")
# new_val = input("Enter value: ")
# if new_key in settings:
#     print("Key already exists, not updated")
# else:
#     settings[new_key] = new_val
#     print("Added successfully")


# ============================================================
# Q8 ⭐⭐⭐ — Modify Nested Value
# ============================================================

# employee dictionary me "salary" ko 50000 se 65000 karo.
# Phir updated dictionary print karo.

employee = {
    "name": "Shivaji",
    "department": "Engineering",
    "details": {
        "experience": 2,
        "salary": 50000
    }
}

# 👇 Apna solution yahan likho:
employee["details"]["salary"] = 65000
print(employee)


# ============================================================
# Q9 ⭐⭐⭐ — clear() and Rebuild
# ============================================================

# Pehle config dictionary ko clear() se khali karo.
# Phir naye values add karo:
#   "host" → "production.server.com"
#   "port" → 443
#   "ssl"  → True
# Phir print karo.

config = {"host": "localhost", "port": 8080, "debug": True}

# 👇 Apna solution yahan likho:
config.clear()
config.update({"host": "production.server.com", "port": 443, "ssl": True})
print(config)


# ============================================================
# Q10 🧠 — Score Tracker
# ============================================================

# scores dictionary hai.
# User se player name aur new score lo.
# Agar player exist karta hai → score update karo.
# Agar nahi → player ko add karo.
# Phir sorted order me print karo (by name).
#
# scores = {
#     "Amit": 250,
#     "Rahul": 180,
#     "Shivaji": 310
# }

scores = {
    "Amit": 250,
    "Rahul": 180,
    "Shivaji": 310
}

# 👇 Apna solution yahan likho:
# player = input("Player Name: ")
# score = int(input("New Score: "))
# scores[player] = score
#
# for p_name in sorted(scores.keys()):
#     print(f"{p_name}: {scores[p_name]}")


# ============================================================
# ✅ Day 05 | 03 - Modifying Elements Complete
# ============================================================
