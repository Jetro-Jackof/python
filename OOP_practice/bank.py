class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        return f"Thank you", (self.age) "year old", (self.name.title())"

class Bank(user):
    total_deposit = 0
    total_withdraw = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
    
    def show_info(self):
        return f"(self.name) has a remaining balance of: round(self.balance,2)"

    def deposit(self):
        dep = float(input(f"(self.name.title(), please enter you deposit"))
        print(f'Thank you for your deposit')
        self.balance = dep
        self.total_deposit += 1
        return f"Your balance is: round((self.balance),2)"