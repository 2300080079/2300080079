class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts.append(account)
        print(f"Account created for {account_holder} with account number {account_number}")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def view_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            account.display()
        else:
            print("Account not found")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found")

def main():
    bank = Bank()
    
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account_number = int(input("Enter account number: "))
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_holder, initial_balance)
        
        elif choice == '2':
            account_number = int(input("Enter account number to view: "))
            bank.view_account(account_number)
        
        elif choice == '3':
            account_number = int(input("Enter account number to deposit into: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)
        
        elif choice == '4':
            account_number = int(input("Enter account number to withdraw from: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
