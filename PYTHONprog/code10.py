# For Loops

# name = 'samriDdh'

# for i in name:
#     print(i)
#     if(i == 'D'):
#         print('This is a capital letter')

colors = ['Red', 'Green', 'Blue', 'Yellow']

for color in colors:
    print(color)
    for i in color:
        print(i)


for k in range(5):
    print(k) # it will print 0 to 5, whereas if you give print(k+1) then it will print 1 to 5

for k in range(1, 9):
    print(k) # it will print from 1 to 8

for k in range(1, 12, 2): #  range(start, stop, step)
    print(k) # it reads it as print 1 then add 1+2 and print the next number which is 3, then again add 2 and print the next number which is 5
