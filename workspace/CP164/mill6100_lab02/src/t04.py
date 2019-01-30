"""
------------------------------------------------------------------------
Lab 2, Task 4 - utilities#stack_test
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from utilities import stack_test
from Stack_array import Stack
from random import randint

source1 = []
source2 = [1]
source3 = [0,1,2,3,4]
source4 = []
for i in range(5):
    source4.append(randint(0,5))

print("Test 1: List: {}".format(source1))
stack_test(source1)
print("\nTest 2: List: {}".format(source2))
stack_test(source2)
print("\nTest 3: List: {}".format(source3))
stack_test(source3)
print("\nTest 4: List: {}".format(source4))
stack_test(source4)