# f = open('myfile1.txt', 'r')

# # line = f.readline()
# # print(line)

# i=0

# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break

#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]

#     print(f"Marks of student {i} in Maths is {m1}")
#     print(f"Marks of student {i} in Chemistry is {m2}")
#     print(f"Marks of student {i} in Physics is {m3}")
#     print(line)


# # --> In the below example there are a few elements in line hence we can manually put \n for the next line 
# f = open('myfile2.txt', 'w')

# lines = ['line1\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()

# But this ex will tell you how to add next line character without actually putting it after every element

f = open('myfile2.txt', 'w')

lines = ['line1', 'line2', 'line3']

for line in lines:
    f.write(line + '\n')

f.close()