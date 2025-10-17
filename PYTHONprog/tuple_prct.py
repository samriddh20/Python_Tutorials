t = (1, 23, 13, 44, 27, 56, 98, 34, 23, 23, 23)

# # for i in t:
# #     print(i)

# print(t.count(23))

# name = ("Germen", "French", "Spanish", "Greek")

# if "Spanish" in name:
#     print("Yes")

t1 = list(t)
t1.insert(9, 17)
t1.append(63)
t = tuple(t1)
print(t)

#Given a tuple of integers, find the maximum and minimum values without using max() or min().

# maxi = t[0]
# mini = t[0]

# for i in t:
#     if i>maxi:
#         maxi = i
#     elif i<mini:
#         mini = i
# print(maxi, mini)

# t2 = t1[2:5]
# t2 = t[2:5]
# print(t2)

# print(t2)

# tup = ((1, 2), (3, 4), (5,))
# tup1 = []

# for i in tup:
#     for j in i:
#         tup1.append(j)
# print(tup1)

# words = ("hi", "hello", "cat", "world", "py")
# long_words = []

# for i in words:
#     if len(i) > 3:
#         long_words.append(i)

# print(long_words)

# t3 = (1, 2, 3, 4, 5, 6)
# t4 = []
# for i in t3:
#     t4.append(i*i)

# print(t4)
# t5 = tuple(t4)
# print(t5)

p = (1, 3, 7, 8, 3, 6, 0, 3, 8)
p1 = []
p2 = []
p3 = []
q = 0
s = 0
# for i in p:
#     if i in p1:
#         p3.append(i)
#         p2.append(p.index(i))
#     else:
#         p1.append(i)
# print(p)
# print(p1)
# print(p2)
# print(p3)

for i in range(len(p)):
    if p[i] == 3:
        q+=1
    if q == 2:
        s = i 
        break
print("The second occurence of 3 is at ", s, "th index")



