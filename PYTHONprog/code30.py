#recursive function

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

#here we use function inside the same function

def fibonacci(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
