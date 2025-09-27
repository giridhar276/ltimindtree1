

# traditional way # regular way
fobj = open("info.txt","w")
fobj.write("python\n")
fobj.close()



######### context manager
# if any line starts with keyword with.. it is called as context manager
# Advantage : file will be closed automatically
# other examples: database connections, network connections we use context mgr

# once you move out of indentation .. file gets closed

# pythonic way # modern way
with open("info.txt","w") as fobj:
    fobj.write("python\n")
    print(fobj.closed) #False # file is not closed here
print(fobj.closed)     #True - file is closed here






