# l = [9 , 5, 14, 56, 3, 44, 9, 44, 56]
# print(l)

# print(l[::-1])# reversed a list without using revrese function

# for i in range(len(l)-1, -1, -1):
#     print(l[i], end= " ")

# # names = ["a", "b", "c"]
# # print(names)
# # names.insert(0, "d")
# # names.insert(4, "e")
# # print(names)

# l.sort()
# print(l)
# print(l[0])
# print(l[5])

# l.remove(9)
# print(l)

# # Given a list of strings, make a new list that contains only the strings with length greater than 3.
# a = ["Hey", "Good", "Morning", "How", "are", "you", "?"]

# -------------------------------------------------------------------------------------------------------------------
numbers = [4, 9, 2, 7, 5]
print(numbers)
largest = numbers[0]
smallest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

# ------------------------------------------------------------------------------------
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []

# for num in numbers:
#     if num not in unique_list:
#         unique_list.append(num)
#         print(unique_list)

# --------------------------------------------------------------
# words = ["hi", "hello", "cat", "world", "py"]
# long_words = []

# for i in words:
#     if len(i) > 3:
#         long_words.append(i)

# print(long_words)

# ------------------------------------------------------------------------
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# l = []

# for i in a:
#     if i%2 == 0:
#         l.append(i*i)  # --> or l.append(i**2)
#         print(l)  
# print(l)

# -------------------------------------------------------------------------

############[[1,2],[3,4],[5]] → [1,2,3,4,5]
# l = [[1,2],[3,4],[5]]
# m = []

# for i in l:                # for this you have to go to the nested list by pulling out a nested for loop
#     for j in i:
#         m.append(j)
#         print(m)

# ---------------------------------------------------------------------------
# Write a program to find the second largest number in a list without sorting.

a = [4, 9, 2, 7, 5]

largest = second_largest = float('-inf')

for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i> second_largest and i != largest:
        second_largest = i

print(largest)
print(second_largest)


# ------------------------------------------------------------------------------
#Given two lists, create a new list containing only the elements common to both.
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [1, 3, 5, 6, 7, 8, 9, 10, 11]
# z = []

# for i in x:
#     for j in y:
#         if i == j:
#             z.append(i)
# print(z)
            



