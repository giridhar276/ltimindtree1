

import os

# program to check whether the input is
# file or directory
for file in os.listdir():
    if os.path.isfile(file):
        print(file, "is a file")
    elif os.path.isdir(file):
        print(file,"is a directory")
