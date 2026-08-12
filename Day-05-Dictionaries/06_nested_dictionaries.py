# ============================================================
# Day-05 | 06 - Nested Dictionaries
# ============================================================

# Nested Dictionary = Dictionary ke andar Dictionary
#
# Example:
#   company = {
#       "emp1": {"name": "Amit", "salary": 50000},
#       "emp2": {"name": "Rahul", "salary": 60000}
#   }
#
# Access:
#   company["emp1"]["name"]  →  "Amit"
#
# Modify:
#   company["emp1"]["salary"] = 55000


# ============================================================
# Q1 ⭐ — Access Nested Value
# ============================================================

# Rahul ki age access karo.
#
# Expected: 22

students = {
    "student1": {"name": "Amit", "age": 21},
    "student2": {"name": "Rahul", "age": 22},
    "student3": {"name": "Shivaji", "age": 20}
}

# 👇 Apna solution yahan likho:
print(students["student2"]["age"])


# ============================================================
# Q2 ⭐ — Print Full Inner Dictionary
# ============================================================

# "laptop" product ki puri information print karo.
#
# Expected: {'brand': 'Dell', 'price': 65000, 'stock': 10}

inventory = {
    "laptop": {"brand": "Dell", "price": 65000, "stock": 10},
    "mouse":  {"brand": "Logitech", "price": 1200, "stock": 50},
    "monitor":{"brand": "LG", "price": 18000, "stock": 5}
}

# 👇 Apna solution yahan likho:
print(inventory["laptop"])


# ============================================================
# Q3 ⭐⭐ — Modify Nested Value
# ============================================================

# "mouse" ki price 1200 se 1500 karo.
# Phir updated inventory print karo.

# 👇 Apna solution yahan likho (same inventory dict):
inventory["mouse"]["price"] = 1500
print(inventory)


# ============================================================
# Q4 ⭐⭐ — Add New Nested Key
# ============================================================

# emp1 me "department" key add karo with value "Engineering".
# Phir emp1 print karo.

company = {
    "emp1": {"name": "Shivaji", "salary": 70000},
    "emp2": {"name": "Amit",    "salary": 55000}
}

# 👇 Apna solution yahan likho:
company["emp1"]["department"] = "Engineering"
print(company["emp1"])


# ============================================================
# Q5 ⭐⭐ — Add Completely New Nested Entry
# ============================================================

# school dict me ek naya student "student4" add karo:
#   name: "Rohit", age: 19, marks: 78
# Phir pura school dict print karo.

school = {
    "student1": {"name": "Amit",    "age": 21, "marks": 75},
    "student2": {"name": "Rahul",   "age": 20, "marks": 88},
    "student3": {"name": "Shivaji", "age": 19, "marks": 91}
}

# 👇 Apna solution yahan likho:
school["student4"] = {"name": "Rohit", "age": 19, "marks": 78}
print(school)


# ============================================================
# Q6 ⭐⭐⭐ — Loop Over Nested Dict
# ============================================================

# Loop use karke har employee ka naam aur salary print karo.
#
# Expected:
#   Shivaji → ₹70000
#   Amit    → ₹55000

# 👇 Apna solution yahan likho (same company dict):
for emp_id, details in company.items():
    print(f"{details['name']} → ₹{details['salary']}")


# ============================================================
# Q7 ⭐⭐⭐ — Find Highest Paid Employee
# ============================================================

# Loop use karke highest salary wale employee ka naam dhundo.
# ⚠️ max() use nahi karna.
#
# Expected: Shivaji (70000)

# 👇 Apna solution yahan likho (same company dict):
max_salary = 0
top_employee = ""
for details in company.values():
    if details["salary"] > max_salary:
        max_salary = details["salary"]
        top_employee = details["name"]
print(f"{top_employee} ({max_salary})")


# ============================================================
# Q8 ⭐⭐⭐ — Count Students Above Average
# ============================================================

# Step 1: Saare students ke marks ka average nikalo
# Step 2: Count karo ki kitne students average se upar hain
# Step 3: Print karo
#
# Expected:
#   Average: 84.67
#   Students above average: 2  (Rahul 88, Shivaji 91)

# 👇 Apna solution yahan likho (same school dict):
total_marks = 0
student_count = len(school)

for details in school.values():
    total_marks += details["marks"]
    
average = total_marks / student_count

above_avg_count = 0
for details in school.values():
    if details["marks"] > average:
        above_avg_count += 1
        
print(f"Average: {average:.2f}")
print(f"Students above average: {above_avg_count}")


# ============================================================
# Q9 ⭐⭐⭐ — 3-Level Nested Access
# ============================================================

# "Python" course ka second topic access karo.
#
# Expected: OOP

university = {
    "CS": {
        "courses": {
            "Python": {
                "topics": ["Basics", "OOP", "DSA"],
                "duration": "3 months"
            },
            "Java": {
                "topics": ["Basics", "Spring"],
                "duration": "2 months"
            }
        }
    }
}

# 👇 Apna solution yahan likho:
print(university["CS"]["courses"]["Python"]["topics"][1])


# ============================================================
# Q10 🧠 — Nested Dict Builder
# ============================================================

# User se 3 baar:
#   - Employee name
#   - Employee salary
# lo aur ek nested dictionary build karo.
#
# Format:
# {
#   "emp1": {"name": "...", "salary": ...},
#   "emp2": {"name": "...", "salary": ...},
#   "emp3": {"name": "...", "salary": ...}
# }
# Phir puri dictionary print karo.

# 👇 Apna solution yahan likho:
built_dict = {}
for i in range(1, 4):
    emp_name = input(f"Enter name for emp{i}: ")
    emp_salary = int(input(f"Enter salary for emp{i}: "))
    built_dict[f"emp{i}"] = {"name": emp_name, "salary": emp_salary}
print(built_dict)


# ============================================================
# ✅ Day 05 | 06 - Nested Dictionaries Complete
# ============================================================
