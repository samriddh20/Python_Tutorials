import os


folderPath = r"D:\python1\os module\sample_photos"
photo_no = 1

for file in os.listdir(folderPath):
    os.rename(folderPath + '\\' + file, folderPath + '\\' + "Sample_" + str(photo_no) + '.png')
    photo_no +=1
