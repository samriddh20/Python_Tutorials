 #For functions we use parenthesis (), for SLICING we use square brackets []
# In splicing if we get [0:-3], then it is just then length of the string minus 3


fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit)
print(fruit[0:-3]) #which means RHS -> len(fruit) - 3 = 2, so [0:2]
print(fruit[-3:-1]) #which means LHS -> len(fruit) - 3 = 2, so [2:4]

