name = "python programming"
# slicing
# string[start:stop:step]
print(name[0])
print(name[0:4])
print(name[0:4:1])
print(name[8:15])
print(name[0:18])
print(name[:])
print(name[::])
print(name[::2])
print(name[0::3])
print(name[-1])
print(name[-2])
print(name[-5:-1])
print(name[::-1])



name = "python programming"
# first char to upper
print(name.capitalize())
print(name.title())
# validating whether the string is upper or not
print(name.isupper())
# convert to upper
print(name.upper())
# validating whehter the stiring is lower or not
print(name.islower())
## convert to lower
print(name.lower())
# check whether string is alpha or not
print(name.isalpha())
# check for alphanumerical
print(name.isalnum())
# replace python with java
print(name.replace("python","java"))
# display string is ceneter of 40
print(name.center(40))
print(name.center(40,"*"))

# split the string to list based on delimeter
print(name.split(" "))
# remove whitespaces
aname = " python  "
print(len(aname))
print(len(aname.strip()))  # remove whitespaces at both the ends
print(len(aname.lstrip())) # only at left side
print(len(aname.rstrip())) # only at right side

# check for substring
print(name.find("ram"))   # check for ra in "python programming"
                         # ra is found .. it returns the index of r
                         # ra is not found.. it returns -1
                

name = "I love {} and {}" # template
print(name.format("Hyd","delhi"))   # I love Hyd and Delhi
print(name.format("python","java")) # I love python and java


print(name.islower())
# simple if 
if  name.islower():
    print("string is lower")
    print("inside if")
    print("still inside if")


# if-else
if name.islower():
    print("string is lower")
else:
    print("String is lower")


# if-elif-elif-elif-elif-elif-else
lang = input("Enter any language :")
if lang == "python":
    print("I am learning python")
elif lang == "unix":
    print("I love unix")
elif lang == "python":
    print("I love python")
else:
    print("I am  learning genai")



# range(start,stop,step)
for val in range(1,11):
    print(val)


for val in range(10,0,-1):
    print(val)

name = "python"
for char in name:
    print(char)

# substring is existing or not
name = "python"
if "ho" in name:
    print("substring found")
else:
    print("not found")

# using find
if name.find("ho") != -1 :
    print("substring found")
else:
    print("not found")


# concat string with number
print("python" + str(9))

print("python" + " " + "programming")

# * is the repetition operator
name = "python"
print(name * 3) #pythonpythonpython






























    
















    



    





















    





































































