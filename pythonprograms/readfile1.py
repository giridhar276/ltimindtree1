#1 reading the file line by line

with open("employees.txt","r") as fobj:
    for line in fobj:
        print(line.strip())
    
