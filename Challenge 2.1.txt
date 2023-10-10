class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Holder: {self._account_holder_name}, Account Number: {self._account_number}, Balance: ${self._account_balance:.2f}"

if __name__ == "__main__":
    account_number = input("Enter your account number: ")
    account_holder_name = input("Enter your account holder name: ")
    initial_balance = float(input("Enter initial account balance: "))
    
    account = BankAccount(account_number, account_holder_name, initial_balance)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            if account.deposit(amount):
                print(f"Deposited ${amount:.2f} successfully.")
            else:
                print("Invalid deposit amount.")
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            if account.withdraw(amount):
                print(f"Withdrawn ${amount:.2f} successfully.")
            else:
                print("Invalid withdrawal amount.")
        elif choice == "3":
            print(account.display_balance())
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")