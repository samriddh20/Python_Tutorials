#Finally Clause

def func():
    try:
        l = [1, 3, 5, 7]
        i = int(input("Enter your index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This will always be executed")

# def funci():
#     try:
#             l = [1, 3, 5, 7]
#             i = int(input("Enter your index: "))
#             print(l[i])
#             return 1
#     except:
#             print("Some error occured")
#             return 0

#     print("This will always be executed")

x =func()
print(x)