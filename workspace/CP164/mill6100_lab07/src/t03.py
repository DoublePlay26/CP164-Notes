"""
------------------------------------------------------------------------
Lab 7, Task 3 - List#split_alt_r
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-04
------------------------------------------------------------------------
"""
from List_linked import List

my_list = List()
values = [11,22,33,44,55,66]
for val in values:
    my_list.append(val)
even, odd = my_list.split_alt_r()

e_contents = []
for node in even:
    e_contents.append(node)
o_contents = []
for node in odd:
    o_contents.append(node)
    
print("Even: {}".format(e_contents))
print("Odd: {}".format(o_contents))

my_list = List()
values = [99]
for val in values:
    my_list.append(val)
even, odd = my_list.split_alt_r()

e_contents = []
for node in even:
    e_contents.append(node)
o_contents = []
for node in odd:
    o_contents.append(node)
    
print("Even: {}\tRear: {}".format(e_contents, even._rear))
print("Odd: {}".format(o_contents))
