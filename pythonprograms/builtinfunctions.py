## methods are different are functions are diferent
## every object has methods Eg:  name.upper()  alist.append()
## functions are common for all the objects  
name = "python"
print(10,20,30)
aname = input("Enter any name :")
print(list(range(1,5)))
alist = [10,20,30,40]
print(max(alist))  # display the largest number in the list
print(min(alist))  #  # display the smallest number in the list
print(sum(alist))   # display the sum of the values
print(len(alist))   # get the length of the list
print(len(name))
val = 10.3
print(round(val)) # round the value to numeric
print(type(val))  # will display type of the object
print(isinstance(name,str))  # if name is str.. it returns True
print(isinstance(name,list))

if isinstance(name,str)):
    print("its a string")

# typecasting functions - converting from one object to another function
val = 10
print(float(val))
print(oct(val))
print(hex(val))

alist =[10,20,30]
print(tuple(alist))
print(set(alist))
print(list(alist))

name = "python"
print(list(name))
print(tuple(name))
















# identity(object)  - will return the unique reference of the object
val = 10
print(id(val))
alist = [10,20,30]
print(id(alist))
book = {"chap1":10}
print(id(book))
