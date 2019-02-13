"""
------------------------------------------------------------------------
Lab 5, Task 1 - Recurse
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-11
------------------------------------------------------------------------
"""
from random import randint
from functions import recurse

x = randint(0, 5)
y = randint(0, 5)

print("x: {}\ty {}".format(x, y))
ans = recurse(x, y)
print(ans)

x = randint(0,3)
y = randint(0,3)

print("x: {}\ty {}".format(x, y))
ans = recurse(x, y)
print(ans)