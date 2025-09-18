class employee:
    def __init__(self,name:str,role:str):
        self.name:str=name
        self.role:str=role


    def show_details(self):
        print(f'employee name : {self.name} role : {self.role}') 

class trainer(employee):
    def __init__(self,name:str,role:str,specialization:str,**kwargs):
        super(). __init__(name,role,**kwargs)
        self.specialization:str=specialization 

    def display(self):
        print(f'trainer name : {self.name} role : {self.role} specialization : {self.specialization}')  
class yogainstructor(employee):
    def __init__(self,name:str,role:str,yoga_style:str,**kwargs):
        super(). __init__(name,role,**kwargs)
        self.yoga_style:str=yoga_style 

    def display1(self):
        print(f'yoga instructor name : {self.name} role : {self.role} yoga_style : {self.yoga_style}') 

class multitrainer(trainer,yogainstructor):
    def __init__(self,name:str,role:str,specialization:str,yoga_style:str):
        super().__init__(name,role,specialization=specialization,yoga_style=yoga_style)

    def display2(self):
        print(f'multi trainer name : {self.name} role : {self.role} specialization : {self.specialization} yoga_style : {self.yoga_style} ')

obj1=employee('amal','accountant')
obj1.show_details()

obj2=trainer('athul','fitness trainer','weight training')
obj2.display()

obj3=yogainstructor('alice','yoga instructor','hatha yoga')
obj3.display1()

obj4=multitrainer('anusree','fitness and yoga trainer','weight training','vinyasa yoga')
obj4.display2()




