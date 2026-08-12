# ============================================================
# Day-05 | 01 - Dictionary Basics
# ============================================================

# Dictionary kya hai?
#   - Key-Value pairs ki collection
#   - Keys unique hote hain
#   - Curly braces {} use hoti hain
#
# Syntax:
#   person = {"name": "Shivaji", "age": 21}
#   person["name"]  →  "Shivaji"


# ============================================================
# Q1 ⭐ — Create a Dictionary
# ============================================================

# Apna ek dictionary banao jisme ye keys hon:
#   name, age, city
#
# Example:
#   {"name": "Shivaji", "age": 21, "city": "Mumbai"}
#
# Phir puri dictionary print karo.

# 👇 Apna solution yahan likho:
my_dict = {"name": "Shivaji", "age": 21, "city": "Mumbai"}
print(my_dict)

# ============================================================
# Q2 ⭐ — Check the Type
# ============================================================

# Neeche diya gaya variable kiska type hai?
# type() function use karke check karo aur print karo.
#
# data = {"brand": "Nike", "price": 3000}

data = {"brand": "Nike", "price": 3000}

# 👇 Apna solution yahan likho:
print(type(data))

# ============================================================
# Q3 ⭐ — Length of Dictionary
# ============================================================

# Is dictionary me kitne key-value pairs hain?
# len() use karke print karo.
#
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "marks": 85,
#     "city": "Delhi"
# }

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85,
    "city": "Delhi"
}

# 👇 Apna solution yahan likho:
print(len(student))

# ============================================================
# Q4 ⭐ — Mixed Value Types
# ============================================================

# Ek dictionary banao jisme:
#   - ek string value ho
#   - ek integer value ho
#   - ek boolean value ho
#   - ek list value ho
#
# Phir dictionary print karo.

# 👇 Apna solution yahan likho:
mixed_dict = {
    "name": "Shivaji",
    "age": 21,
    "is_student": True,
    "skills": ["Python", "DSA"]
}
print(mixed_dict)

# ============================================================
# Q5 ⭐⭐ — Empty Dictionary
# ============================================================

# Ek empty dictionary banao.
# Phir uski length print karo.
# Phir ek key "language" add karo with value "Python".
# Phir dubara print karo.

# 👇 Apna solution yahan likho:
empty_dict = {}
print("Length before:", len(empty_dict))

empty_dict["language"] = "Python"
print("After adding:", empty_dict)

# ============================================================
# Q6 ⭐⭐ — Key Exists Check
# ============================================================

# in keyword use karke check karo:
#   → "email" key hai ya nahi?
#
# user = {"name": "Amit", "age": 25, "city": "Pune"}
#
# Expected:
#   False  (kyunki email key nahi hai)

user = {"name": "Amit", "age": 25, "city": "Pune"}

# 👇 Apna solution yahan likho:
print("email" in user)

# ============================================================
# Q7 ⭐⭐ — Dictionary vs List Difference
# ============================================================

# Neeche ek list aur ek dictionary dono hain.
# Comment me likho:
#   1. Dono me kya fark hai?
#   2. Kab list use karenge, kab dictionary?

my_list = ["Shivaji", 21, "Mumbai"]
my_dict = {"name": "Shivaji", "age": 21, "city": "Mumbai"}

# 👇 Answer comment me likho:
# Difference: List index (0, 1, 2) se access hoti hai, Dictionary keys ("name", "age") se access hoti hai. List ordered hoti hai, Dictionary key-value pairs hold karti hai.
# Use List when: Order important ho ya sirf values store karni hon.
# Use Dict when: Data ko kisi specific label/key (jaise 'name', 'price') se associate karke store karna ho.


# ============================================================
# Q8 ⭐⭐ — Duplicate Keys
# ============================================================

# Neeche dictionary me same key "name" do baar hai.
# Print karo aur dekho — kya hoga?
# Phir comment me likho: Python ne kya rakha aur kyun?
#
# person = {
#     "name": "Amit",
#     "name": "Rahul",
#     "age": 22
# }

person = {
    "name": "Amit",
    "name": "Rahul",
    "age": 22
}

print(person)

# 👇 Comment me likho:
# Result: {'name': 'Rahul', 'age': 22}
# Reason: Dictionary me keys unique honi chahiye. Agar same key dobara aati hai toh purani value overwrite ho jati hai nayi value se.


# ============================================================
# Q9 ⭐⭐⭐ — Nested Value (Simple)
# ============================================================

# Ek dictionary banao jisme ek key ki value
# khud ek list ho.
#
# Example:
#   student = {
#       "name": "Shivaji",
#       "subjects": ["Math", "Python", "DSA"]
#   }
#
# Phir "subjects" list ka second element print karo.

# 👇 Apna solution yahan likho:
student_nested = {
    "name": "Shivaji",
    "subjects": ["Math", "Python", "DSA"]
}
print(student_nested["subjects"][1])

# ============================================================
# Q10 🧠 — Build from Variables
# ============================================================

# Neeche variables diye hain.
# In variables ko use karke ek dictionary banao.
# Manually keys mat type karna — variable names ko keys banaao.
#
# name = "Shivaji"
# age = 21
# language = "Python"
#
# Expected dictionary:
#   {"name": "Shivaji", "age": 21, "language": "Python"}
#
# Hint: dict() constructor try karo

name = "Shivaji"
age = 21
language = "Python"

# 👇 Apna solution yahan likho:
my_dict_vars = dict(name=name, age=age, language=language)
print(my_dict_vars)

# ============================================================
# ✅ Day 05 | 01 - Dictionary Basics Complete
# ============================================================
