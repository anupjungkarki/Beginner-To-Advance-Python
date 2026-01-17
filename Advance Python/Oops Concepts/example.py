class Bank:
    def __init__(self,name, address):
        self._name = name
        self.address = address


    def get_name(self):
        return f"The name is : {self._name}"


class Account(Bank):
    def __init__(self, name , address , account_no, balance):
        super().__init__(name,address)
        self._account_no = account_no
        self.__balance = balance

    def get_account_no(self):
        return self.__account_no
    
    def get_details(self):
        return f"{self._name} and {self._account_no}"
    
class Loan(Account):
    def __init__(self, name , address , account_no, balance,loan_amount):
        super().__init__(name,address,account_no, balance)
        self._loan_amount = loan_amount

    def get_loan_amount(self):
        return self._loan_amount
    
    def get_details(self):
        return f"{self._name} and {self._account_no}"
    

n = Bank("Anup", "Solukhumbu")
print(n.get_name())

a = Account("Anup","Solu",123, 50000)
print(a.get_details())

l = Loan("Anup","Solu",133, 50000, 677)
print(l.get_details())