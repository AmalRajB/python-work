from abc import ABC,abstractmethod

class user(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year

    def account_age(self):
        current_year=2025
        if(self.account_year==current_year):
            return "account created on this year"
        else:
            return (f'{current_year-self.account_year} years old')
    @abstractmethod    
    def get_role(self):
        pass

class admin(user):
    
    def get_role(self):
        return 'admin' 

    def __str__(self):
        return (f'{self.name} is a {self.get_role()} , and the account age is {super().account_age()} ')  

class guest(user):
    
    def get_role(self):
        return 'guest' 

    def __str__(self):
        return (f'{self.name} is a {self.get_role()} , and the account age is {super().account_age()} ')  

    
obj1=admin('amal',2020)
print(obj1)

obj2=guest('athul',2025)
print(obj2)

    
        







      
