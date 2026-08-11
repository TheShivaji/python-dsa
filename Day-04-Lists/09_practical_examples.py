# ============================================================
# Day-04 | 09 - Practical Examples
# ============================================================

# Concepts Used:
# - List methods: append(), remove()
# - Nested lists: access, modify, search
# - Loops: for loop with conditions
# - User input: input()
# ============================================================


# ============================================================
# Q1 ⭐⭐ — To-Do Task
# ============================================================

# User se ek task lo aur list me add karo.

tasks = ["Study Python", "Practice DSA", "Build Project"]

user_input = input("Enter task: ")
tasks.append(user_input)

print("Updated Tasks:", tasks)


# ============================================================
# Q2 ⭐⭐⭐ — Product Price Update
# ============================================================

# User se product name aur new price lo.
# Agar product mila to uska price update karo.

products = [
    ["Laptop", 60000],
    ["Mouse", 1000],
    ["Keyboard", 2000]
]

product_name = input("Enter product name: ")
product_price = int(input("Enter new product price: ₹"))

product_found = False

for product in products:
    if product[0].lower() == product_name.lower():
        product[1] = product_price
        product_found = True
        break

if product_found:
    print("Price Updated Successfully")
    print(products)
else:
    print("Product Not Found")


# ============================================================
# Q3 ⭐⭐⭐ — Contact Search
# ============================================================

# User se naam lo aur uska phone number display karo.
# Agar naam nahi mila → "Contact Not Found"

contacts = [
    ["Amit", "9876543210"],
    ["Rahul", "9123456780"],
    ["Shivaji", "9988776655"]
]

search_name = input("Enter name: ")

contact_found = False

for contact in contacts:
    if contact[0].lower() == search_name.lower():
        print(f"Phone: {contact[1]}")
        contact_found = True
        break

if not contact_found:
    print("Contact Not Found")


# ============================================================
# Q4 ⭐⭐⭐ — Inventory Update
# ============================================================

# User se product name aur quantity sold lo.
# Inventory me se quantity ghata do.
# Agar available stock se zyada ho → "Insufficient Stock"

inventory = [
    ["Laptop", 5],
    ["Mouse", 10],
    ["Keyboard", 3]
]

product_name = input("Enter product name: ")
quantity_sold = int(input("Enter quantity sold: "))

product_found = False

for product in inventory:
    if product[0].lower() == product_name.lower():

        product_found = True

        if quantity_sold <= 0:
            print("Invalid Quantity")

        elif quantity_sold > product[1]:
            print("Insufficient Stock")

        else:
            product[1] -= quantity_sold
            print("Inventory Updated Successfully")
            print(inventory)

        break

if not product_found:
    print("Product Not Found")


# ============================================================
# Q5 🧠 — Mini Student Management
# ============================================================

students = [
    ["Amit", 75],
    ["Rahul", 82],
    ["Shivaji", 91]
]

while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Show Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # --------------------------------------------------------
    # 1. Show Students
    # --------------------------------------------------------

    if choice == "1":

        print("\n----- Students -----")

        for student in students:
            print(f"Name: {student[0]} | Marks: {student[1]}")

    # --------------------------------------------------------
    # 2. Add Student
    # --------------------------------------------------------

    elif choice == "2":

        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students.append([name, marks])

        print("Student Added Successfully")
        print(students)

    # --------------------------------------------------------
    # 3. Search Student
    # --------------------------------------------------------

    elif choice == "3":

        search_name = input("Enter student name: ")

        student_found = False

        for student in students:

            if student[0].lower() == search_name.lower():
                print(f"Name: {student[0]}")
                print(f"Marks: {student[1]}")

                student_found = True
                break

        if not student_found:
            print("Student Not Found")

    # --------------------------------------------------------
    # 4. Update Marks
    # --------------------------------------------------------

    elif choice == "4":

        search_name = input("Enter student name: ")
        new_marks = int(input("Enter new marks: "))

        student_found = False

        for student in students:

            if student[0].lower() == search_name.lower():

                student[1] = new_marks
                student_found = True

                print("Marks Updated Successfully")
                break

        if not student_found:
            print("Student Not Found")

    # --------------------------------------------------------
    # 5. Exit
    # --------------------------------------------------------

    elif choice == "5":

        print("Student Management Closed")
        break

    else:

        print("Invalid Option")


# ============================================================
# ✅ Day-04 | Practical Examples Complete
# ============================================================