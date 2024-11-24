bank_accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Delete Account")
    print("5. Display All Accounts")
    print("6. Exit")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        acc_num = int(input("Enter account number: "))
        if acc_num in bank_accounts:
            print("Account already exists!")
        else:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Balance cannot be negative!")
            else:
                bank_accounts[acc_num] = initial_balance
                print("Account created successfully!")
    
    elif ch == 2:
        acc_num = int(input("Enter account number: "))
        if acc_num in bank_accounts:
            deposit_amount = float(input("Enter the amount to deposit: "))
            if deposit_amount <= 0:
                print("Deposit amount must be greater than zero!")
            else:
                bank_accounts[acc_num] += deposit_amount
                print(f"Amount deposited successfully! Updated balance: {bank_accounts[acc_num]}")
        else:
            print("Invalid account number!")
    
    elif ch == 3:
        acc_num = int(input("Enter account number: "))
        if acc_num in bank_accounts:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= 0:
                print("Withdrawal amount must be greater than zero!")
            elif withdraw_amount > bank_accounts[acc_num]:
                print("Insufficient balance!")
            else:
                bank_accounts[acc_num] -= withdraw_amount
                print(f"Amount withdrawn successfully! Updated balance: {bank_accounts[acc_num]}")
        else:
            print("Invalid account number!")
    
    elif ch == 4:
        acc_num = int(input("Enter account number to delete: "))
        if acc_num in bank_accounts:
            del bank_accounts[acc_num]
            print("Account deleted successfully!")
        else:
            print("Invalid account number!")
    
    elif ch == 5:
        if bank_accounts:
            print("\nAll Accounts:")
            for acc, balance in bank_accounts.items():
                print(f"Account Number: {acc}, Balance: {balance}")
        else:
            print("No accounts available!")
