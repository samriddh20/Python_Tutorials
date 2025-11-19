# Hybrid Inheritance

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class child(Derived1, Derived2):
    pass


# Hierarchical Inheritance
class CEO:
    name = "Shayne Elliot"
    def __init__(self):
        self.name = "Shayne Elliot"
    def __str__(self):
        return f"{self.name} is the CEO of this Company"

class COO(CEO):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is the COO of this company"

class CTO(CEO):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} is the CTO of this company"
    
    def showDetails(self):
        print(f"Welcome to the Technical Domain of this company")

class ManagerO(COO):
    def __init__(self, name):
        self.name = name
        self.domain = "Operations Manager"
    
    def __str__(self):
        return f"{self.name} is the {self.domain} of this company"

class ManagerT(CTO):
    def __init__(self, name):
        self.name = name
        self.domain = "Technical Manager"
    
    def __str__(self):
        return f"{self.name} is the {self.domain} of this company"
    
    def showDetails(self):
        CTO.showDetails(self)
        print(f"Manager of Technical department")


a = CEO()
print(a)

b = COO("Alison Burgers")
print(b)

c = CTO("Baba YAGA")
print(c)

d = ManagerO("Bryan")
print(d)

e = ManagerO("Adam")
print(e)

f = ManagerT("Jessica")
f.showDetails()
print(f)


