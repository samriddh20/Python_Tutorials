# strings are immutable

a = "Sam!!!!!!!!!!!!!!!!"

c = "Jai Shree Ram"

b = "!!Sam!!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # it only strips trailing characters, not the leading characters
print(b.rstrip("!"))
print(a.replace(a, b)) # or
print(a.replace("Sam", "Nivs"))
print(c.split(" "))
# capitalize() turns the first character to uppercase and rest all to lower
print(a.count("!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) # results as a boolean data type

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) # we can overright a variable
# find() method will give us the index positioning of the first occurence
# isalnum() method tells us if the string is made of A-z, a-z, 0-9
#isaplha() method tells us if the string is made of A-z, a-z