

'''
write a progarm to count character frequencies:


Enter a string :  hello

h : 1 time
e : 1 time
l : 2 times
o : 1 time
'''

name = input("Enter a string :")
strset = set(name)
for char in strset:
    print(char, name.count(char),"time")

