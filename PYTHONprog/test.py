# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))

# print("Addition :", a+b)
# print("Subtraction :", a-b)
# print("Multiplication :", a*b)
# print("Divison :", a/b)

def calculator(a, b):
    sum = a+b
    sub = a-b
    Multpily = a*b
    Division = a/b
    return f"The Sum is {sum},\nThe Sub is {sub},\n, The multiplication is {Multpily},\nThe division is {Division}"


val = calculator(10, 2)
print(val) 
