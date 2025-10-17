#Raising customer errors

a = input("Enter any number between 5 and 9: ")

if(a == "quit"):
    print("Better luck next time!")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Value should be between 5 and 9")


    