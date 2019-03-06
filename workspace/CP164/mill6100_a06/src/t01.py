"""
------------------------------------------------------------------------
Assignment 6, Task 1 - is_identical, remove_many, __getitem__, clean,
intersection, union, prepend, append, remove_front, combine, split, split_alt
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-06
------------------------------------------------------------------------
"""
from List_linked import List

print("Testing List#is_identical")
print("\nSame values")
my_list = List()
other_list = List()
values = [1,2,3,4]
for val in values:
    my_list.append(val)
    other_list.append(val)
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format(values))
print("List 2 contents: {}".format(values))
print("Identical? {}\tExpected: {}".format(identical, True))

print("\nDifferent values")
my_list = List()
other_list = List()
values = [1,2,3,4]
for val in values:
    my_list.append(val)
for val in values[:-1]:
    other_list.append(val)
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format(values))
print("List 2 contents: {}".format(values[:-1]))
print("Identical? {}\tExpected: {}".format(identical, False))

print("\nEmpty lists")
my_list = List()
other_list = List()
values = []
for val in values:
    my_list.append(val)
    other_list.append(val)
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format(values))
print("List 2 contents: {}".format(values))
print("Identical? {}\tExpected: {}".format(identical, True))

print("Testing List#remove_many")
print("\nEmpty list")
my_list = List()
values = []
for val in values:
    my_list.append(val)
to_remove = 2
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
contents = []
for val in my_list:
    contents.append(val)
    
print("List contents after remove: {}".format(contents))
print("Expected: {}".format([]))

print("\nMissing key")
my_list = List()
values = [1,2,3,4]
for val in values:
    my_list.append(val)
to_remove = 5
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
contents = []
for val in my_list:
    contents.append(val)
    
print("List contents after remove: {}".format(contents))
print("Expected: {}".format([1,2,3,4]))

print("\nList only contains the key")
my_list = List()
values = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
for val in values:
    my_list.append(val)
print("Initial contents: {}".format(values))
to_remove = 2
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
contents = []
for val in my_list:
    contents.append(val)
print("Front: {}\tRear: {}".format(my_list._front, my_list._rear))
print("List contents after remove: {}".format(contents))
print("Expected: {}".format([]))

print("Testing List#__getitem__")

print("\nEmpty list")
my_list = List()
try:
    item = my_list[0]
except AssertionError:
    print("Invalid index. Assertion thrown correctly")
    
print("\nList of values")
values = [1,2,3,4]
for val in values:
    my_list.append(val)

item = my_list[0]
print("Item returned from my_list[0]: {}".format(item))
print("Expected: {}".format(values[0]))

print("Testing List#clean")

print("\nEmpty list")
my_list = List()
my_list.clean()
print("Cleaned list")
contents = []
for val in my_list:
    contents.append(val)
print("Contents after clean: {}".format(contents))
print("Expected: {}".format([]))

print("\nNo duplicates")
my_list = List()
values = [1,2,3,4]
for val in values:
    my_list.append(val)
print("Initial contents: {}".format(values))
my_list.clean()
print("Cleaned list")
contents = []
for val in my_list:
    contents.append(val)
print("Contents after clean: {}".format(contents))
print("Expected: {}".format(values))