
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

new_car = Car('audi', 'a4', 2016)
print(new_car.get_descriptive_name())
new_car.read_odometer()
print('\n')

#test update odometer
new_car.update_odometer(23)
new_car.read_odometer()
print('\n')

#second test
used_car = Car('subaru', 'outback', 2013)
print(used_car.get_descriptive_name())
used_car.update_odometer(23500)
used_car.read_odometer()

used_car.increment_odometer(100)
used_car.read_odometer()




