# Example of banking Simple Banking System Using objects and class

class BankAccount:
    def __init__(self, account_holder,account_number,balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your New balance is ${self.balance}.")
        else:
            print("Invalid Deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuffient Fund to Withdraw!")
        elif amount <= 0:
            print("Invalid Withdraw Amount. Please Enter Valid Amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount},. Your New Balance is ${self.balance}")
    
    def check_balance(self):
        print(f"Account Balance for {self.account_holder} is ${self.balance}.")


account = BankAccount("Anup Karki","12432637365", 1000)
account.deposit(50)
account.withdraw(500)
account.check_balance()

