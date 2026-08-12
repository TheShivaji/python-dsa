# ============================================================
# Day-05 | 04 - Dictionary Methods
# ============================================================

# Important Dictionary Methods:
#
#   dict.keys()      → all keys
#   dict.values()    → all values
#   dict.items()     → all key-value pairs as tuples
#   dict.get(k, d)   → value or default
#   dict.update({})  → merge another dict
#   dict.pop(k)      → remove & return value
#   dict.popitem()   → remove & return last pair
#   dict.copy()      → shallow copy
#   dict.clear()     → remove all
#   dict.setdefault(k, v) → get or set default


# ============================================================
# Q1 ⭐ — keys() Method
# ============================================================

# Print karo saari keys of this dictionary.
#
# Expected: dict_keys(['name', 'age', 'city', 'marks'])

student = {"name": "Shivaji", "age": 21, "city": "Mumbai", "marks": 91}

# 👇 Apna solution yahan likho:
print(student.keys())

# ============================================================
# Q2 ⭐ — values() Method
# ============================================================

# Print karo saari values of this dictionary.
#
# Expected: dict_values(['Shivaji', 21, 'Mumbai', 91])

# 👇 Apna solution yahan likho (same student dict):
print(student.values())


# ============================================================
# Q3 ⭐ — items() Method
# ============================================================

# Print karo saare key-value pairs as tuples.
#
# Expected:
#   dict_items([('name', 'Shivaji'), ('age', 21), ...])

# 👇 Apna solution yahan likho (same student dict):
print(student.items())


# ============================================================
# Q4 ⭐⭐ — update() — Merge Two Dicts
# ============================================================

# base_info me extra_info ko merge karo using update().
# Phir final merged dictionary print karo.
#
# Expected:
#   {'name': 'Amit', 'age': 22, 'city': 'Delhi', 'email': 'amit@gmail.com'}

base_info = {"name": "Amit", "age": 22}
extra_info = {"city": "Delhi", "email": "amit@gmail.com"}

# 👇 Apna solution yahan likho:
base_info.update(extra_info)
print(base_info)


# ============================================================
# Q5 ⭐⭐ — pop() with Default
# ============================================================

# "discount" key ko pop karo.
# Agar key nahi hai to default return ho: 0
# Result print karo.
#
# Run 1: discount key hai   → 10
# Run 2: agar delete kar do → 0

product = {"name": "Mouse", "price": 1000, "discount": 10}

# 👇 Apna solution yahan likho:
print(product.pop("discount", 0))


# ============================================================
# Q6 ⭐⭐ — popitem() Method
# ============================================================

# popitem() use karke last key-value pair remove karo.
# Remove hua pair print karo.
# Phir updated dictionary print karo.

info = {"brand": "Nike", "type": "Shoes", "price": 5000}

# 👇 Apna solution yahan likho:
removed_item = info.popitem()
print("Removed:", removed_item)
print(info)


# ============================================================
# Q7 ⭐⭐ — setdefault() Method
# ============================================================

# setdefault() use karo:
#   → "score" key nahi hai → default 0 set karo
#   → "name" key already hai → existing value rakho
# Dono results print karo.
#
# Expected:
#   score → 0
#   name  → Rahul

profile = {"name": "Rahul", "age": 20}

# 👇 Apna solution yahan likho:
print("score →", profile.setdefault("score", 0))
print("name →", profile.setdefault("name", "Unknown"))


# ============================================================
# Q8 ⭐⭐⭐ — copy() — Shallow Copy
# ============================================================

# original ka ek copy banao using copy().
# Copy me "price" change karo.
# Phir dono print karo aur dekho:
#   → original change hua ya nahi?
#
# Expected:
#   original: {"item": "Laptop", "price": 60000}
#   copied:   {"item": "Laptop", "price": 75000}

original = {"item": "Laptop", "price": 60000}

# 👇 Apna solution yahan likho:
copied = original.copy()
copied["price"] = 75000
print("original:", original)
print("copied:  ", copied)


# ============================================================
# Q9 ⭐⭐⭐ — Check Value Existence
# ============================================================

# Kisi specific value ka existence check karna.
# values() method use karke check karo:
#   → "Python" subjects dict me hai ya nahi?
#
# Expected: True

courses = {
    "Web Dev": "JavaScript",
    "Data Science": "Python",
    "Mobile": "Flutter"
}

# 👇 Apna solution yahan likho:
print("Python" in courses.values())


# ============================================================
# Q10 🧠 — Method Chaining Challenge
# ============================================================

# config dict pe ye kaam karo (order matter karta hai):
#   Step 1: "debug" key ka value get karo (default: False)
#   Step 2: "version" key set karo with setdefault (default: "1.0")
#   Step 3: new_settings se update karo
#   Step 4: "temp" key pop karo
#   Step 5: Final dictionary print karo
#
# Expected final:
#   {'host': 'localhost', 'port': 9000, 'version': '1.0', 'ssl': True}

config = {
    "host": "localhost",
    "port": 8080,
    "temp": "remove_me"
}

new_settings = {"port": 9000, "ssl": True}

# 👇 Apna solution yahan likho:
debug_val = config.get("debug", False)
config.setdefault("version", "1.0")
config.update(new_settings)
config.pop("temp", None)

print(config)


# ============================================================
# ✅ Day 05 | 04 - Dictionary Methods Complete
# ============================================================
