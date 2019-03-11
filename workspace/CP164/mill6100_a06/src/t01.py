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
from Movie_utilities import read_movies
from Movie import Movie

fh = open('movies.txt', 'r')
movies = read_movies(fh)
movies_mid = len(movies) // 2


print("\n\nTesting List#is_identical")
print("\nSame values")
my_list = List()
other_list = List()
for val in movies:
    my_list.append(val)
    other_list.append(val)
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
print("Identical? {}\tExpected: {}".format(identical, True))

print("\nDifferent values")
my_list = List()
other_list = List()
for val in movies[:movies_mid]:
    my_list.append(val)
for val in movies[movies_mid:]:
    other_list.append(val)
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
print("Identical? {}\tExpected: {}".format(identical, False))

print("\nEmpty lists")
my_list = List()
other_list = List()
    
identical = my_list.is_identical(other_list)

print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
print("Identical? {}\tExpected: {}".format(identical, True))

print("\n\nTesting List#remove_many")
print("\nEmpty list")
my_list = List()
to_remove = Movie("Dellamorte Dellamore", 1994, None, None, None)
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
print("List contents after remove: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nMissing key")
my_list = List()
for val in movies[1:]:
    my_list.append(val)
to_remove = Movie("Dellamorte Dellamore", 1994, None, None, None)
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
print("List contents after remove: {}".format([val for val in my_list]))
print("Expected: {}".format(movies))

print("\nList only contains the key")
my_list = List()
for i in range(5):
    my_list.append(movies[0])
print("Initial contents: {}".format([val for val in my_list]))
to_remove = Movie("Dellamorte Dellamore", 1994, None, None, None)
my_list.remove_many(to_remove)
print("Removed: {}".format(to_remove))
print("List contents after remove: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\n\nTesting List#__getitem__")

print("\nEmpty list")
my_list = List()
try:
    item = my_list[0]
except AssertionError:
    print("Invalid index. Assertion thrown correctly")
    
print("\nList of values")
# No need to define my_list again here since empty from above
for val in movies:
    my_list.append(val)

item = my_list[0]
print("Item returned from my_list[0]: {}".format(item))
print("Expected: {}".format(movies[0]))

print("\n\nTesting List#clean")

print("\nEmpty list")
my_list = List()
my_list.clean()
print("Cleaned list")
print("Contents after clean: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNo duplicates")
my_list = List()
for val in movies:
    my_list.append(val)
print("Initial contents: {}".format([val for val in my_list]))
my_list.clean()
print("Cleaned list")
print("Contents after clean: {}".format([val for val in my_list]))
print("Expected: {}".format(movies))

print("\nSome duplicates")
my_list = List()
my_list.append(movies[0])
for val in movies:
    my_list.append(val)
print("Initial values: {}".format([val for val in my_list]))
my_list.clean()
print("Cleaned list")
print("Contents after clean: {}".format([val for val in my_list]))
expected = [val for val in movies]
expected.append(movies[0])
print("Expected: {}".format(expected))

print("\nAll values are the same")
my_list = List()
for i in range(5):
    my_list.append(movies[0])
my_list.clean()
print("Cleaned list")
print("Contents after clean: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[0]))

print("\n\nTesting List#intersection")

print("\nEmpty lists")
my_list = List()
other_list = List()
target = List()
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.intersection(my_list, other_list)
print("List intersection")
print("Contents of intersection: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nNo shared values")
my_list = List()
other_list = List()
target = List()
for val in movies[:movies_mid]:
    my_list.append(val)
for val in movies[movies_mid:]:
    other_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.intersection(my_list, other_list)
print("List intersection")
print("Intersection List contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nSome shared values")
my_list = List()
other_list = List()
target = List()
for val in movies[:(movies_mid + 3)]:
    my_list.append(val)
for val in movies[movies_mid:]:
    other_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.intersection(my_list, other_list)
print("List intersection")
print("Intersection List contents: {}".format([val for val in target]))
print("Expected: {}".format(movies[(movies_mid):(movies_mid +  3)]))

print("\nAll values are shared")
my_list = List()
other_list = List()
target = List()
for val in movies:
    my_list.append(val)
    other_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.intersection(my_list, other_list)
print("List intersection")
print("Intersection List contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\n\nTesting List#union")

print("\nEmpty lists")
my_list = List()
other_list = List()
target = List()
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.union(my_list, other_list)
print("List union")
print("Union List contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nOne empty list")
my_list = List()
other_list = List()
target = List()
for val in movies:
    my_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.union(my_list, other_list)
print("List union")
print("Union List contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\nOne empty list (opposite list of before test)")
my_list = List()
other_list = List()
target = List()
for val in movies:
    other_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.union(my_list, other_list)
print("List union")
print("Union List contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\nBoth lists non-empty")
my_list = List()
other_list = List()
target = List()
for val in movies[:movies_mid]:
    my_list.append(val)
for val in movies[movies_mid:]:
    other_list.append(val)
print("List 1 contents: {}".format([val for val in my_list]))
print("List 2 contents: {}".format([val for val in other_list]))
target.union(my_list, other_list)
print("List union")
print("Union List contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\n\nTesting List#prepend")

print("\nEmpty list")
my_list = List()
value = movies[-1]
print("Initial contents: {}".format([val for val in my_list]))
my_list.prepend(value)
print("Prepended {}".format(value))
print("Post-prepend contents: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[-1]))

print("\nList with initial values")
my_list = List()
for val in movies:
    my_list.append(val)
value = movies[0]
print("Initial contents: {}".format([val for val in my_list]))
my_list.prepend(value)
print("Prepended {}".format(value))
print("Post-prepend contents: {}".format([val for val in my_list]))
expected = [val for val in movies]
expected.insert(0, movies[0])
print("Expected: {}".format(expected))

print("\n\nTesting List#append")

print("\nEmpty list")
my_list = List()
value = movies[0]
print("Initial contents: {}".format([val for val in my_list]))
my_list.append(value)
print("Appended {}".format(value))
print("Post-append List contents: {}".format([val for val in my_list]))
print("Expected: {}".format(movies[0]))

print("\nList with initial values")
my_list = List()
for val in movies:
    my_list.append(val)
value = movies[0]
print("Initial contents: {}".format([val for val in my_list]))
my_list.append(value)
print("Appended {}".format(value))
print("Post-append List contents: {}".format([val for val in my_list]))
expected = [val for val in movies]
expected.append(movies[0])
print("Expected: {}".format(expected))

print("\n\nTesting List#remove_front")

print("\nEmpty list")
my_list = List()
print("Initial list contents: {}".format([val for val in my_list]))
try:
    value = my_list.remove_front()
except AssertionError:
    print("Tried removing from an empty list. Assertion thrown correctly")

print("\nPopulated list")
my_list = List()
for val in movies:
    my_list.append(val)
print("Initial list contents: {}".format(val for val in my_list))
value = my_list.remove_front()
print("Removed front of List")
print("Value removed from front: {}".format(value))
print("Expected: {}".format(movies[0]))
print("Contents of list after removing front: {}".format([val for val in my_list]))

print("\n\nTesting List#combine")

print("\nEmpty lists")
my_list = List()
other_list = List()
target = List()
print("List 1 Contents: {}".format([val for val in my_list]))
print("List 2 Contents: {}".format([val for val in other_list]))
target.combine(my_list, other_list)
print("Combined the lists")
print("Combined list contents: {}".format([val for val in target]))
print("Expected: {}".format([]))

print("\nOne empty list")
my_list = List()
other_list = List()
target = List()
for val in movies:
    my_list.append(val)
print("List 1 Contents: {}".format([val for val in my_list]))
print("List 2 Contents: {}".format([val for val in other_list]))
target.combine(my_list, other_list)
print("Combined the lists")
print("Combined list contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\nBoth non-empty")
my_list = List()
other_list = List()
target = List()
for val in movies[:movies_mid]:
    my_list.append(val)
for val in movies[movies_mid:]:
    other_list.append(val)
print("List 1 Contents: {}".format([val for val in my_list]))
print("List 2 Contents: {}".format([val for val in other_list]))
target.combine(my_list, other_list)
print("Combined the lists")
print("Combined list contents: {}".format([val for val in target]))
print("Expected: {}".format(movies))

print("\n\nTesting List#split")

print("\nEmpty list")
my_list = List()
print("Initial list contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split()
print("List split")
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list of length 1")
my_list = List()
my_list.append(movies[0])
print("Initial list contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split()
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format(movies[0]))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list of even length > 1")
my_list = List()
for val in movies[:4]:
    my_list.append(val)
print("Initial list contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split()
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format(movies[:2]))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format(movies[2:4]))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list of odd length > 1")
my_list = List()
for val in movies[:5]:
    my_list.append(val)
print("Initial list contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split()
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format(movies[:3]))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format(movies[3:5]))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\n\nTesting List#split_alt")

print("\nEmpty list")
my_list = List()
print("List initial contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split_alt()
print("List alt split")
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format([]))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format([]))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list with even length")
my_list = List()
for val in movies[:4]:
    my_list.append(val)
print("List initial contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split_alt()
print("List alt split")
expected1 = []
expected2 = []
for i in range(len(movies[:4])):
    movie = movies[i]
    if i % 2 != 0:
        expected1.append(movie)
    else:
        expected2.append(movie)
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format(expected1))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format(expected2))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))

print("\nNon-empty list with odd length")
my_list = List()
for val in movies[:5]:
    my_list.append(val)
print("List initial contents: {}".format([val for val in my_list]))
target1, target2 = my_list.split_alt()
print("List alt split")
expected1 = []
expected2 = []
for i in range(len(movies[:5])):
    movie = movies[i]
    if i % 2 != 0:
        expected1.append(movie)
    else:
        expected2.append(movie)
print("Target 1 Contents: {}".format([val for val in target1]))
print("Expected: {}".format(expected1))
print("Target 2 Contents: {}".format([val for val in target2]))
print("Expected: {}".format(expected2))
print("Original List contents: {}".format([val for val in my_list]))
print("Expected: {}".format([]))