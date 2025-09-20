class account:
    def __init__(self,name:str,balance:float):
        self._name:str=name
        self._balance:float=balance
      
    def __add__(self,other):
        return self._balance+other._balance 

class savings_account(account):
    def __init__(self,name:str,balance:float):
        super().__init__(name,balance)

    def calculate_interest(self):
        return self._balance * 0.05 

class current_account(account):
    def __init__(self,name:str,balance:float):
        super().__init__(name,balance)

    def calculate_interest(self):
        return self._balance * 0.02
    
obj1= savings_account('ravi',10000)
print('SavingsAccount:')
print(f'name:{obj1._name}\n balance:{obj1._balance}\n interest:{obj1.calculate_interest()}\n')

obj2 = current_account('anjali',15000)
print('CurrentAccount:')
print(f'name:{obj2._name}\n balance:{obj2._balance}\n interest:{obj2.calculate_interest()}\n')
    
print("total balance : ",obj1+obj2)              


        

    

    

