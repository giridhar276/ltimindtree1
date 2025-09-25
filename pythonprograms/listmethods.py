alist = [10,45,23,67,26,42,45,10,10,10,10,10]

alist[3] = 650  # replacing value

# slicing
print(alist[0] )
print(alist[0:4])
print(alist[::-1])

## list methods
#list.append(singlevalue)
alist.append(94)
print("After appending :", alist)

#list.extend(iterable)
alist.extend([85,28,3])
print("After extending :", alist)

#alist.insert(where,what)    # list.insert(index,value)
alist.insert(1,49)
print("After inserting :",alist)

#list.pop(index)
alist.pop(10)   # 1 is the index # value at index 1 is removed
print("After pop operation :",alist)

# list.remove(value)
if 100 in alist:
    alist.remove(100)
    print("After remove :", alist)
else:
    print("value not in list")

# reverse list values
alist.reverse()
print("After reversing :", alist)

# sorting values
alist.sort()
print("After sorting in ascending:", alist)
alist.sort(reverse= True)
print("After sorting in descending:", alist)

# list.count(value) --> will display no. of occurences of that value
print("count of 10 :", alist.count(10))




for val in alist:
    print(val)


length = len(alist)
for val in range(0,length):   # range(0,10)
    print(alist[val])



alist = [10,20,30,40]
rev = []
for val in alist:
    rev = [ val] + rev
print(rev)


# task 9
words = ["python","unix","java","oracle"]

output = []
for item in words:
    if len(item) > 4:
        output.append(item)


# task 10 : converting list to string
words = ["I","love","python","programming"]
line = " ".join(words)
print(line)



















    






    









