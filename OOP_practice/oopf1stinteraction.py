'''Parent'''
class Drink:
    def __init__(self,name) -> None:
        self.name = name
    def getDetails(self):
        return " The drink is: " + self.name

#Son
class Beer(Drink):

    #proper object
    count = 0
    def __init__(self, name, brand, alcohol) -> None:
        super().__init__(name)
        self.brand = brand
        self.alcohol = alcohol
        Beer.count += 1

    # This use the parent class and brand, alcohol from Beer class
    def getDetails(self):
        return super().getDetails() + " the brand is " + self.brand + " with " + str(self.alcohol) + " of alcohol "
beer1 = Beer("Pale Ale", "Minerva", 4.5)
#this connect the class Beer with the class Drink and use getDetails print the name, but
# we can make a new getDetails to the class Beer that overwrite the parent class
print(beer1.getDetails())

beer2 = Beer("Corona", "Corona", 0.3)
print(beer2.getDetails())

print(Beer.count)