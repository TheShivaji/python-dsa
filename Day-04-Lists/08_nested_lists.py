# ============================================================
# Day-04 | 08 - Nested Lists
# ============================================================

# Syntax Reminder:
#
# Accessing an inner list:
# nested_list[row_index][column_index]
#
# Example:
# matrix[0][1]
#
# Outer Loop:
# for row in matrix:
#     ...
#
# Nested Loop:
# for row in matrix:
#     for element in row:
#         ...

# Nested List = List ke andar List
# Example:
#   students = [["Amit", 21], ["Rahul", 22]]
#   Access: students[0]      → ["Amit", 21]
#           students[0][0]   → "Amit"
#           students[0][1]   → 21


# ============================================================
# Q1 ⭐ — Basic Nested List
# ============================================================

# Puri nested list print karo.
#
# students = [
#     ["Amit", 21],
#     ["Rahul", 22],
#     ["Shivaji", 21]
# ]
# Expected: [['Amit', 21], ['Rahul', 22], ['Shivaji', 21]]

students = [
    ["Amit", 21],
    ["Rahul", 22],
    ["Shivaji", 21]
]

# 👇 Apna solution yahan likho:

stu = [stud for stud in students]
print(stu)

# ============================================================
# Q2 ⭐ — Access First Inner List
# ============================================================

# Same students list se sirf first student ki information print karo.
#
# Expected: ['Amit', 21]

# 👇 Apna solution yahan likho:
print(students[0])


# ============================================================
# Q3 ⭐⭐ — Access Nested Element
# ============================================================

# Same list se Shivaji ka naam access karo.
#
# Hint:
#   students → third student → name
#
# Expected: Shivaji

# 👇 Apna solution yahan likho:

print(students[2][0])


# ============================================================
# Q4 ⭐⭐ — Access Age
# ============================================================

# Rahul ki age access karo.
#
# students = [
#     ["Amit", 21],
#     ["Rahul", 22],
#     ["Shivaji", 21]
# ]
# Expected: 22

# 👇 Apna solution yahan likho:
print(students[1][1])


# ============================================================
# Q5 ⭐⭐ — Modify Nested Element
# ============================================================

# Same list me Rahul → Rohit change karo.
#
# Expected:
#   [["Amit", 21], ["Rohit", 22], ["Shivaji", 21]]

# 👇 Apna solution yahan likho:
students[1][0] = "Rohit"
print(students)

# ============================================================
# Q6 ⭐⭐ — Nested Numbers (Indexing)
# ============================================================

# Sirf indexing use karke 1, 5 aur 9 access karo.
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Expected: 1  5  9  (teen alag print statements)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 👇 Apna solution yahan likho:
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])



# ============================================================
# Q7 ⭐⭐⭐ — Print Each Row
# ============================================================

# for loop se each row print karo.
# ⚠️ Abhi nested loop nahi — sirf ek loop.
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Expected:
#   [1, 2, 3]
#   [4, 5, 6]
#   [7, 8, 9]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 👇 Apna solution yahan likho:
for row in matrix:
    print(row)

# ============================================================
# Q8 ⭐⭐⭐ — Print Every Element (Nested Loop)
# ============================================================

# Nested for loop use karke har individual number print karo.
#
# Hint:
#   outer loop → row
#   inner loop → element
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Expected:
#   1  2  3  4  5  6  7  8  9  (ek ek line pe)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 👇 Apna solution yahan likho:
for row in matrix:
    for elements in row:
        print(elements)


# ============================================================
# Q9 ⭐⭐⭐ — Sum of Matrix
# ============================================================

# Nested loops use karke all elements ka sum nikalo.
# ⚠️ sum() use nahi karna.
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Expected: 45

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 👇 Apna solution yahan likho:
sum = 0
for row in matrix:
    for elem in row:
        sum+=elem

print(sum)



# ============================================================
# Q10 🧠 — Find Largest in Nested List
# ============================================================

# Nested loops use karke largest number find karo.
# ⚠️ max() use nahi karna.
#
# matrix = [
#     [10, 25, 8],
#     [45, 12, 30],
#     [7,  50, 20]
# ]
# Expected: 50

matrix = [
    [10, 25, 8],
    [45, 12, 30],
    [7,  50, 20]
]


# 👇 Apna solution yahan likho:
large_val = 0

for row in matrix:
    for elem in row:
        if(elem > large_val):
            large_val=elem

print(large_val)


# ============================================================
# ✅ Day 04 | Nested Lists Complete
# ============================================================
