# ATM Machine (Mini Project - V3)
# Concepts: Functions, Parameters, Return, if-elif-else, while loop

balance = 5000
transactions = 0
invalid_attempts = 0

border = "=" * 40


def show_menu():
    print("\n" + border)
    print("        🏦 PYTHON ATM SYSTEM")
    print(border)
    print("1. 💰 Check Balance")
    print("2. ➕ Deposit")
    print("3. ➖ Withdraw")
    print("4. 🚪 Exit")
    print(border)


def check_balance():
    print("\n" + border)
    print(f"💰 Current Balance : ₹{balance}")
    print(border)


def deposit():
    global balance, transactions

    amount = int(input("Enter Deposit Amount: ₹"))

    if amount <= 0:
        print("\n" + border)
        print("❌ Invalid Deposit Amount")
        print(border)
    else:
        balance += amount
        transactions += 1

        print("\n" + border)
        print("✅ Deposit Successful")
        print(f"💰 Current Balance : ₹{balance}")
        print(f"🔄 Transactions    : {transactions}")
        print(border)


def withdraw():
    global balance, transactions

    amount = int(input("Enter Withdraw Amount: ₹"))

    if amount <= 0:
        print("\n" + border)
        print("❌ Invalid Withdraw Amount")
        print(border)

    elif amount > balance:
        print("\n" + border)
        print("❌ Insufficient Balance")
        print(border)

    else:
        balance -= amount
        transactions += 1

        print("\n" + border)
        print("✅ Withdraw Successful")
        print(f"💰 Current Balance : ₹{balance}")
        print(f"🔄 Transactions    : {transactions}")
        print(border)


def show_summary():
    print("\n" + border)
    print("         🙏 THANK YOU")
    print("      FOR USING OUR ATM")
    print(border)

    print("📊 TRANSACTION SUMMARY")
    print("-" * 40)
    print(f"💰 Final Balance     : ₹{balance}")
    print(f"🔄 Transactions      : {transactions}")
    print(f"⚠️ Invalid Attempts  : {invalid_attempts}")
    print("-" * 40)
    print("❤️ Visit Again!")
    print("✅ Program Closed Successfully")
    print(border)


while True:

    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        show_summary()
        break

    else:
        invalid_attempts += 1

        print("\n" + border)
        print("❌ Invalid Option")
        print(f"⚠️ Invalid Attempts : {invalid_attempts}")
        print(border)
