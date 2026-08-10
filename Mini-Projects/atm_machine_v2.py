# ATM Machine (Mini Project - V2)

balance = 5000
transactions = 0
invalid_attempts = 0

border = "=" * 40


def get_integer(prompt):
    """Prompt the user for an integer and return None for invalid input."""
    try:
        return int(input(prompt))
    except ValueError:
        return None


def print_header():
    print("\n" + border)
    print("        🏦 PYTHON ATM SYSTEM")
    print(border)
    print("1. 💰 Check Balance")
    print("2. ➕ Deposit")
    print("3. ➖ Withdraw")
    print("4. 🚪 Exit")
    print(border)


def print_summary():
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
    print_header()
    choice = get_integer("Enter your choice: ")

    if choice is None:
        invalid_attempts += 1
        print("\n" + border)
        print("❌ Invalid Input. Please enter a number.")
        print(f"⚠️ Invalid Attempts : {invalid_attempts}")
        print(border)
        continue

    if choice == 1:
        print("\n" + border)
        print(f"💰 Current Balance : ₹{balance}")
        print(border)

    elif choice == 2:
        deposit = get_integer("Enter Deposit Amount: ₹")

        if deposit is None or deposit <= 0:
            invalid_attempts += 1
            print("\n" + border)
            print("❌ Invalid Deposit Amount")
            print(f"⚠️ Invalid Attempts : {invalid_attempts}")
            print(border)
        else:
            balance += deposit
            transactions += 1
            print("\n" + border)
            print("✅ Deposit Successful")
            print(f"💰 Current Balance : ₹{balance}")
            print(f"🔄 Transactions    : {transactions}")
            print(border)

    elif choice == 3:
        withdraw = get_integer("Enter Withdraw Amount: ₹")

        if withdraw is None or withdraw <= 0:
            invalid_attempts += 1
            print("\n" + border)
            print("❌ Invalid Withdraw Amount")
            print(f"⚠️ Invalid Attempts : {invalid_attempts}")
            print(border)

        elif withdraw > balance:
            invalid_attempts += 1
            print("\n" + border)
            print("❌ Insufficient Balance")
            print(f"⚠️ Invalid Attempts : {invalid_attempts}")
            print(border)

        else:
            balance -= withdraw
            transactions += 1
            print("\n" + border)
            print("✅ Withdraw Successful")
            print(f"💰 Current Balance : ₹{balance}")
            print(f"🔄 Transactions    : {transactions}")
            print(border)

    elif choice == 4:
        print_summary()
        break

    else:
        invalid_attempts += 1
        print("\n" + border)
        print("❌ Invalid Option")
        print(f"⚠️ Invalid Attempts : {invalid_attempts}")
        print(border)
