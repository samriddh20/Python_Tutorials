#getters and setters

#Getters in Python are methods that are used to access the values of an object's properties

class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")
    
    @property
    def ten_value(self):
        return 10 * self._value

#Now what if you wanna assign some new value to the "value" arguement, you will have to use setters

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10



a = MyClass(10)
a.show()
print(a.ten_value)

a.ten_value = 2000
a.show()

