# lists
# marks = [3, 4, 5, "A", True, 34, 55, "79", 30, 78]

# print(marks)
# print(len(marks))
# print(marks[9])
# print(marks[0:9]) #whatever number is after ":" (say 9), it will print till the previous index of that(which will be 8)
# print(marks[0:-1]) # here just put : len() - 1 (here 10-1 = 9), and this will also print till a previous index(which will be 8)
# print(marks[0:9:1])# it's a jumper, 3rd number 
# print(marks[0:4:2])
# print(marks[0:5:2])
# print(marks[0:5:1])

lst0 = [i for i in range(10)]
print(lst0)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)
# lst = [i*i for i in range(10) if i%2 == 1]
# print(lst)

lst1 = ["How", "are", "you", "bro", "?"]
lst1with_o = [item for item in lst1 if "o" in item]
print(lst1with_o)

lst0.append(10)
print(lst0)
l0 = [6, 3, 4, -1]
lst0.extend(l0)
print(lst0)
# lst0.sort()
# print(lst0)
# lst0.sort(reverse=True)
# print(lst0)
print(lst0.index(-1))

print(lst0.count(-1))
m = lst0.copy()
m[0] = 1
print(lst0)

lst0.insert(1, 899)
print(lst0)

lst07 = [47, 56, 21]
lst007 = lst0 + lst07
print(lst007)
