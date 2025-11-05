# Multiple Inheritence
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of the Employee is {self.name}")

class sales:
    def __init__(self, designation):
        self.designation = designation

    def show(self):
        print(f"{self.designation}\n")
    
class salesEmployee(Employee, sales):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    
    def __str__(self):
        return f"This is {self.name}, who will be our new {self.designation}."
    
a = salesEmployee("Mark", "Sales Manager")
print(a)
a.show() # --> whichever parent class you put first will print their method

# another example for multiple inheritence
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def make_sound(self):
#         print("Sound made by the Animal!")

# class Mammal:
#     def __init__(self, name, fur_color):
#         self.name = name
#         self.fur_color = fur_color

# class Dog(Animal, Mammal):  # --> whichever is placed in a first position, will get the priority over functions
#     def __init__(self, name, breed, fur_color):
#         Animal.__init__(self, name, species = "Dog")
#         Mammal.__init__(self, name, fur_color)
#         self.breed = breed

#     def make_sound(self):
#         print("Bark!")

# a = Dog("Trigger", "Labrador", "White")
# a.make_sound()
