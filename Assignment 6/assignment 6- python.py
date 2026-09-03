print("============================")
print("WELCOME DEAR CUSTOMERE")
print("============================")
print("1. check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

balance = 100000
choice = input("Enter your choice (1-4): ")
if choice == "1":
    print("Your balance is:", balance)
elif choice == "2":
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful. New balance is:", balance)
elif choice == "3":
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. New balance is:", balance)
    else:
        print("Insufficient funds.")
elif choice == "4":
    print("Thank you for using our services.")
else:
    print("Invalid choice. please select a valid option (1-4).")