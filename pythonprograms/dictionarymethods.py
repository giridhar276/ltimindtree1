# dictionary
book = {"chap1":10 ,"chap2": 20 ,"chap3":30 ,"chap1":100 }

print(book["chap1"])
#print(book["chap21"])
# returns None if key is not found
# if key is found.. will return the value
print(book.get("chap2")) 
                          


# add new key-value to dictionary
book["chap4"] = 40
book["chap5"] = 50
print(book)

# display individual value
print(book["chap1"]) # 100
print(book["chap5"]) # 50

# display keys
print(book.keys())

# display key line by line
for key in book.keys():
    print(key)


book = {"chap1":10 ,"chap2": 20 ,"chap3":30 ,"chap1":100 }
for key in book:
    print(key)


    
####################################
# display values
print(book.values())

for value in book.values():
    print(value)
#####################################
# display key and value at a time
print(book.items())    #[(key,value) , ( key,value) , ( key,value) ]

for key,value in book.items():
    print("key:", key)
    print("value :",value)

#######################################
#dict.pop(key)  - key and its corresponding value will be removed
book.pop("chap1")
print("After pop operation :", book)
book.pop("chap2")
print("After pop operation :", book)

########################################
# book.popitem() --- will remove last inserted key-value
book.popitem()
print("After popitem operation :", book)
book.popitem()
print("After popitem operation :", book)

############ combining dictionaries ###############
book = {"chap1":10 ,"chap2":20}
newbook = {"chap3":30 ,"chap4":40 }
# method1
finalbook = { **book , **newbook}
print(finalbook)

#method2
book.update(newbook)   # book is getting updated
print(book)





























    













