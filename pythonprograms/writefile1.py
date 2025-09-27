# if path is not mentioned.. file gets created in current directory
# fobj acts like cursor for navigating between the lines
fobj = open("info.txt","w")

fobj.write("python\n")
fobj.write("java\n")

fobj.writelines(["ruby","react","nodejst\n"])

for val in range(1,10):
    fobj.write(  str(val)   + "\n")

fobj.close()


# below code erases the file content
fobj = open("info.txt","w")
fobj.write("unix shell scripting\n")
fobj.close()

# below code apends the new content to existing file
fobj = open("info.txt","a")   # append mode  
fobj.write("unix shell scripting\n")
fobj.close()
