"""
------------------------------------------------------------------------
Testing for Movie class accepting key values (i.e., accepting None)
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-04
------------------------------------------------------------------------
"""
from Movie import Movie
from List_array import List

movie = Movie('Juno', 2007, None, None, None)

print(movie)

l = List()
n = [[],[0, 1],1,2,3,4]
for i in n:
    l.append(i)
    
for i in l:
    print(i)

val = l.remove([0])

for i in l:
    print(i)
    
print("Val: {}".format(val))