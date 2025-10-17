#tuple
# tup = (1, 2, 3, 4, 32, 356, True, "alpha", 21)
# print(type(tup), tup)

# print(len(tup))
# print(tup[0])
# print(tup[1])
# print(tup[3])

# if "alpha" in tup:
#     print("Yes ")

# tup2 = tup[1:5]
# print(tup2)
# print(tup[:-1])

#Operations with tuples
#Note: Tuples are immutable, you can only make changes by converting it to a list

# name = ("Australia", "America", "Alaska", "Antartica", "Africa")
# print(type(name), name)

# ## name.append("Argentina")   #This will throw an error coz tuples are immutable
# name1 = list(name)
# name1.append("Argentina")
# name1.pop(2)
# name = tuple(name1)
# print(name)

#tuples can concatenate

t = (1, 2, 3, 4, 5)
q = (4, 3, 2, 1)
r = t + q
print(type(r), r)
print(r.count(3))
print(r.index(3))
print(r.index(3, 4, 7))