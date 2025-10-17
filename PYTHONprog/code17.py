countries = ("A", "B", "C", "D", "E")
temp = list(countries)
temp.append("F")
temp.pop(3)
temp[2] = "X"
countries = tuple(temp)

print(type(countries), countries)

countries2 = ("G", "H", "I")
continent = countries + countries2
print(continent)

res = countries.count("A")
print(res)