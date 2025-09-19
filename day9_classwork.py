class vehicle:
    def __init__(self,vehicle_id:str,base_rate:float):
        self._vehicle_id:str=vehicle_id
        self._base_rate:float=base_rate
    def display_details(self):
        print(f'Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate}')

    def rental_charge(self):
        return 0.0

class car(vehicle):
    def __init__(self,vehicle_id:str,base_rate:float,num_seats:int):
        super().__init__(vehicle_id,base_rate)
        self.num_seats:int=num_seats
    def rental_charge(self):
        return self._base_rate * self.num_seats
class bike(vehicle):
    def __init__(self,vehicle_id:str,base_rate:float,bike_type:str):
        super().__init__(vehicle_id,base_rate)
        self.bike_type:str=bike_type
    def rental_charge(self):
        return self._base_rate * 0.5    
    
def calculate_rental(vehicle:vehicle):
    vehicle=vehicle.rental_charge()
    print(f'Rental Charge: {vehicle}')

car1 = car("CAR001", 1000.0, 4)
bike1 = bike("BIKE001", 500.0, "Scooter")  

car1.display_details()
calculate_rental(car1)

  
       

    
        



