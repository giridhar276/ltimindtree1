# taking input from user and writing to file

user = input("Enter a string: ")
with open("newfile.txt","w") as fobj:
    fobj.write(user)
