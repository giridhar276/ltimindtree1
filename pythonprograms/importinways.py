


# method 1 : all the methods are imported to your program

import math
print(math.log(2))
print(math.tan(1))
print(math.floor(45.3))

# method 2:  importing with alias name

import math as m
print(m.sin(1))
print(m.ceil(34.3))
print(m.log(2))


# method3 : importing required methods only

from math import log,tan  # only log and tan are imported
print(log(1))
print(tan(2))
