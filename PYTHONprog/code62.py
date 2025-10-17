# Access Modifiers

# Types of modiefiers:-
#     Public access modifier
#     Private access modifier
#     Protected access modifier


#  Public access modifier

class Employee:
    def __init__(self):
        self.name = "Sam"
    
a = Employee()
print(a.name)

#  Private acess modifier

class Student:
    def __init__(self):
        self.__name = "Amanda" # by putting a double underscore you make a variable or method as private
        # this is called NAME MANGLING 
    
b = Student()
# print(b.__name) # so if someone try to access it they can't

# But if someone want's to access it anyways:
print(b._Student__name) # they can access like that

# print(b.__dir__()) # this will tell you more methods like this, that you can apply in this class

class People:
    def __init__(self, age, name):
        self.__age = age 

    def __function(self):
        self.y = 34
        print(self.y)

class subject(People):
    pass

a = People(24, "Amy")
b = subject

# print(a.__age)                    #can't access both the variable and function (in class and sub class both)
# print(a.__function)
# print(b.__age)
# print(b.__function)


#     Protected access modifier

class Bike:
    def __init__(self, brand, year):
        self._brand = brand             #it's just a label that it is protected variable [single underscore prefix (_)]
        self._year = year

    def __func(self): 
        self._x = "bikes"

c = Bike("BMW", 2025)
print(c._brand)
print(c._year)
    

