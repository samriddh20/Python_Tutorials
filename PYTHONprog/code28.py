#f-strings practice

radius = 30
area = 3.14*radius**2

print(f"The area of the circle with radius {radius} is {area:.2f}")

a = 10
b = 90
print(f"a + b = {a + b}")

#Print a number in binary and hexadecimal format using f-string.

number = 42

print(f"Binary (no prefix): {number:b}")
print(f"Binary (with prefix): {number:#b}")
print(f"Binary (padded): {number:08b}")
