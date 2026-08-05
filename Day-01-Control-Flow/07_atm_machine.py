# ATM Machine (Mini Project)

balance = 5000

print("===== ATM MENU =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    print(f"\nCurrent Balance: ₹{balance}")

elif choice == 2:
    deposit = int(input("Enter deposit amount: ₹"))

    if deposit <= 0:
        print("❌ Invalid Deposit Amount")
    else:
        balance += deposit
        print("✅ Deposit Successful")
        print(f"Current Balance: ₹{balance}")

elif choice == 3:
    withdraw = int(input("Enter withdraw amount: ₹"))

    if withdraw <= 0:
        print("❌ Invalid Withdraw Amount")

    elif withdraw > balance:
        print("❌ Insufficient Balance")

    else:
        balance -= withdraw
        print("✅ Withdraw Successful")
        print(f"Current Balance: ₹{balance}")

elif choice == 4:
    print("🙏 Thank You for Using Our ATM")

else:
    print("❌ Invalid Option")
