

  
########## raising default exception ######
if 1 < 2 :
    raise Exception("error found")

########## raising default exception ######
name = "python"
if not name.isupper():
    raise Exception("its not upper")
    
######### raising using NameError ##########
if name.islower():
    raise NameError("its lower")


############################ writing your own Exception ###########

class MyOwnException(Exception):
    pass

name  = "python"
if name.islower():
    raise MyOwnException("its lower")

