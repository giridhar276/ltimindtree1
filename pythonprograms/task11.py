'''
Write a program to join corresponding strings from two lists.
first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]
Output:
Good Morning
Data Science
Machine Learning
''' 
# method1
first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]
for val in range(0,len(first)):
    output = first[val] + " " + second[val]
    print(output)

# method2
first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]

for item in zip(first,second):
    print(item[0] + " " + item[1])
