"""
------------------------------------------------------------------------
Assignment 7, Task 1 - Linked_Queue Implementation
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from Queue_linked import Queue

print("Testing Queue#combine")

print("\nEmpty Queues")
source1 = Queue()
source2 = Queue()
target = Queue()
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Combined Queues")
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nSource1 empty")
source1 = Queue()
source2 = Queue()
values = [1,2,3,4]
for val in values:
    source2.insert(val)
target = Queue()
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Combined Queues")
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([1,2,3,4]))

print("\nSource2 empty")
source1 = Queue()
source2 = Queue()
values = [1,2,3,4]
for val in values:
    source1.insert(val)
target = Queue()
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Combined Queues")
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([1,2,3,4]))

print("\nBoth Queues non-empty")
source1 = Queue()
source2 = Queue()
values = [1,2,3,4]
values_others = [5,6,7,8]
for val in values:
    source1.insert(val)
for val in values_others:
    source2.insert(val)
target = Queue()
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Combined Queues")
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([1,5,2,6,3,7,4,8]))
