# break statement

# for i in range(12):
#     if(i==10):
#         break
#     print("5 x", i+1, "=", 5 * (i+1))
    

# print("out of the loop now")


for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 x", i+1, "=", 5 * (i+1))

#replica of Do while loop in C/C++
 
a = 0
while True:
    print(a)
    a = a + 1
    if(a%100 == 0):
        break
    
