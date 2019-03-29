"""
------------------------------------------------------------------------
Lab 10, Task 1 - test_Sorts_array
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-22
------------------------------------------------------------------------
"""
from test_Sorts_array import create_sorted, create_reversed, \
create_randoms

a = create_sorted()
b = create_reversed()
c = create_randoms()

print("Sorted:")
for num in a:
    print(num)
print("Reversed:")
for num in b:
    print(num)
print("Random Lists:")
print('[',end='')
for l in c:
    print('[',end='')
    for num in l:
        print(num,end=', ')
    print('],')
print(']')