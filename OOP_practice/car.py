
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

new_car = Car('audi', 'a4', 2016)
print(new_car.get_descriptive_name())
new_car.read_odometer()