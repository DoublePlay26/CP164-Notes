"""
------------------------------------------------------------------------
Lab 7, Task 4 - List#intersection_r
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-04
------------------------------------------------------------------------
"""
from List_linked import List

my_list = List()
values = [1,2,3,4]
other = List()
other_vals = [1]

for val in values:
    my_list.append(val)
for val in other_vals:
    other.append(val)
    
my_list.intersection(my_list, other)

contents = []
for val in my_list:
    contents.append(val)

print("Contents: {}".format(contents))