class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposite(self,amount):
        self.balance += amount
    def withdraw(self,amount):
       if self.balance < amount:
         print("Error: insufficient funds")
       else:
          self.balance -= amount
    def check_balance(self):
       print(f"balance is {self.balance}")

acc = BankAccount()
acc.check_balance()
acc.deposite(1000000)
acc.check_balance()
acc.withdraw(40000)
acc.check_balance()



