#Local vs Global Variables

x = 10 
print(x)

def func():
    x = 4
    return f"This is a local variable {x}"


print(f"This is a global variable {x}")
print(func())

x = 9           # this is how you change a global variable
print(f"This is a global variable {x}")

# what if you wanna change a global variable from inside a function

y = 10 
print(y)

def func():
    global y 
    y = 4
    return f"This is a local variable {y}"



print(f"This is a global variable {y}")
print(func())
print(f"This is a global variable {y}")
