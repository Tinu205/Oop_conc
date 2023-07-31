class Bankaccount:
    def __init__(self,acc_num,customer,balance = 0):
        self.acc_num = acc_num
        self.balance = balance
        self.customer = customer
        self.transaction = []

    def deposit(self,amount):
        self.balance+=amount
        self.transaction.append(f"Deposited: {amount}")
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.transaction.append(f"Deposited: {amount}")
            return f"Balance in account: {self.balance}"
class Transaction(Bankaccount):
    def __init__(self,transaction):
        super.__init__(transaction)
    def get_trans(self):
        return self.transaction

    
    def get_trans(self):
        return Transaction

root = Bankaccount(123456,"Panda",1000)
root.deposit(500)
print(root.get_balance())

root.withdraw(1600)
print(root.withdraw(120))

print(root.get_trans)