tup = (1, 2, 76, 342, 32, "green", True)
# d = (1, 2, 76, 342, 32, "green", True)

print(type(tup), tup)
# print(type(d), d)

print(tup[0])
print(tup[1])
print(tup[2])

if 342 in tup:
    print("Yes it's there in this tuple")


# tup2 = tup[1:4]
# print(tup2)
# print(tup)

print(tup[:4])