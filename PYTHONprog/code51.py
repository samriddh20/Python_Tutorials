# with open('myfile.txt', 'r') as f:
#     f.seek(10) # this will put you in the 10th byte position and now all the reading starts from here
#     print(f.read(10)) # this will start it's reading from 11th byte till 10 more bytes

#     print(f.tell()) # this will tell you the exact position where we currently are


with open('samplefile.txt', 'w') as f:
    f.write('Bella Ciao!')
    f.truncate(5)

with open('samplefile.txt', 'r') as f:
    print(f.read())