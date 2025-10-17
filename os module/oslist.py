import os

folders = os.listdir("data")

print(os.getcwd()) #this will give you location of your directory
os.chdir("\python1")
print(os.getcwd()) #this will change your directory

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))
