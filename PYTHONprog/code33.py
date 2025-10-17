#dictonaries
d = {'name':'Sam', 'age':'24', 'height':'184'}

# print(d)
# print(d['age'])
# print(d.keys())
# print(d.values())
# print(d.items())

# # for i in d:
# #     print(i)

# for i, j in d.items():
#     print(f"{i} : {j}")


ep1 = {566:40, 789:70, 463:20, 952:80, 656: 50}
ep2 = {780:45, 899:73}

ep1.update(ep2)
ep1.pop(899)
ep1.popitem()
del ep1[463]
print(ep1)
