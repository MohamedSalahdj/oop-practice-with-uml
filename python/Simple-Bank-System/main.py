from bank import BankAccount


if __name__ == "__main__":
    while True:
        action = input("Choose an action\n 1-Create Account \n 2-Deposit \n 3-Withdraw \n 4-Show Balance \n 5-Exit\n")

        match action:
            case "1":
                owner = input("Enter account owner name: ")
                account = BankAccount(owner)
            
            case "2":
                account_number = input("Enter account number: ")
                if account := BankAccount.get_account(account_number=account_number):
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
            
            case "3":
                account_number = input("Enter account number: ")
                if account := BankAccount.get_account(account_number=account_number):
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)

            case "4":
                account_number = input("Enter account number: ")
                if account := BankAccount.get_account(account_number=account_number):
                    account.show_balance()

            case "5":
                print("Exiting...")
                break
