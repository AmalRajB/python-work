from abc import ABC, abstractmethod 
class user(ABC):
    def __init__(self,name,joined_year):
        self.name=name
        self.joined_year=joined_year 
    @abstractmethod
    def calculate_year(self):
        current_year=2025
        if(self.joined_year==current_year):
            return('joined in this year')     
        else:
            return(f'been part of {current_year-self.joined_year} years')

        
class customer(user):
    def __init__(self,name,joined_year):
        super().__init__(name,joined_year)
        self.role='customer'
        
        
    def calculate_year(self):
        super().calculate_year()
    
    def show(self):
        print(f'name: {self.name} role : {self.role} year : {super().calculate_year()}')       
    
class vendor(user):
    def __init__(self,name,joined_year):
        super().__init__(name,joined_year)
        self.role='vendor'
        
    def calculate_year(self):
        super().calculate_year()
    def show(self):
        print(f'name: {self.name} role : {self.role} year : {super().calculate_year()}')       

obj=customer("amal",2023) 
obj.show() 

obj2=vendor('athul',2025)
obj2.show()
    
    






        

    

    



    





    

    
