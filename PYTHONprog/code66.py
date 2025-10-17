class Employee:
    companyName = "Apple" # this is a class Variable
    noOfEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_value = 0.5 # These are called instance variable
        Employee.noOfEmployee += 1

    def showDetails(self):
        print(f"The name of the Employee is {self.name} in {self.noOfEmployee} sized company {self.companyName} and the raise percentage is {self.raise_value}") 
        # These are called instance variable


emp1 = Employee("Sam")
emp1.raise_value = 8
emp1.companyName = "Microsoft"
emp1.showDetails()

print(Employee.companyName)

Employee.companyName = "Google"

emp2 = Employee("John")

emp2.showDetails()

# Note 
"""
Class variables are shared among all the instances of a class and are used to store information that is common to all instances. 
Instance variables are unique to each instance of a class and are used to store information that is specific to each instance
"""