class BankAccount : 
    def __init__(self, account_holder, balance = 0) : 
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit (self, amount) : 
        if amount > 0 : 
            self.balance += amount
            print(f"{amount} deposited successfully")
        else : 
            print("Invalid deposit amount")

    def withdraw (self, amount):
        if amount <= 0 :
            print("Invalid withdrawl amount")
        elif self.balance >= amount : 
            self.balance -= amount
            print(f"{amount} Withdrawn successfully")
        else : 
            print("Insufficient funds")

    def check_balance(self) : 
        print(f"Current balance : {self.balance}")
    
account1 = BankAccount("Pippa", 1000)
account1.check_balance()
account1.deposit(500)
account1.check_balance()
account1.withdraw(300)
account1.check_balance()
account1.withdraw(2000)
account1.check_balance()
