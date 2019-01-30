"""
------------------------------------------------------------------------
Lab 2, Task 2 - utilities#array_to_stack
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from utilities import array_to_stack
from Stack_array import Stack

array = [0, 1, 2, 3, 4]
s = Stack()

print("Array: {}".format(array))

array_to_stack(s, array)

print("Values: {}".format(s._values))
print("Stack to Array: ")
for elem in s:
    print(elem, end=' ')
print()
print("Array: {}".format(array))

print("Top: {}".format(s.peek()))
