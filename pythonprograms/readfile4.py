
import csv
with open("employees.txt","r") as fobj:
    # converting file object to csv obj
    reader = csv.reader(fobj)
    for line in reader:
        print(line)
    
