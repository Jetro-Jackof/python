class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        return f"Thank you, {self.age} year old, {self.name.title()}"

class Bank(user):
    total_deposit = 0
    total_withdraws = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
    
    def show_info(self):
        return f"{self.name} has a remaining balance of: {round(self.balance,2)}"

    def deposit(self):
        dep = float(input(f"{self.name.title()}, please enter you deposit"))
        print(f'Thank you for your deposit')
        self.balance = dep
        self.total_deposit += 1
        return f"Your balance is: {round((self.balance),2)}"

    def withdraws(self):
        wd = float(input(f"{self.name.title()}, please enter how much you would like to withdraw"))
        if self.balance < wd:
            return "Your request exces your balance"
        else:
            print("Thank you for your withdraw")
            self.balance -wd
            self.total_withdraws += 1

def options(user2):
    print("Congratulations for you new bank account")
    print("Choose one option")
    while True:
        option_choice = int(input("1) Balance \n2) Withdraw \n3) Deposit \4) Total withdraws \n5) Total deposits \n 6) Finish"))
        if option_choice == 1:
            print(user_one_bank.show_info())
            if option_choice == 1 and user_two != None:
                print(user_two_bank.show_info())
        elif option_choice == 2:
            print(user_one_bank.withdraws())
            if option_choice == 2 and user_two != None:
                wd = input(f"{user_two.name} would you like to withdraw? Yes or No: ")
                if wd.lower()== 'yes':
                    print(user_two_bank.withdraws())
        elif option_choice == 3:
            print(user_one.ban.deposit())
            if option_choice == 3 and user_two != None:
                dep = input(f"{user_two.name} Would you like to deposit? Yes or No: ")
                if dep.lower() == 'yes':
                    print(user_two_bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_withdraws} withdraws.")
            if option_choice == 4 and user_two != None:
                print(f"There have been {user_two_bank.total_withdraws} withdraws.")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_deposit} deposit.")
            if option_choice == 5 and user_two != None:
                print(f"There have been {user_two_bank.total_deposit} deposit.")
        elif option_choice ==6:
            print("Thank you for your preference")
            return False
            break
        else:
            print("Please chose a number from 1 to 6")
def bank_creation(name):
    balance = float(input(f"{name.name.title()} Your account balance is:"))
    return balance

while True:
    print(f"Welcome to bank_name")
    name = input("Enter your name")
    age = int(input("Enter your age"))
    user_one = User(name,age)
    user_two = None
    new_user = input("Would you like to register a new user? Type No ")
    if new_user.lower() = 'yes':
        name= input("Enter the second person's name: ")
        age = int(input("Enter the second person's age:"))
        user_two= User(name, age) 
        print("Thank you for register a secod user ")
        user_one_balance =  bank_creation(user_one.name)
        user_two_balance =  bank_creation(user_two.name)
        user_one_bank= Bank(user_one.name, user_one.age,user_one.balance)
        user_two_bank= Bank(user_two.name, user_two.age,user_two.balance)
        flag = options(user_two)
        if flag == False:
            break
    else:
        user_one_balance = bank_creation(user_one.name)
        user_one_bank = Bank(user_one.name,user_one.age, user_one.balance)
        flag = options(user_two)
        if flag == False:
            break






































