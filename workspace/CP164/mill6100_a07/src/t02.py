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

values = [1,2,3,4]
other_values = [5,6,7,8]

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
for val in values:
    source2.insert(val)
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nSource2 Empty")
source1 = Priority_Queue()
source2 = Priority_Queue()
target = Priority_Queue()
for val in values:
    source1.insert(val)
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nBoth PQ's non-empty")
source1 = Priority_Queue()
source2 = Priority_Queue()
target = Priority_Queue()
for val in values:
    source1.insert(val)
for val in other_values:
    source2.insert(val)
print("Source1 Contents: {}".format([val for val in source1]))
print("Source2 Contents: {}".format([val for val in source2]))
target.combine(source1, source2)
print("Target Contents: {}".format([val for val in target]))
print("Expected: {}".format([1,5,2,6,3,7,4,8]))

print("\n\nTesting PQ#insert")

print("\nEmpty initial PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
value = 5
print("Value to insert: {}".format(value))
pq.insert(value)
print("Inserted")
print("New PQ Contents: {}".format([val for val in pq]))
print("Expected: {}".format([5]))

print("\nNon-empty initial PQ")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
value = 6
print("Value to insert: {}".format(value))
pq.insert(value)
print("Inserted")
print("New PQ Contents: {}".format([val for val in pq]))
print("Expected: {}".format([1,2,3,4,6]))

print("\n\nTesting PQ#is_empty")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
empty = pq.is_empty()
print("PQ empty? Got: {}".format(empty))
print("Expected: {}".format(True))

print("\nNon-empty PQ")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
empty = pq.is_empty()
print("PQ empty? Got: {}".format(empty))
print("Expected: {}".format(False))

print("\n\nTesting PQ#__len__")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
pq_len = len(pq)
print("Length of PQ: {}".format(pq_len))
print("Expected: {}".format(0))

print("\nPQ with ONE element")
pq = Priority_Queue()
pq.insert(0)
print("PQ Contents: {}".format([val for val in pq]))
pq_len = len(pq)
print("Length of PQ: {}".format(pq_len))
print("Expected: {}".format(1))

print("\nPQ with MORE THAN ONE element")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
pq_len = len(pq)
print("Length of PQ: {}".format(pq_len))
print("Expected: {}".format(len(values)))

print("\n\nTesting PQ#peek")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
try:
    front_value = pq.peek()
except AssertionError:
    print("Unable to peek empty PQ. Assertion thrown correctly")
    
print("\nPQ with ONE element")
pq = Priority_Queue()
value = 3
pq.insert(value)
print("PQ Contents: {}".format([val for val in pq]))
front_value = pq.peek()
print("Front value returned: {}".format(front_value))
print("Expected: {}".format(value))

print("\nPQ with MORE THAN ONE element")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
value = 0
pq.insert(value)
print("PQ Contents: {}".format([val for val in pq]))
front_value = pq.peek()
print("Front value returned: {}".format(front_value))
print("Expected: {}".format(value))

print("\n\nTesting PQ#remove")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
try:
    removed_val = pq.remove()
except AssertionError:
    print("Unable to remove from an empty PQ. Assertion thrown correctly")

print("\nPQ with ONE element")
pq = Priority_Queue()
value = 3
pq.insert(value)
print("PQ Contents: {}".format([val for val in pq]))
removed_val = pq.remove()
print("Removed value: {}".format(removed_val))
print("Expected: {}".format(value))

print("\nPQ with MORE THAN ONE element")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
removed_val = pq.remove()
print("Removed value: {}".format(removed_val))
print("Expected: {}".format(values[0]))

print("\n\nTesting PQ#split_alt")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
target1, target2 = pq.split_alt()
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))

print("\nPQ with ONE element")
pq = Priority_Queue()
pq.insert(4)
print("PQ Contents: {}".format([val for val in pq]))
target1, target2 = pq.split_alt()
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([4]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))
print("Original PQ Contents: {}".format([val for val in pq]))

print("\nPQ with MORE THAN ONE element")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
target1, target2 = pq.split_alt()
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([1,3]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([2,4]))
print("Original PQ Contents: {}".format([val for val in pq]))

print("\n\nTesting PQ#split_key")

print("\nEmpty PQ")
pq = Priority_Queue()
print("PQ Contents: {}".format([val for val in pq]))
key = 1
print("Key to split on: {}".format(key))
target1, target2 = pq.split_key(key)
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))
print("Original PQ Contents: {}".format([val for val in pq]))

print("\nPQ with ONE element, key priority equal")
pq = Priority_Queue()
pq.insert(1)
print("PQ Contents: {}".format([val for val in pq]))
key = 1
print("Key to split on: {}".format(key))
target1, target2 = pq.split_key(key)
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([1]))
print("Original PQ Contents: {}".format([val for val in pq]))

print("\nPQ with ONE element, key priority lower")
pq = Priority_Queue()
pq.insert(2)
print("PQ Contents: {}".format([val for val in pq]))
key = 1
print("Key to split on: {}".format(key))
target1, target2 = pq.split_key(key)
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([2]))
print("Original PQ Contents: {}".format([val for val in pq]))

print("\nPQ with MORE THAN ONE element")
pq = Priority_Queue()
for val in values:
    pq.insert(val)
print("PQ Contents: {}".format([val for val in pq]))
key = 3
print("Key to split on: {}".format(key))
target1, target2 = pq.split_key(key)
print("Target1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([1,2]))
print("Target2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([3,4]))
print("Original PQ Contents: {}".format([val for val in pq]))
