# class Employee:
#     name = "Sam"

# e = Employee()
# print(e.name)
# print(len(e))

#Now in the above example if you wanna get a len of the class's attribute, this is not the way
#we have special methods/magic methods to do so

# class Employee:
#     name = "Sam"

#     def __len__(self):
#         i=0
#         for c in self.name:
#             i += 1
#         return i

# e = Employee()
# print(e.name)
# print(len(e)) # in this case you simply got the answer by calling the function with 'len' and not '__len__'

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self): # this is basically the face of the class
#         return f"The Employee is {self.name}"    
    

# e = Employee("Selena")

# # print(e) # whenever you run this, it won't give you the actual information, it would provide you with some memory location like <__main__.Employee object at 0x000001DC3057AB50>
# print(e)

#similary we also have reaper method

# class Employee:
#     def __init__(self, name):
#         self.name = name
    
#     # def __str__(self): # this is the by default face regardless of reaper being in the class
#     #     return f"The employee is {self.name} str"
    

#     def __repr__(self):
#         return f"Employee: ({self.name})"
    
# e = Employee("Kendrick")
# print(e) # if you comment out str then reaper method takes it's place
# print(str(e)) # you can call them by these names as well
# print(repr(e))


class Employee:
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print("Hey Bro")

e = Employee("Bruce")
e() # this is how you can call an object from the class

# you can perform more use case in this call function

class People:
    def __init__(self, name, region):
        self.name = name
        self.region = region
    
    def __call__(self):
        print(f"This is {self.name}, from {self.region}")

e = People("Alex", "Mexico")
e() # so the thing written on the __call__ function would return
#this is how you can call function