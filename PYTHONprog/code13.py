def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
#this is how we make a function, so that we can recall it without writing the logic everytime

def isGreator(a, b):
    if(a>b):
        print("First number is greator")
    else:
        print("second number is greator or equal")

def isLesser(a, b):
    pass # this is saying run the rest of the code and ignore this for now, this will be defined later, in case you don't write 'pass' you will get the error
 
a = 8
b = 9

isGreator(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)
 


c = 7
d = 8
isGreator(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)

# if(c>d):
#     print("First number is greator")
# else:
#     print("second number is greator or equal")