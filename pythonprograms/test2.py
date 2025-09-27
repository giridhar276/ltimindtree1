import csv

try:
    with open("employeesss.txt","r")as fobj:
     reader = csv.reader(fobj)
     for line in reader:
         print(line)
except TypeError as err:
    print("Invalid output ",err)
except IndexError as err:
    print("Index Error ",err)
except KeyError as err:
    print("Index Error ",err)
except ValueError as err:
    print("Value Error ",err)
    
    
     
