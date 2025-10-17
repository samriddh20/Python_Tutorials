# F string

# letter = "Hey my name is {} and I am from {}"
# name = "Sam"
# country = "India"

# print(letter.format(name, country))

# letter = "Hey my name is {1} and I am from {0}"

# print(letter.format(country, name)) 
# # # Now to avoid giving sequence to every statement we have a solution

# print(f"Hey my name is {name} and I am from {country}")
# # # if you want to display exactly {name} and {country} you gotta put them into double curcly braces
# print(f"Hey my name is {{name}} and I am from {{country}}")


# txt = "For only {price: .2f} dollars!" # .2f will round of the number to 2 decimal places
# print(txt.format(price = 49.0999))
# # Now a better way

price = 49.0999
txt = f"For only {price:.2f} dollars!"
print(txt)