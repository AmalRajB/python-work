class person:
    def __init__(self,name:str,age:int):
        self.name:str=name
        self.age:int=age

    def show_details(self):
        print(f'name : {self.name} age: {self.age}')

class employee(person):
    def __init__(self,name:str,age:int,id:str,**kwargs):
        super().__init__(name, age,**kwargs)

        self.id:str=id 

    def show_details1(self):
            print(f'name: {self.name} age :{self.age} id : {self.id}')    

class parttime(person):
    def __init__(self,name:str,age:int,workinghours:float,**kwargs):
        super().__init__(name, age,**kwargs)
        self.workinghours:float=workinghours
    def show_details2(self):
            print(f'name: {self.name} age :{self.age} working_hours : {self.workinghours}') 


class consultant (employee,parttime):
    def __init__(self, name:str, age:int, id:str, workinghours:float, project_name:str):
        super().__init__(name, age, id=id, workinghours=workinghours)
        self.project_name:str = project_name

    def show_details3(self):
        print(f'name: {self.name} age: {self.age} id: {self.id} working_hours: {self.workinghours} project_name: {self.project_name}')
            

           


obj1=person('Alice',30)
obj1.show_details()

obj2=employee('amal',21,'EMP001')
obj2.show_details1()

obj3=parttime('athul',22,6.5)
obj3.show_details2()

obj4=consultant('anusree',24,'AART11',8.1,'python')
obj4.show_details3()







      

