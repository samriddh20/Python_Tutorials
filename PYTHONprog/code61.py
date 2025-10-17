#Inheritence

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The Employee with id: {self.id} is {self.name}")

#Now let's suppose I wanna add programming language also here

#Does that means I have to change the Employee class?
#No it will be messy, instead we will use inheritence

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Sam", 650)
e1.showDetails()
# e2 = Employee("Jack", 310) # Now this will not show you the language details
# e2.showDetails()

e2 = Programmer("Jack", 310)
e2.showDetails()
e2.showLanguage()

