# a = 300
# b = 3300

# print("A") if a>b else print("=") if a==b else print("B") # these are called short hand if else statments
# # they are used to incorporate simple logics into one line for better readibility

#making a manual library here
# def welcome():
#     print("You are welcome in this library")

# if __name__ == "__main__":
#     welcome()

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Testing add function....")
    print(add(5,3))

