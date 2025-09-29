
import os
# object oriented
class FileOperations:
    def __init__(self,filename):
        self.filename = filename
    def createObject(self):
        try:
            if os.path.isfile(self.filename):   
                self.fobj = open(self.filename,"r")
        except Exception as err:
            print(err)
    def readFile(self):
        try:
            for line in self.fobj:
                print(line.strip())
        except Exception as err:
            print(err)
filename ="employees.txt"
if os.path.isfile(filename) and os.path.getsize(filename) > 0 :
    file1 = FileOperations(filename)
    file1.createObject()
    file1.readFile()
else:
    print("file is not found")
