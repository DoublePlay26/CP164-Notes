"""
------------------------------------------------------------------------
Lab 6, Task 1 - Append, Prepend, Insert Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-25
------------------------------------------------------------------------
"""
from List_linked import List

ll = List()
vals = [1,2,3,4]
for val in vals:
    ll.append(val)

print("Testing Append")    
check = []
for node_val in ll:
    check.append(node_val)

print("List contents: {}".format(check))
print("Expected: {}".format(vals))

print("\nTesting Prepend")
check = []
to_prepend = 0
ll.prepend(to_prepend)

for val in ll:
    check.append(val)

print("List contents: {}".format(check))
print("Expected: {}".format([0,1,2,3,4]))

print("\nTesting Insert")
print("Positive index within range")
check = []
to_insert = 6
ll.insert(2, to_insert)

for val in ll:
    check.append(val)
    
print("List contents: {}".format(check))
print("Expected: {}".format([0,1,6,2,3,4]))

print("Negative index within range")
check = []
to_insert = 6
ll.insert(-1, to_insert)

for val in ll:
    check.append(val)
    
print("List contents: {}".format(check))
print("Expected: {}".format([0,1,2,3,4]))
    
