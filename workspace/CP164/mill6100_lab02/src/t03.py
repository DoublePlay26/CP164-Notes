"""
------------------------------------------------------------------------
Lab 2, Task 3 - utilities#stack_to_array
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from utilities import stack_to_array
from Stack_array import Stack

target = []
array = [1,2,3,4]

s = Stack()

for i in array:
    s.push(i)
    
print("Array before: {}".format(target))
print("Stack before:")
for i in s:
    print(i, end=' ')
print()
stack_to_array(s, target)

print("Array after: {}".format(target))
print("Stack After:")
for i in s:
    print(i, end=' ')
