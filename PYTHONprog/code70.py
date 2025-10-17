class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    # This cls will act as employee, and the first split as name and the second split as salary

e = Employee("Sam", 250000)
print(e.name)
print(e.salary)

string = "John-12000"
# e2 = Employee(string.split("-")[0], string.split("-")[1]) # Now this looks a little messy to change the format like this
# so, why don't we add something like this in our class, so that it would take the format automatically

e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
