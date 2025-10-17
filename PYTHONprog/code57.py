class RoyalEnfield:
    name = "Intercepter"
    cc = "650"
    color = "Red"
    def info(self): #self helps the function to work over that particular variable
        print(f"{self.name} with {self.cc} cc engine, coming in {self.color}")

a = RoyalEnfield()

# print(a, type(a))
a.info()

a.name = "GT"
a.cc = "650"
a.color = "Chrome"

b = RoyalEnfield()
b.name = "Bullet Standard"
b.cc = "350"
b.color = "Black"

#all the data is getting encapsulated into one class making all these objects
#Now what will happen if you name an object for the given class, and don't put any details of it
c = RoyalEnfield()

#it will take the default value provided in the class
a.info()
b.info()
c.info()

