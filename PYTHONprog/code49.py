f = open('myfile.txt', 'r')
# print(f)              #--> this will give you something like this <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>


# HOW TO READ A FILE
# text = f.read()
# print(text)
# f.close()

# HOW TO WRITE A FILE
# f = open("myfile.txt", 'w')

# f.write()
# f.close()        #--> this will wipe out the data from the myfile.txt as we have not given anything to write, if we do then it would remove the data and add the new one

# f.write('Hey Bro, myfile.txt content has wiped out ')
# f.close()

# how to append

# f = open("myfile.txt", "a")
# f.write("\t I'm just getting appended")
# f.close()

#another way of appending/writing/reading 
with open('myfile.txt', 'a') as f:
    f.write("\n I'm the new way of appending")