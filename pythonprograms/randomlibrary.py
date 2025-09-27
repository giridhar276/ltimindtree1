


import random

# dislay random decimal value between 0 to 1
print(random.random())

# display random value betwen the range
print(random.randint(1,100))
print(random.randint(1000,9999))

# shuffling the values
alist = list(range(1,15))
print("Before shuffling:", alist)
random.shuffle(alist)
print("After shuffling :", alist)
random.shuffle(alist)
print("After shuffling :", alist)

# display random value betwen the range
print(random.randrange(1,40))
