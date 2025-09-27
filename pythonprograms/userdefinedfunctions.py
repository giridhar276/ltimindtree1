# fixed arguments
print("**** fixed arguments *****")
def display(a,b):
    print(a,b)
    
display(10,20)

# default arguments
print("***** default arguments *******")
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display()         # 0 0 0
display(10)       # 10 0 0 
display(10,20)    # 10 20 0
display(10,20,30) # 10 20 30

# keyword arguments
print("****** keyword arguments ******")
def display(b,a,c):
    print(a,b,c)
display(c = 30,a=10,b =20)

# variable length arguments
# if any object begins with * .. it is treated as tuple
def display(*data):
    #print(data)
    for value in data:
        print(value)
    
display(10,20,30,40,50,45,23,12,56,876,43,56,43,56,43,43,"unix")


#### **kwargs is a dictionary 
def displayinfo(**kwargs):
    for k,v in kwargs.items():
        print("key :", k )
        print("value:", v)



displayinfo(chap1 = 10 , chap2 = 20)










