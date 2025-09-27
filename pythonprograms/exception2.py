try:
    fobj= None
    fobj =  open("employees.txt","r")

except Exception as err:
    print("file is not found",err)

else:
    for line in fobj:
        print(line.strip())

finally:
    if fobj is not None:
        print("closing the     file")
        fobj.close()
    
        
