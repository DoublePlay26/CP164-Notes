"""
------------------------------------------------------------------------
Lab 7, Task 2 - List#is_identical_r
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-04
------------------------------------------------------------------------
"""
from List_linked import List

my_list = List()
other = List()
values = [1,2,3,4]
for val in values:
    my_list.append(val)
for val in values:
    other.append(val)
    
identical = my_list.is_identical_r(other)

print("List 1 contents: {}".format(values))
print("List 2 contents: {}".format(values))
print("Identical? {}".format(identical))