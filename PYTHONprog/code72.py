# class Parent:
#     def parent_method(self):
#         print("this is parent method")
    
# class Child(Parent):
#     def child_method(self):
#         print("this is child class")
#         super().parent_method()

# child_object = Child()
# child_object.child_method()

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company(Employee):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    
sam = Employee("Sam", 24)
ben = Company("Ben", 24, 30990)

print(ben.name)
print(ben.age)
print(ben.id)
