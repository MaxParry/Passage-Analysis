import os
import path

source_directory = 'input_data'
file1 = 'paragraph_1.txt'
file2 = 'paragraph_2.txt'
filelist = [file1, file2]

passagelist = []

for afile in filelist:
    path = os.path.join(source_directory, afile)
    with open(path, 'r', newline='') as f:
        passagelist.append(f.read())



