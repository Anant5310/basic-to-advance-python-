class bank:
    def __init__(self, bal, no):
        self.account_bal = bal
        self.account_no = no
        
    def credit(self,amount):
        self.account_bal+= amount
        print(amount,'is creatted on acc')
        
    def debit(self,amount):
        self.account_bal -= amount
        print(amount,"is debitted on your account")

b1 = bank(20000,12345)
b1.debit(5000)
b1.credit(700)
print('on your account',b1.account_no,'balance is :',b1.account_bal)