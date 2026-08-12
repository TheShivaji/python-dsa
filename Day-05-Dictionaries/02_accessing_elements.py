# ============================================================
# Day-05 | 02 - Accessing Elements
# ============================================================

# Dictionary me values access karne ke 2 tarike:
#
#   1. Square bracket:  dict["key"]   → KeyError agar key nahi
#   2. get() method:    dict.get("key") → None agar key nahi
#
# Example:
#   person = {"name": "Shivaji", "age": 21}
#   person["name"]          →  "Shivaji"
#   person.get("email")     →  None


# ============================================================
# Q1 ⭐ — Access by Key
# ============================================================

# product dictionary se "brand" aur "price" access karo
# aur print karo.
#
# Expected:
#   Samsung
#   45000

product = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 45000,
    "color": "Black"
}

# 👇 Apna solution yahan likho:
print(product["brand"])
print(product["price"])

# ============================================================
# Q2 ⭐ — Access Using Variable
# ============================================================

# Ek variable me key ka naam store karo
# aur us variable se dictionary value access karo.
#
# key = "city"
# Expected: Pune

profile = {"name": "Amit", "age": 25, "city": "Pune"}

key = "city"

# 👇 Apna solution yahan likho:
print(profile[key])


# ============================================================
# Q3 ⭐ — get() Method — Key Exists
# ============================================================

# get() method use karke "marks" ki value access karo.
#
# Expected: 88

student = {"name": "Rahul", "age": 20, "marks": 88}

# 👇 Apna solution yahan likho:
print(student.get("marks"))


# ============================================================
# Q4 ⭐⭐ — get() with Default Value
# ============================================================

# get() method use karo.
# Agar "email" key exist nahi karta to
# default value return ho: "Not Provided"
#
# Expected: Not Provided

user = {"name": "Shivaji", "age": 21, "city": "Mumbai"}

# 👇 Apna solution yahan likho:
print(user.get("email", "Not Provided"))


# ============================================================
# Q5 ⭐⭐ — KeyError Experiment
# ============================================================

# Neeche code run karo aur KeyError dekho.
# Phir comment me explain karo:
#   - Error kya hai?
#   - Kab aata hai?
#   - Kaise avoid karein?
#
# car = {"brand": "Tesla", "model": "Model 3"}
# print(car["color"])

car = {"brand": "Tesla", "model": "Model 3"}
# print(car["color"])   ← uncomment karke run karo (commented for clean run)

# 👇 Comment me likho:
# Error: KeyError: 'color'
# When it occurs: Jab hum square bracket se aisi key access karne ki koshish karte hain jo dictionary me exist nahi karti.
# How to avoid: get() method use karke (jaise car.get("color")), ya in keyword se check karke (if "color" in car).


# ============================================================
# Q6 ⭐⭐ — Access Nested Value
# ============================================================

# "phone" key ke andar "android" ki value access karo.
#
# Expected: Samsung

devices = {
    "laptop": "Dell",
    "phone": {
        "android": "Samsung",
        "ios": "iPhone"
    }
}

# 👇 Apna solution yahan likho:
print(devices["phone"]["android"])


# ============================================================
# Q7 ⭐⭐ — Access List Inside Dictionary
# ============================================================

# student ke "subjects" list ka last subject access karo.
#
# Expected: DSA

student = {
    "name": "Shivaji",
    "subjects": ["Python", "Math", "DSA"]
}

# 👇 Apna solution yahan likho:
print(student["subjects"][-1])


# ============================================================
# Q8 ⭐⭐⭐ — Safe Access with get()
# ============================================================

# User se ek key input lo.
# get() se us key ki value print karo.
# Agar key exist nahi karta: "Key not found"
#
# inventory = {
#     "laptop": 10,
#     "mouse": 25,
#     "keyboard": 15
# }
#
# Example:
#   Enter key: mouse   →  25
#   Enter key: tablet  →  Key not found

inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

# 👇 Apna solution yahan likho:
# user_key = input("Enter key: ")
# print(inventory.get(user_key, "Key not found"))


# ============================================================
# Q9 ⭐⭐⭐ — in Operator for Access
# ============================================================

# User se key input lo.
# Agar key exist karta hai → value print karo
# Agar nahi → "Key does not exist"
#
# config = {
#     "host": "localhost",
#     "port": 8080,
#     "debug": True
# }

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

# 👇 Apna solution yahan likho:
# config_key = input("Enter key: ")
# if config_key in config:
#     print(config[config_key])
# else:
#     print("Key does not exist")


# ============================================================
# Q10 🧠 — Multi-level Nested Access
# ============================================================

# company dictionary se "Python" developer ki salary access karo.
#
# Expected: 90000

company = {
    "name": "TechCorp",
    "departments": {
        "engineering": {
            "Python": {"count": 5, "salary": 90000},
            "Java":   {"count": 3, "salary": 85000}
        },
        "design": {
            "UI": {"count": 2, "salary": 70000}
        }
    }
}

# 👇 Apna solution yahan likho:
print(company["departments"]["engineering"]["Python"]["salary"])


# ============================================================
# ✅ Day 05 | 02 - Accessing Elements Complete
# ============================================================
