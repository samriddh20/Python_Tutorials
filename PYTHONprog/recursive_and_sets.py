# def func(n):

#     if n==1:
#         return 1
#     else:
#         return n, func(n-1)
    
# print(func(1))
# print(func(2))
# print(func(3))
# # -----------------------------------------------------------

# def sum(n):
#     if n==1:
#         return 1
#     elif n <= 0:
#         return "This is not a natural number"
#     else:
#         return n + sum(n-1)
    
# print(sum(0))
# print(sum(1))
# print(sum(2))
# print(sum(3))
# print(sum(5))
# -------------------------------------------------------------------------
# Write a recursive function to count the digits of a number.

# def digi_cnt(n):
#     if n==1:
#         return 1
#     else:
#         for i in n:

# n=47899
# m = str(n)
# print(len(m))
# def digi_cnt(n):      
#     if n == 0:
#         return 1  # Special case for 0, which has one digit
#     elif n < 10:
#         return 1  # Base case: single-digit number
#     else:
#        # Recursive step: remove one digit and add 1 to the count of remaining digits
#         return 1 + digi_cnt(n // 10)
    
# print(digi_cnt(47899))

# print(10/2) # normal division that gives a float value
# print(10//2) # integer division that gives integer value

# s = {96, 2, 1, 4, 5, 3, 0, 2}
# print(type(s), s)

# if 2 in s:
#     print("Yes")

# s.add(27)
# print(s)
# s.update({2, 9, 10})
# print(s)
# s.remove(2)
# print(s)
# s.discard(27)
# print(s)
# # s.pop(10) # this won't work coz it can only remove a random element just like below
# s.pop()
# print(s)

# my_set = {1, 2, 3, 4}
# removed_element = my_set.pop()
# print(f"Removed element: {removed_element}")
# print(my_set)# Output will vary depending on which element is popped