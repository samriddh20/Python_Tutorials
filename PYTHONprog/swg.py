import random

list = ['Snake', 'Water', 'Gun']

Users_choice = input("Hey let's play Snake Water Gun\n What would you choose:\n")

computer = random.choice(list)

if (Users_choice == computer):
    print("Computer's choice is ", computer)
    print("It's a tie")
elif(Users_choice == "Snake" and computer == "Water"):
    print("Computer's choice is ", computer)
    print("You won from the computer")
elif(Users_choice == "Water" and computer == "Gun"):
    print("Computer's choice is ", computer)
    print("You won from the computer")
elif(Users_choice == "Gun" and computer == "Snake"):
    print("Computer's choice is ", computer)
    print("You won from the computer")
else:
    print("Computer's choice is", computer)
    print("You lost to the computer")
    
