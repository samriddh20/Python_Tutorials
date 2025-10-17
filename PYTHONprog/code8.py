import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))

if(4<timestamp < 12):
    print('Good Morning')
elif(12 < timestamp < 17):
    print('Good Afternoon')
elif(17 < timestamp < 21):
    print('Good Evening')
else:
    print('Good Night')

# timestamp = time.strftime('%M')
# print(timestamp)

# timestamp = time.strftime('%S')
# print(timestamp)