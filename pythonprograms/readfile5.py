############################# using csv library #####################
###################### every line is displayed in list ###############
import csv
workset = set()
with open("employees.txt") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        workset.add(workclass)
    # displaying output
    for work in workset:
        print(work)
################################ reading line by line ###############
workset = set()
with open("employees.txt") as fobj:
    header = fobj.readline()
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        workclass = output[1]
        workset.add(workclass)
    for work in workset:
        print(work)
        

############################# using dictionary
workdict = dict()
with open("employees.txt") as fobj:
    header = fobj.readline()
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        workclass = output[1]
        workdict[workclass] = 0  # generating dict{"private":1 ,"public":1 }
    for work in workdict:
        print(work)






        







    
        
