"""
------------------------------------------------------------------------
Assignment 5, Task 1 - is_identical, remove_many, __getitem__, clean, 
intersection, union, prepend, append, remove_front, combine, split, 
split_alt
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-27
------------------------------------------------------------------------
"""
from List_linked import List
from Movie_utilities import read_movies
from Movie import Movie

fh = open('movies.txt', 'r')
movies = read_movies(fh)
# Human readable of movies list
hr_movies = []
for movie in movies:
    hr_movies.append(movie)
my_list = List()

print("Testing 'List#is_identical'")
print("\n\tTest list of movies vs empty list")
my_other_list = List()
for val in hr_movies:
    my_list.append(val)
for val in []:
    my_other_list.append(val)
identical = my_list.is_identical(my_other_list)
print("List 1 Contents: {}".format(hr_movies))
print("List 2 Contents: {}".format([]))
print("Identical? {}\tExpecting: {}".format(identical, False))

print("\n\tTest list of movies vs list of movies")
my_other_list = List()
for val in hr_movies:
    my_other_list.append(val)
identical = my_list.is_identical(my_other_list)
print("List 1 Contents: {}".format(hr_movies))
print("List 2 Contents: {}".format(hr_movies))
print("Identical? {}\tExpecting: {}".format(identical, True))

print("\n\tTest empty list vs empty list")
my_list = List()
my_other_list = List()
for val in []:
    my_list.append(val)
for val in []:
    my_other_list.append(val)
identical = my_list.is_identical(my_other_list)
print("List 1 Contents: {}".format([]))
print("List 2 Contents: {}".format([]))
print("Identical? {}\tExpecting: {}".format(identical, True))

print("\nTesting List#remove_many")
my_list = List()
for val in hr_movies:
    my_list.append(val)
# Add movies twice so there are duplicates
for val in hr_movies:
    my_list.append(val)
print("List contents before remove: {}".format(hr_movies))
my_list.remove_many(Movie("Juno", 2007, None, None, None))
print("Key removed: {}".format(hr_movies[8]))
contents = []
for val in my_list:
    contents.append(val)
print("List contents after remove: {}".format(contents))
#print("Expected: {}".format([1,2,4,2,5,4]))

print("\nTesting List#__getitem__")
my_list = List()
for val in hr_movies:
    my_list.append(val)
expected = hr_movies[0]
value = my_list[0]
print("Value returned from index access: {}".format(value))
print("Expected: {}".format(expected))

print("\nTesting List#clean")
my_list = List()
for val in hr_movies:
    my_list.append(val)
for val in hr_movies:
    my_list.append(val)
my_list.clean()
print("Cleaned the list")
contents = []
for val in my_list:
    contents.append(val)
print("List contents after clean: {}".format(contents))
print("Expected: {}".format(hr_movies))

print("\nTesting List#intersection")

print("\nTesting List#union")

print("\nTesting List#prepend")
my_list = List()
for val in hr_movies:
    my_list.append(val)
my_list.prepend(hr_movies[-1])
print("Prepended {}".format(hr_movies[-1]))
contents = []
for val in my_list:
    contents.append(val)
print("List contents after prepend: {}".format(contents))
print("Expected: {}{}".format(hr_movies, hr_movies[-1]))

print("\nTesting List#append")
my_list = List()
for val in hr_movies:
    my_list.append(val)
my_list.append(hr_movies[0])
print("Appended 5")
contents = []
for val in my_list:
    contents.append(val)
print("List contents after append: {}".format(contents))
print("Expected: {}{}".format(hr_movies[0], hr_movies))

print("\nTesting List#remove_front")
my_list = List()
print("Original values: {}".format(hr_movies))
for val in hr_movies:
    my_list.append(val)
front = my_list.remove_front()
print("Removed the front node of the list")
contents = []
for val in my_list:
    contents.append(val)
print("List contents after remove: {}".format(contents))
print("Expected list contents: {}".format(hr_movies[1:]))
print("Value returned after removing front: {}".format(front))
print("Expected value: {}".format(hr_movies[0]))

print("\nTesting List#combine")
print("Empty initial List:")
my_list = List()
my_other = List()
middle = (len(hr_movies)//2) - 1
for val in hr_movies[:middle]:
    my_list.append(val)
for val in hr_movies[middle:]:
    my_other.append(val)
print("List 1: {}".format(hr_movies[:middle]))
print("List 2: {}".format(hr_movies[middle:]))
combined = List()
combined.combine(my_list, my_other)
print("Combined the two lists into combined.")
contents = []
for val in combined:
    contents.append(val)
print("Contents of combined: {}".format(contents))
print("Expected: {}".format(hr_movies))
my_list_contents = []
for val in my_list:
    my_list_contents.append(val)
print("Contents of source1: {}".format(my_list_contents))
my_other_contents = []
for val in my_other:
    my_other_contents.append(val)
print("Contents of source2: {}".format(my_other_contents))

print("\n\tInitial List has values already")
my_list = List()
my_list2 = List()
my_other = List()
my_list.append(hr_movies[0])
for val in hr_movies[:middle]:
    my_list2.append(val)
for val in hr_movies[middle:]:
    my_other.append(val)
content = []
for val in my_list:
    content.append(val)
print("Initial values: {}".format(content))
print("List 1: {}".format(hr_movies[:middle]))
print("List 2: {}".format(hr_movies[middle:]))
my_list.combine(my_list2, my_other)
print("Combined the two lists into combined.")
contents = []
for val in my_list:
    contents.append(val)
print("Contents of combined: {}".format(contents))
print("Expected: {}{}".format(hr_movies[0], hr_movies))
my_list2_contents = []
for val in my_list2:
    my_list2_contents.append(val)
print("Contents of source1: {}".format(my_list2_contents))
my_other_contents = []
for val in my_other:
    my_other_contents.append(val)
print("Contents of source2: {}".format(my_other_contents))

print("\nTesting List#split")
my_list = List()
for val in hr_movies:
    my_list.append(val)
print("Initial contents of List: {}".format(hr_movies))
target1, target2 = my_list.split()
print("Split the list")
contents1 = []
for val in target1:
    contents1.append(val)
print("Contents of target1: {}".format(contents1))
print("Expected: {}".format(hr_movies[:middle]))
contents2 = []
for val in target2:
    contents2.append(val)
print("Contents of target2: {}".format(contents2))
print("Expected: {}".format(hr_movies[middle:]))
contents = []
for val in my_list:
    contents.append(val)
print("Contents of original List: {}".format(contents))

print("\nTesting List#split_alt")
my_list = List()
for val in hr_movies:
    my_list.append(val)
print("Initial contents of List: {}".format(hr_movies))
target1, target2 = my_list.split_alt()
print("Split alt the list")
contents1 = []
for val in target1:
    contents1.append(val)
print("Contents of target1: {}".format(contents1))
print("Expected: {}".format(hr_movies[0:-1:2]))
contents2 = []
for val in target2:
    contents2.append(val)
print("Contents of target2: {}".format(contents2))
print("Expected: {}".format(hr_movies[1:-1:2]))
contents = []
for val in my_list:
    contents.append(val)
print("Contents of original list: {}".format(contents))
