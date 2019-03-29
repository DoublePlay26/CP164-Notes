"""
------------------------------------------------------------------------
Assignment 9, Task 4 - node_counts, __contains__, parent (iterative), parent_r (recursive)
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-28
------------------------------------------------------------------------
"""
from BST_linked import BST

print('Testing BST#node_counts')

print('\n\nEmpty BST')
bst = BST()

zero, one, two = bst.node_counts()
print("Nodes w/ ZERO children: {}\tExpected: {}".format(zero, 0))
print("Nodes w/ ONE children: {}\t\tExpected: {}".format(one, 0))
print("Nodes w/ TWO children: {}\t\tExpected: {}".format(two, 0))

print('\n\nNon-empty BST with only two nodes')
bst = BST()
for val in [2,4]:
    bst.insert(val)
zero, one, two = bst.node_counts()
print("Nodes w/ ZERO children: {}\tExpected: {}".format(zero, 1))
print("Nodes w/ ONE child: {}\t\tExpected: {}".format(one, 1))
print("Nodes w/ TWO children: {}\t\tExpected: {}".format(two, 0))

print('\n\nNon-empty BALANCED BST with 3 nodes')
bst = BST()
for val in [2,4,1]:
    bst.insert(val)
zero, one, two = bst.node_counts()
print("Nodes w/ ZERO children: {}\tExpected: {}".format(zero, 2))
print("Nodes w/ ONE child: {}\t\tExpected: {}".format(one, 0))
print("Nodes w/ TWO children: {}\t\tExpected: {}".format(two, 1))

print('\n\nNon-empty UNBALANCED BST with 3 nodes')
bst = BST()
for val in [2,4,3]:
    bst.insert(val)
zero, one, two = bst.node_counts()
print("Nodes w/ ZERO children: {}\tExpected: {}".format(zero, 1))
print("Nodes w/ ONE child: {}\t\tExpected: {}".format(one, 2))
print("Nodes w/ TWO children: {}\t\tExpected: {}".format(two, 0))

print('\n\nTesting BST#__contains__')

print('\n\nEmpty BST')
bst = BST()
key = 6
key_in = key in bst
print("Key: {}".format(key))
print("Key in bst? {}\tExpected: {}".format(key_in, False))

print('\n\nNon-empty BST, key NOT in bst')
bst = BST()
for val in [4,3,5,8,7]:
    bst.insert(val)
key = 6
key_in = key in bst
print("Key: {}".format(key))
print("Key in bst? {}\tExpected: {}".format(key_in, False))

print('\n\nNon-empty BST, key IN bst')
bst = BST()
for val in [4,3,5,8,6]:
    bst.insert(val)
key = 6
key_in = key in bst
print("Key: {}".format(key))
print("Key in bst? {}\tExpected: {}".format(key_in, True))

print('\n\nTesting BST#parent (iterative)')

print('\n\nEmpty BST')
bst = BST()
try:
    parent = bst.parent(4)
except AssertionError:
    print("Cannot locate parent in an empty BST. Assertion thrown correctly.")

print('\n\nNon-empty BST, key NOT in bst')
bst = BST()
for val in [5,4,2,3,7,6,8]:
    bst.insert(val)
print("BST Contents: {}".format([val for val in bst]))
key = 9
print("Key: {}".format(key))
parent = bst.parent(key)
print("Parent of key: {}".format(parent))
print("Expected: {}".format(None))

print('\n\nNon-empty BST, key IN bst')
bst = BST()
for val in [5,4,2,3,7,6,8]:
    bst.insert(val)
print("BST Contents: {}".format([val for val in bst]))
key = 7
print("Key: {}".format(key))
parent = bst.parent(key)
print("Parent of key: {}".format(parent))
print("Expected: {}".format(5))

print('\n\nTesting BST#parent (recursive)')

print('\n\nEmpty BST')
bst = BST()
try:
    parent = bst.parent_r(4)
except AssertionError:
    print("Cannot locate parent in an empty BST. Assertion thrown correctly.")

print('\n\nNon-empty BST, key NOT in bst')
bst = BST()
for val in [5,4,2,3,7,6,8]:
    bst.insert(val)
print("BST Contents: {}".format([val for val in bst]))
key = 9
print("Key: {}".format(key))
parent = bst.parent_r(key)
print("Parent of key: {}".format(parent))
print("Expected: {}".format(None))

print('\n\nNon-empty BST, key IN bst')
bst = BST()
for val in [5,4,2,3,7,6,8]:
    bst.insert(val)
print("BST Contents: {}".format([val for val in bst]))
key = 7
print("Key: {}".format(key))
parent = bst.parent_r(key)
print("Parent of key: {}".format(parent))
print("Expected: {}".format(5))