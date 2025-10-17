#MAP----------> map(function, iterable)

def square(x):
    return x*x

print(square(4))

l = [1, 2, 3, 6, 4, 8]

#now if you have to square each of the items present in the list

newl = []
for i in l:
    newl.append(square(i))

print(newl)

#now a more optimal way

sqr = list(map(lambda x: x*x, l))
print(sqr)

#Filter -----------------------> filer(predicate, iterable) means if the predicate is true filter those instances

even = list(filter(lambda x: x%2 == 0, l))
print(even)

#Reduce -----------------------> reduce(function, iterable)

from functools import reduce

sum = reduce(lambda x,y: x+y, l)

print(sum)


