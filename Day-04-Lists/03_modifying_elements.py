# ============================================================
#          Day-04 | 03 - Modifying Elements
# ============================================================


# Q1 ⭐ — Simple Modification
# languages = ["Python", "JavaScript", "Java", "C++"]
# JavaScript ko TypeScript se replace karo.
# Expected: ["Python", "TypeScript", "Java", "C++"]

languages = ["Python", "JavaScript", "Java", "C++"]

languages[1] = "TypeScript"

print(languages)
 


# -------------------------------------------------------

# Q2 ⭐ — Modify First Element
# colors = ["Red", "Green", "Blue"]
# Red ko Black karo.
# Expected: ["Black", "Green", "Blue"]

colors = ["Red", "Green", "Blue"]

colors[0] = "Black"

print(colors)



# -------------------------------------------------------

# Q3 ⭐⭐ — Modify Last Element
# numbers = [10, 20, 30, 40, 50]
# Last element ko 100 karo.
# Hint: Negative indexing ka use kar sakta hai.
# Expected: [10, 20, 30, 40, 100]

numbers = [10, 20, 30, 40, 50]

numbers[-1] = 100

print(numbers)



# -------------------------------------------------------

# Q4 ⭐⭐ — Multiple Elements
# languages = ["Python", "JavaScript", "Java", "C++", "Go"]
# Change: JavaScript → TypeScript, Java → Rust
# Expected: ["Python", "TypeScript", "Rust", "C++", "Go"]

languages = ["Python", "JavaScript", "Java", "C++", "Go"]

languages[1] = "TypeScript"
languages[2] = "Rust"

print(languages)



# -------------------------------------------------------

# Q5 ⭐⭐ — Modify Using User Input
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# User se index aur new value lo:
#   Enter index: 1
#   Enter new fruit: Grapes
# Expected: ["Apple", "Grapes", "Mango", "Orange"]

fruits = ["Apple", "Banana", "Mango", "Orange"]

user_input = int(input("Enter index : "))
new_fruit = input("Enter the new fruit")

fruits[user_input] = new_fruit

print(fruits)


# -------------------------------------------------------

# Q6 ⭐⭐⭐ — Marks Update
# marks = [65, 72, 81, 55, 90]
# First student → 75
# Last student  → 95
# Expected: [75, 72, 81, 55, 95]

marks = [65, 72, 81, 55, 90]

marks[0] = 75
marks[-1] = 95

print(marks)


# -------------------------------------------------------

# Q7 ⭐⭐⭐ — Replace Multiple Values
# numbers = [1, 2, 3, 4, 5]
# 2, 3, 4 ko replace karke [1, 20, 30, 40, 5] banao.
# Hint: Individual indexes se try kar.

numbers = [1, 2, 3, 4, 5]

numbers[1] = 20
numbers[2] = 30
numbers[3] = 40

print(numbers)



# -------------------------------------------------------

# Q8 🧠 — Challenge
# students = ["Amit", "Rahul", "Shivaji", "Rohit", "Akash"]
# "Shivaji" ko "Developer" se replace karo.
# Expected: ["Amit", "Rahul", "Developer", "Rohit", "Akash"]

students = ["Amit", "Rahul", "Shivaji", "Rohit", "Akash"]

students[2] = "Developer"
print(students)




