from functools import reduce

l = [5, 4, 99, 100, 7, 23]

# sqr = list(map(lambda x: x*x, l))
# print(sqr)

eves = list(filter(lambda x: x%2 == 0, l))
print(eves)

sqr_eves = list(map(lambda x: x*x, eves))
print(sqr_eves)

sum_sqr_eves = reduce(lambda x,y: x+y, sqr_eves)
print(sum_sqr_eves)

# sum = reduce(lambda x,y: x+y, l)
# print(sum)


max_num = reduce(lambda x,y: x if x>y else y, l)
print(max_num)

product = reduce(lambda x, y: x*y, l)
print(product)


a = ["Brian", "Gordon", "Kendrik", "Joe", "Avici"]
c = ["brian", "gordon", "kendrik", "joe", "avici"]


uc = list(map(lambda x: x.upper(), a))
print(uc)

cap = list(map(lambda x: x.capitalize(), c))
print(cap)

long_words = list(filter(lambda x: len(x)>5, a))
# print(long_words)

len_words = list(map(lambda x: len(x), a))
# print(len_words)

# words = ["apple", "banana", "cherry"]
# combined = reduce(lambda a, b: a + ", " + b, words)
# print(combined)  # 'apple, banana, cherry'

words = ["madam", "racecar", "hello", "level", "python"]
palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)  # ['madam', 'racecar', 'level']


