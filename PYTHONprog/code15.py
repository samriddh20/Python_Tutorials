l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort()
# l.sort(reverse = True)
# l.reverse()
# print(l.index(1)) # this gives index of first occuring of that item
# print(l.count(1))
# m = l.copy() #this way main list 'l' will not undergo the changes for 'm' list
# m[0] = 0
# l.insert(1, 899) # it says insert 899 at index no 1
# m = [900, 1000, 1100]
# l.extend(m) # this will append list 'm' to the list 'l'

# one more way for the above
m = [900, 1000, 1100]
k = l + m
print(k)
print(l)

