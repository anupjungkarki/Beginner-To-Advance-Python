# Example of banking Simple Banking System Using objects and class

class BankAccount:
    # Constructor to initialize a new bank account
    def __init__(self, account_holder,account_number,balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your New balance is ${self.balance}.")
        else:
            print("Invalid Deposit amount. Please enter a positive number.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuffient Fund to Withdraw!")
        elif amount <= 0:
            print("Invalid Withdraw Amount. Please Enter Valid Amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount},. Your New Balance is ${self.balance}")

    # Method to check balance
    def check_balance(self):
        print(f"Account Balance for {self.account_holder} is ${self.balance}.")


# Creating an instance of BankAccount
account = BankAccount("Anup Karki","12432637365", 1000)


# Using Method for Deposit, Withdraw and Check Balance 
account.deposit(50)
account.withdraw(500)
account.check_balance()



