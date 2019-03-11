"""
------------------------------------------------------------------------
Assignment 7, Task 2 - Priority_Queue_linked Implementation
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from Priority_Queue_linked import Priority_Queue

print("Testing PQ#combine")

print("\nEmpty Queues")
source1 = Priority_Queue()
source2 = Priority_Queue()
target = Priority_Queue()
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nSource1 Empty")
source1 = Priority_Queue()
source2 = Priority_Queue()
target = Priority_Queue()
values = [1,2,3,4]
for val in values:
    source2.insert(val)
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([]))