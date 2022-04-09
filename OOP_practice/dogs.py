class Dog():
    """first model with animal"""
    
    def __init__(self, name, age) -> None:
        "Name and age atributes"
        self.name = name
        self.age = age

    def sit(self):
        '''Make the dog to sit'''
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()