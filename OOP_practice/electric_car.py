
class Car():

    def __init__(self, make, model , year) -> None:
        self.make = make
        self.model = model
        self.year = year
        #default value as an atribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {str(self.odometer_reading)} miles on it.')

    #update the value of the odometer
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")
    
    #increase odometer value
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    #Bettery attributes
    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This battery has a {str(self.battery_size)}-kwh battery.")
    def get_range(self):
        if self.battery_size ==70:
            range =240
        elif self.bettery_size ==85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += " miles on a full charge."
        print(message)

#child class
class ElectricCar(Car):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()

   
    
#test 1
my_tesla = ElectricCar('Tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

#test  2
my_tesla.battery.get_range()