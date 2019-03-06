"""
------------------------------------------------------------------------
Lab 7 - Task 1: List#_linear_search_r
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
for val in values:
    my_list.append(val)
    
key = 5
p, c, i = my_list._linear_search_r(key)

print("Previous: {}".format(p._value if p is not None else p))
print("Current: {}".format(c._value if c is not None else c))
print("Index: {}".format(i))

print("Test with empty list")
my_list = List()
values = [99]
for val in values:
    my_list.append(val)
key = 99
p, c, i = my_list._linear_search_r(key)

print("Previous: {}".format(p._value if p is not None else p))
print("Current: {}".format(c._value if c is not None else c))
print("Index: {}".format(i))