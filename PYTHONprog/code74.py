# ---------------------Method Overriding------------------------------

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def area(self):
#         return self.x*self.y

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14*self.radius*self.radius

# rec = Shape(4, 5)
# print(rec.area())

# c = Circle(4)
# print(c.area())

# Here's another way to do so


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius) # this is how method overriding works

    def area(self):
        return 3.14*super().area()
    
c = Circle(4)
print(c.area())

# here you used inheritence
