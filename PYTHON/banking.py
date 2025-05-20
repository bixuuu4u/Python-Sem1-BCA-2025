# Class-> bank
# Attributes -> Holder name and balance
# Methods -> Deposite Withdraw

class Bank:


    def __init__(self,holder_name,holder_balance=0.0):
        self.holder_name=holder_name
        self.holder_balance=holder_balance

    def deposite(self,amount):
        if amount>0:
            self.holder_balance +=amount
            print(f"{amount} deposited to your account. Current balance {self.holder_balance}")
        else:
            print("Deposite amount cant be negetive")

    def withdraw(self,amount):
        if 0< amount <= self.holder_balance:
            self.holder_balance -=amount
            print(f"{amount} withdrawn from your account. Current balance {self.holder_balance}")
        else:
            print("Insufficient funds")

    def display(self):
        print("Welcome to Bank")
        print(f"Account Holder:{self.holder_name}")
        print(f"Current balance:{self.holder_balance}")

account1= Bank("Biswajeet",1000)
account2= Bank("Bisu",9090)

account1.display()
account1.deposite(90)
account1.withdraw(50)
account1.withdraw(90909090)
account2.display()
account2.deposite(90)
account2.withdraw(50)
account2.withdraw(909)
