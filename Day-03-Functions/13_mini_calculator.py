
def add(a, b):
    """This function performs addition"""
    return a + b

def subtract(a, b):
    """This function performs subtraction"""
    return a - b

def multiply(a, b):
    """This function performs multiplication"""
    return a * b

def divide(a, b):
    """This function performs division"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

user_input = input("Enter expression (e.g., 10+5, 20-4, 5*3, 8/2): ")


user_input = user_input.replace(" ", "")

if '+' in user_input:
    a, b = user_input.split("+")
    print("Result:", add(float(a), float(b)))

elif '-' in user_input:
    a, b = user_input.split("-")
    print("Result:", subtract(float(a), float(b)))

elif '*' in user_input:
    a, b = user_input.split("*")
    print("Result:", multiply(float(a), float(b)))

elif '/' in user_input:
    a, b = user_input.split("/")
    print("Result:", divide(float(a), float(b)))

else:
    print("Invalid operator! Please use +, -, * or /")
