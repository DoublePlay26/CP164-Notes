"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-13
------------------------------------------------------------------------
"""
from Stack_array import Stack

vals = [1,2,3,4]
s = Stack()
for val in vals:
    s.push(val)

for i in s:
    print(i, end=',')
print()
s.reverse()
for i in s:
    print(i, end=',')
print()
s.reverse() #1,2,3,4
target1, target2 = s.split_alt()
for i in target1:
    print(i, end=',')
print()
for i in target2:
    print(i, end=',')
print()