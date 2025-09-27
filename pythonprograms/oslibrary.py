### os library
###  display all list of files from current directory( if path is not mentiond)
import os
print(os.listdir())

### default is current working directory
for file in os.listdir():
    print(file)

###### will display from C:
for file in os.listdir("C:\\"):
    print(file)

print("****** present working directory *****")
print(os.getcwd()) # pwd

print("******** display current user name ***********")
print(os.getlogin())

####
os.mkdir("mydir")

for val in range(1,5):
    os.mkdir( "dir" + str(val))

