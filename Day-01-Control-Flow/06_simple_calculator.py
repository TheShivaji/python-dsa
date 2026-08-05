# Simple Calculator

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /, %): ")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot Divide by Zero")

elif operator == "%":
    if num2 != 0:
        print(num1 % num2)
    else:
        print("Cannot Modulo by Zero")

else:
    print("Invalid Operator")
