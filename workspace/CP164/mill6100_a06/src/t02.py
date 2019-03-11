"""
------------------------------------------------------------------------
Assignment 6, Task 2 - SortedList methods
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-08
------------------------------------------------------------------------
"""
from Sorted_List_linked import Sorted_List
from Movie_utilities import read_movies
from Movie import Movie

fh = open('movies.txt', 'r')
movies = read_movies(fh)
movies_mid = len(movies) // 2


print("\n\nTesting Sorted_List#insert")

print("\nEmpty list")
my_list = Sorted_List()
print("Initial SL contents: {}".format([val for val in my_list]))
to_insert = Movie("Dellamorte Dellamore", 1994, None, None, None)
my_list.insert(to_insert)
print("Inserted {}".format(to_insert))
print("SL Contents: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[0]))

print("\nNon-empty list")
my_list = Sorted_List()
my_list.insert(movies[-1])
print("Initial SL contents: {}".format([val for val in my_list]))
to_insert = Movie("Dellamorte Dellamore", 1994, None, None, None)
my_list.insert(to_insert)
print("Inserted {}".format(to_insert))
print("SL Contents: {}".format([val for val in my_list]))
expected = [movies[-1]]
expected.insert(0, movies[0])
print("Expected: {}".format(expected))

print("\n\nNOT TESTING Sorted_List#_linear_search. Used in remove, find, intersection, \
union, __contains__, index.")

print("\n\nTesting Sorted_List#remove")

print("\nEmpty list")
my_list = Sorted_List()
print("Initial Contents: {}".format([val for val in my_list]))
to_remove = movies[0]
print("Value to remove: {}".format(to_remove))
value = my_list.remove(to_remove)
print("Removed value: {}".format(value))
print("Remaining list: {}".format([val for val in my_list]))
print("Expected: {}".format([val for val in my_list]))

print("\nNon-empty list, remove from front")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("Initial Contents: {}".format([val for val in my_list]))
to_remove = movies[0]
print("Value to remove: {}".format(to_remove))
value = my_list.remove(to_remove)
print("Removed value: {}".format(value))
print("Remaining list: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[1:]))

print("\nNon-empty list, remove from rear")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("Initial Contents: {}".format([val for val in my_list]))
to_remove = movies[-1]
print("Value to remove: {}".format(to_remove))
value = my_list.remove(to_remove)
print("Removed value: {}".format(value))
print("Remaining list: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[:-1]))

print("\nNon-empty list, remove from middle somewhere")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("Initial Contents: {}".format([val for val in my_list]))
to_remove = movies[4]
print("Value to remove: {}".format(to_remove))
value = my_list.remove(to_remove)
print("Removed value: {}".format(value))
print("Remaining list: {}".format([val for val in my_list]))
expected = []
for val in movies[:4]:
    expected.append(val)
for val in movies[5:]:
    expected.append(val)
print("Expected: {}".format(expected))

print("\n\nTesting Sorted_List#remove_front")

print("\nEmpty list")
my_list = Sorted_List()
print("Initial contents: {}".format([val for val in my_list]))
try:
    value = my_list.remove_front()
except AssertionError:
    print("Cannot remove front of empty list. Assertion thrown successfully.")
print("List contents after remove: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("Initial contents: {}".format([val for val in my_list]))
value = my_list.remove_front()
print("Value removed: {}".format(value))
print("List contents after remove: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[1:]))

print("\n\nTesting Sorted_List#index")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
to_find = movies[0]
print("Finding index of {}".format(to_find))
index = my_list.index(to_find)
print("Index returned: {}".format(index))

print("\nNon-empty list")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
to_find = movies[5]
print("Finding index of {}".format(to_find))
index = my_list.index(to_find)
print("Index returned: {}".format(index))
expected = 5
print("Expected: {}".format(expected))

print("\n\nTesting Sorted_List#find")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
to_find = movies[3]
print("Finding {}".format(to_find))
value = my_list.find(to_find)
print("Value returned: {}".format(value))

print("\nNon-empty list, front")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
to_find = movies[0]
print("Finding {}".format(to_find))
value = my_list.find(to_find)
print("Value returned: {}".format(value))

print("\nNon-empty list, rear")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
to_find = movies[-1]
print("Finding {}".format(to_find))
value = my_list.find(to_find)
print("Value returned: {}".format(value))

print("\nNon-empty list, somewhere in the middle")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
to_find = movies[movies_mid]
print("Finding {}".format(to_find))
value = my_list.find(to_find)
print("Value returned: {}".format(value))

print("\n\nTesting Sorted_List#peek")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
try:
    value = my_list.peek()
except AssertionError:
    print("Cannot peek at empty list. Assertion thrown successfully.")

print("\nNon-Empty List")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
value = my_list.peek()
print("Value peeked: {}".format(value))
print("Expected: {}".format(my_list[0]))

print("\n\nTesting Sorted_List#count")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
to_count = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("To count: {}".format(to_count))
count = my_list.count(to_count)
print("Counted: {}".format(count))
expected = 5
print("Expected: {}".format(expected))

print("\nNon-Empty list without key")
my_list = Sorted_List()
for val in movies[1:]:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
to_count = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("To count: {}".format(to_count))
count = my_list.count(to_count)
print("Counted: {}".format(count))
expected = 0
print("Expected: {}".format(expected))

print("\nNon-empty list with key")
my_list = Sorted_List()
for i in range(5):
    my_list.insert(movies[0])
print("List contents: {}".format([val for val in my_list]))
to_count = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("To count: {}".format(to_count))
count = my_list.count(to_count)
print("Counted: {}".format(count))
expected = 5
print("Expected: {}".format(expected))

print("\n\nTesting Sorted_List#min")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
try:
    min_ = my_list.min()
except AssertionError:
    print("Cannot find the min of an empty list. Assertion thrown successfully.")

print("\nNon-empty list")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
min_ = my_list.min()
print("Returned min: {}".format(min_))
print("Expected: {}".format(my_list[0]))

print("\nNon-empty list with multiple of same min")
my_list = Sorted_List()
for i in range(5):
    my_list.insert(movies[0])
print("List contents: {}".format([val for val in my_list]))
min_ = my_list.min()
print("Returned min: {}".format(min_))
print("Expected: {}".format(my_list[0]))

print("\n\nTesting Sorted_List#max")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
try:
    max_ = my_list.max()
except AssertionError:
    print("Cannot find the max of an empty list. Assertion thrown successfully.")

print("\nNon-empty list")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
max_ = my_list.max()
print("Returned max: {}".format(max_))
print("Expected: {}".format(my_list[-1]))

print("\nNon-empty list with multiple of same min")
my_list = Sorted_List()
for i in range(5):
    my_list.insert(movies[0])
print("List contents: {}".format([val for val in my_list]))
max_ = my_list.max()
print("Returned max: {}".format(max_))
print("Expected: {}".format(my_list[-1]))

print("\n\nTesting Sorted_List#is_identical")

print("\nEmpty lists")
my_list = Sorted_List()
other_list = Sorted_List()
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
identical = my_list.is_identical(other_list)
print("Returned identical: {}".format(identical))
print("Expected: {}".format(True))

print("\nOne empty, one non-empty")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
other_list = Sorted_List()
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
identical = my_list.is_identical(other_list)
print("Returned identical: {}".format(identical))
print("Expected: {}".format(False))

print("\nBoth non-empty, not identical")
my_list = Sorted_List()
other_list = Sorted_List()
for val in movies[:movies_mid]:
    my_list.insert(val)
for val in movies[movies_mid:]:
    other_list.insert(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
identical = my_list.is_identical(other_list)
print("Returned identical: {}".format(identical))
print("Expected: {}".format(False))

print("\nBoth non-empty, identical")
my_list = Sorted_List()
other_list = Sorted_List()
for val in movies[:movies_mid]:
    my_list.insert(val)
    other_list.insert(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
identical = my_list.is_identical(other_list)
print("Returned identical: {}".format(identical))
print("Expected: {}".format(True))

print("\n\nTesting Sorted_List#__contains__")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
key = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("Key: {}".format(key))
contains = key in my_list
print("Contains key: {}".format(contains))
print("Expected: {}".format(False))

print("\nNon-empty list, does not contain")
my_list = Sorted_List()
for val in movies[1:]:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
key = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("Key: {}".format(key))
contains = key in my_list
print("Contains key: {}".format(contains))
print("Expected: {}".format(False))

print("\nNon-empty list, does  contain")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
key = Movie("Dellamorte Dellamore", 1994, None, None, None)
print("Key: {}".format(key))
contains = key in my_list
print("Contains key: {}".format(contains))
print("Expected: {}".format(True))

print("\n\nTesting Sorted_List#__getitem__")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
index = 0
print("Getting at index: {}".format(index))
try:
    item = my_list[index]
except AssertionError:
    print("Invalid index since list empty. Assertion caught successfully.")

print("\nNon-empty list")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
index = 0
print("Getting at index: {}".format(index))
item = my_list[index]
print("Item at index: {}".format(item))
print("Expected: {}".format(my_list.min()))

print("\nIndex out of range")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
index = 0
print("Getting at index: {}".format(index))
try:
    item = my_list[index]
except AssertionError:
    print("Invalid index. Assertion thrown successfully.")

print("\n\nTesting Sorted_List#clean")

print("\nEmpty list")
my_list = Sorted_List()
print("List contents: {}".format([val for val in my_list]))
my_list.clean()
print("List cleaned")
print("List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list, no duplicates")
my_list = Sorted_List()
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
my_list.clean()
print("List cleaned")
print("List contents: {}".format([val for val in my_list]))

print("\nNon-empty list, some duplicates")
my_list = Sorted_List()
for i in range(2):
    my_list.insert(movies[0])
for val in movies:
    my_list.insert(val)
print("List contents: {}".format([val for val in my_list]))
my_list.clean()
print("List cleaned")
print("List contents: {}".format([val for val in my_list]))
print("Expected: {}".format(movies))

print("\nNon-empty list, all duplicates")
my_list = Sorted_List()
for i in range(5):
    my_list.insert(movies[0])
print("List contents: {}".format([val for val in my_list]))
my_list.clean()
print("List cleaned")
print("List contents: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[0]))

print("\n\nTesting Sorted_List#intersection")

print("\nEmpty lists")
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nOne empty list")
source1 = Sorted_List()
for val in movies:
    source1.insert(val)
source2 = Sorted_List()
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nBoth non-empty, no values shared")
source1 = Sorted_List()
for val in movies[:movies_mid]:
    source1.insert(val)
source2 = Sorted_List()
for val in movies[movies_mid:]:
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nBoth non-empty, some values shared")
source1 = Sorted_List()
for val in movies[:(movies_mid + 3)]:
    source1.insert(val)
source2 = Sorted_List()
for val in movies[movies_mid:]:
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format(movies[movies_mid:(movies_mid + 3)]))

print("\nBoth non-empty, all values shared")
source1 = Sorted_List()
source2 = Sorted_List()
for val in movies:
    source1.insert(val)
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\n\nTesting Sorted_List#union")

print("\nEmpty lists")
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nOne empty list")
source1 = Sorted_List()
for val in movies:
    source1.insert(val)
source2 = Sorted_List()
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\nBoth non-empty, no values shared")
source1 = Sorted_List()
for val in movies[:movies_mid]:
    source1.insert(val)
source2 = Sorted_List()
for val in movies[movies_mid:]:
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\nBoth non-empty, some values shared")
source1 = Sorted_List()
for val in movies[:(movies_mid + 3)]:
    source1.insert(val)
source2 = Sorted_List()
for val in movies[movies_mid:]:
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
expected = [val for val in movies]
expected.extend(movies[movies_mid:(movies_mid + 3)])
expected.sort()
print("Expected: {}".format(expected))

print("\nBoth non-empty, all values shared")
source1 = Sorted_List()
source2 = Sorted_List()
for val in movies:
    source1.insert(val)
    source2.insert(val)
target = Sorted_List()
print("List 1 contents: {}".format([val for val in source1]))
print("List 2 contents: {}".format([val for val in source2]))
target.intersection(source1, source2)
print("Target contents: {}".format([val for val in target]))
expected = [val for val in movies]
expected.extend(movies)
expected.sort()
print("Expected: {}".format(expected))