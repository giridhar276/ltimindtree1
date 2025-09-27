########### using default Exception #######
try:
    with open("employees3333.txt","r") as fobj:
        for line in fobj:
            print(line.strip())
            
except Exception as err:
    print(err)


################# adding more exceptions ############
try:
    with open("employees3333.txt","r") as fobj:
        for line in fobj:
            print(line.strip())
except TypeError as err:
    print("Invalid opertion :",err)
except ValueError as err:
    print("Invalid input:",err)
except (IndexError,ValueError,KeyError) as err:
    print("Invalid index or key:",err)
except Exception as err:
    print("Unknown exception :",err)








    
