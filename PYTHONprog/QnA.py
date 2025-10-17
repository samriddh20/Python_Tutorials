Questions = [
    "1. Which institution developed India's first ‘Farmland price index’?\ni. IIT Madras\tii. IIM Ahmadabad\tiii. IIM Bengaluru\tiv. IISc Bengaluru",
    "\n2. Panna Tiger Reserve is located in which state/UT?\ni, Madhya Pradesh\tii. Maharashtra\tiii. Gujrat\tiv. Rajasthan",
    "\n3. Which company recently announced to launch ‘AMBER alerts’ to find missing children?\ni. Microsoft\tii.Google \tiii.Meta \tiv.Apple",
    "\n4. India’s first liquid-mirror telescope has been commissioned in which state/UT?\ni.Sikkim\tii. Jammu and Kashmir\tiii. Uttarakhand\tiv. Himachal Pradesh",
    "\n5. Uttarakhand Chief Minister Pushkar Singh Dhami won the bypoll from which constituency?\ni. Champawat\tii. Khatima\tiii. Gangotri\tiv.Yamunotri"
]

Answers = [2, 1, 3, 3, 1]

name = input("Enter your name: ")
print("Hello", name, ", let the game begin")

Amount_earned = 0

for i in range(len(Questions)):
    print(Questions[i])
    ans = int(input("Enter your answer(1, 2, 3, or 4): "))
    if ans == Answers[i]:
        print("Absolutely Correct!")
        Amount_earned += 10000  # Increment the amount earned
        print("You've earned Rs:", Amount_earned)
    else:
        Amount_earned -= 500
        print("I'm afraid it's a wrong answer.\n The correct Answer is:", Answers[i],"\n You've earned Rs:", Amount_earned)
    if i < len(Questions) - 1:
        input("Press Enter to continue to the next question...")
    else:
        print("\nThank you for playing with us\nYou won Rs:", Amount_earned)
