#import module_use as m  ### alias
from module_use import *
import math


#print(m.squire(31))   ### module alias
print(sum(20))
print(squire(5))
print(multi(10,20))

### math module functions
x=11.2
print(math.ceil(x))

y = -12
print(math.fabs(y))

print(math.factorial(5))
print(math.floor(x))

print(math.fsum([10,20,30,40]))
print(math.sqrt(64))