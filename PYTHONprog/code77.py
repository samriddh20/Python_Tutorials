# Operator Overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, a):
        # return f"{self.i + a.i}i + {self.j + a.j}j + {self.k + a.k}k" # results type would be <class 'str'>, but if we make it:-
        return Vector(self.i + a.i, self.j + a.j, self.k + a.k) # <class '__main__.Vector'>


v1 = Vector(2, 3, 5)
print(v1)
v2 = Vector(1, 4, 6)
print(v2)

print(v1 + v2) # if you simply add it like that, it will throw an error saying + is an unsupported operand
# now look at the __add__ operator that I'm gonna put in the class

print(type(v1+v2))

# refer to this page for more info
# https://docs.python.org/3/library/operator.html