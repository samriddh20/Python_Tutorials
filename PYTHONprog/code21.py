# def average(a, b):
#     print("The average is", (a+b)/2)

# average(5, 7)/

def average(*numbers): # the star before it makes it a tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("average is", sum/len(numbers))
    return sum/len(numbers)

c = average(5, 6)
print(c)
