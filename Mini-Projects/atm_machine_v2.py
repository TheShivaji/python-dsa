# ATM Machine (Mini Project - V2)

balance = 5000
transactions = 0
invalid_attempts = 0

border = "=" * 40

while True:

    print("\n" + border)
    print("        🏦 PYTHON ATM SYSTEM")
    print(border)
    print("1. 💰 Check Balance")
    print("2. ➕ Deposit")
    print("3. ➖ Withdraw")
    print("4. 🚪 Exit")
    print(border)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n" + border)
        print(f"💰 Current Balance : ₹{balance}")
        print(border)

    elif choice == 2:
        deposit = int(input("Enter Deposit Amount: ₹"))

        if deposit <= 0:
            print("\n" + border)
            print("❌ Invalid Deposit Amount")
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
        withdraw = int(input("Enter Withdraw Amount: ₹"))

        if withdraw <= 0:
            print("\n" + border)
            print("❌ Invalid Withdraw Amount")
            print(border)

        elif withdraw > balance:
            print("\n" + border)
            print("❌ Insufficient Balance")
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

        break

    else:
        invalid_attempts += 1

        print("\n" + border)
        print("❌ Invalid Option")
        print(f"⚠️ Invalid Attempts : {invalid_attempts}")
        print(border)
