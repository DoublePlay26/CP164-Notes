"""
------------------------------------------------------------------------
Assignment 8, Task 3 - Deque_linked Implementation
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-11
------------------------------------------------------------------------
"""
from Deque_linked import Deque

values = [1,2,3,4]
other_values = [5,6,7,8]

print("Testing Deque#insert_front")

print("\nEmpty intial Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
to_insert = 3
print("Inserting {} at front".format(to_insert))
d.insert_front(to_insert)
print("Inserted")
print("Deque Contents: {}".format([val for val in d]))
print("Expected: {}".format([3]))

print("\nNon-empty intial Deque")
d = Deque()
for val in values:
    d.insert_front(val)
print("Deque Contents: {}".format([val for val in d]))
to_insert = 3
print("Inserting {} at front".format(to_insert))
d.insert_front(to_insert)
print("Inserted")
print("Deque Contents: {}".format([val for val in d]))
expected = [val for val in values]
expected.append(to_insert)
expected = expected[::-1]
print("Expected: {}".format(expected))

print("\n\nTesting Deque#insert_rear")

print("\nEmpty Initial Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
to_insert = 3
print("Inserting {} at rear".format(to_insert))
d.insert_rear(to_insert)
print("Inserted")
print("Deque Contents: {}".format([val for val in d]))
print("Expected: {}".format([3]))

print("\nNon-empty intial Deque")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
to_insert = 3
print("Inserting {} at rear".format(to_insert))
d.insert_rear(to_insert)
print("Inserted")
print("Deque Contents: {}".format([val for val in d]))
expected = [val for val in values]
expected.append(to_insert)
print("Expected: {}".format(expected))

print("\n\nTesting Deque#is_empty")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
empty = d.is_empty()
print("Empty? {}".format(empty))
print("Expecting: {}".format(True))

print("\nNon-empty Deque")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
empty = d.is_empty()
print("Empty? {}".format(empty))
print("Expecting: {}".format(False))

print("\n\nTesting Deque#__len__")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
length = len(d)
print("Returned length of Deque: {}".format(length))
print("Expected: {}".format(0))

print("\nNon-empty Deque with ONE element")
d = Deque()
d.insert_front(5)
print("Deque Contents: {}".format([val for val in d]))
length = len(d)
print("Returned length of Deque: {}".format(length))
print("Expected: {}".format(1))

print("\nNon-empty Deque with MORE THAN ONE element")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
length = len(d)
print("Returned length of Deque: {}".format(length))
print("Expected: {}".format(len(values)))

print("\n\nTesting Deque#peek_front")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
try:
    value = d.peek_front()
except AssertionError:
    print("Cannot peek front of empty Deque. Assertion thrown successfully.")

print("\nNon-empty Deque")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
value = d.peek_front()
print("Peeked front: {}".format(value))
print("Expected: {}".format(values[0]))

print("\n\nTesting Deque#peek_rear")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
try:
    value = d.peek_rear()
except AssertionError:
    print("Cannot peek rear of empty Deque. Assertion thrown successfully.")

print("\nNon-empty Deque")
d = Deque()
for val in values:
    d.insert_front(val)
print("Deque Contents: {}".format([val for val in d]))
value = d.peek_rear()
print("Peeked rear: {}".format(value))
print("Expected: {}".format(values[0]))

print("\n\nTesting Deque#remove_front")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
try:
    value = d.remove_front()
except AssertionError:
    print("Cannot remove front of empty Deque. Assertion thrown successfully.")

print("\nNon-empty Deque")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
value = d.remove_front()
print("Removed front: {}".format(value))
print("Expected: {}".format(values[0]))

print("\n\nTesting Deque#remove_rear")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
try:
    value = d.remove_rear()
except AssertionError:
    print("Cannot remove rear of empty Deque. Assertion thrown successfully.")

print("\nNon-empty Deque")
d = Deque()
for val in values:
    d.insert_front(val)
print("Deque Contents: {}".format([val for val in d]))
value = d.remove_rear()
print("Removed front: {}".format(value))
print("Expected: {}".format(values[0]))

print("\n\nTesting Deque#swap")

print("\nEmpty Deque")
d = Deque()
print("Deque Contents: {}".format([val for val in d]))
l = 0
r = 0
print("l: {}\tr: {}".format(l, r))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

print("\nDeque with ONE element")
d = Deque()
d.insert_front(values[0])
print("Deque Contents: {}".format([val for val in d]))
l = 0
r = 0
print("l: {}\tr: {}".format(l, r))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

print("\nDeque with MORE THAN ONE element")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
l_index = 0
l = d._front
r_index = -1
r = d._rear
print("l: {}\tr: {}".format(l_index, r_index))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

print("\nDeque with MORE THAN ONE element, l < r")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
l_index = -1
l = d._rear
r_index = 0
r = d._front
print("l: {}\tr: {}".format(l_index, r_index))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

print("\nDeque with MORE THAN ONE element, l and r not front or rear")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
l_index = 1
l = d._front._next
r_index = 2
r = d._rear._prev
print("l: {}\tr: {}".format(l_index, r_index))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

print("\nDeque with MORE THAN ONE element")
d = Deque()
for val in values:
    d.insert_rear(val)
print("Deque Contents: {}".format([val for val in d]))
l_index = 2
l = d._rear._prev
r_index = 1
r = d._front._next
print("l: {}\tr: {}".format(l_index, r_index))
d._swap(l, r)
print("Deque Contents: {}".format([val for val in d]))

