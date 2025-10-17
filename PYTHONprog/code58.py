# class Person:
#     def __init__(self): # this is known as a constructor
#         print("Hey I'm a Person!")

# a = Person()

#Now you like you saw, this is like an initialization, if you only give self with __init__ function, it takes one variable
#how about you like to add more values/variables in it

class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Anna", "Research Analyst")
a.info()
b = Person("Mark", "Developer")
b.info()


c = Person()
c.info() 
#Here you will get the below error

# Person.__init__() missing 2 required positional arguments: 'name' and 'occ'

#Now you might wonder why it as missing 2 arg not three as self was also there in the __init__ func
#This is because "c" is the self arg which it takes automatically 