"""
------------------------------------------------------------------------
Lab 5, Task 2 - GCD
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-11
------------------------------------------------------------------------
"""
from functions import gcd
from random import randint

m = randint(0, 20000)
n = randint(-20000, 20000)

ans = gcd(m, n)
print("m: {}\tn: {}\tans: {}".format(m, n, ans))