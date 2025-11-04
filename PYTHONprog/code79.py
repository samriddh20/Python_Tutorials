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
        print(f"{self.designation}")
    
class salesEmployee(Employee, sales):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    
    def __str__(self):
        return f"This is {self.name}, the {self.designation}."
    
a = salesEmployee("Mark", "Sales Manager")
print(a)
a.show() # --> whichever parent class you put first will print their method