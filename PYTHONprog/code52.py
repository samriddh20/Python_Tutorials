double = lambda x : x*2
# print(double(28))


#this is how you use function as an arguement in another function
def appl(fx, value):
    return 6 + fx(value)

# print(appl(double, 14))

#also you can directly put a lambda function in here

print(appl(lambda x: x*x*x, 4))

add = lambda x, y: print(f"{x} * {y} = {x*y}")

add(3, 4)