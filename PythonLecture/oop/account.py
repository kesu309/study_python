class Account:

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.count
        Account.count += 1

    def withdraw(self, price):             #　withdraw 引き出し
        if price <= self.balance:
            self.balance -= price
            self.show_balance()
        else:
            print(f"残高({self.balance}円) 足りません")

    def deposit(self, price):
        self.balance += price 
        self.show_balance()      

    def show_balance(self):
        print(f"{self.name}(口座番号:{self.account_number})の残高は{self.balance}円です")
    

myaccount = Account(name="my account", balance=1000)
print(myaccount.name)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(1500)