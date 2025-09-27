## write a program to display all the lines that starts with python


with open("languages.txt") as fobj:
    for line in fobj:
        line = line.strip()
        if line.startswith("python"):
            print(line)


### using regular expressions
print("**** using re ******")
import re
with open("languages.txt") as fobj:
    for line in fobj:
        line = line.strip()
        if re.match("python",line):
            print(line)


#re.match(substring,string) : will match at the beginning of the line
#re.search(substring,string) : will search anything in the string
#re.sub(old,new,string)     : will replace old with new

name = "I love python programming"
if re.search("python",name):
    print("substring found in the string")

if re.match("python", name):
    print("substrin found at the beginning of the string")
else:
    print("substring not found at the beginning of the string")


output = re.sub("python","java",name)
print(output)   












