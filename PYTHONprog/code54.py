# 'is' vs '=='

a = [1,2,3]
b = [1,2,3]

print( a is b) # compares exact location of object in the memory
print(a == b) # compares value

# so for lists as they are mutable the exact memory location would be false but the value would be same 

c = (1,2)
d = (1,2)

print(c is d)
print(c == d)

# now for tuples, as they are immutable python creates only one memory location for two same tuples
# hence it will be the same for location as well as value
