"""
------------------------------------------------------------------------
Lab 6, Task 5 - Peek and Remove Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-25
------------------------------------------------------------------------
"""
from List_linked import List

ll = List()
values = [11,22,33,44,55,66]
for i in values:
    ll.append(i)

val = ll.remove(77)

contents = []
for i in ll:
    contents.append(i)
print("Remove {}, remaining list: {}".format(val, contents))