# x = [1, 2, 4, 6, 7]
# # print(x.__dir__)
# print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("John", 30)
print(a.__dict__)

print(help(Person))