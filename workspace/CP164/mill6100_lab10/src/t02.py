"""
------------------------------------------------------------------------
Lab 10, Task 2 - test_sort
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-25
------------------------------------------------------------------------
"""
from test_Sorts_array import test_sort, SORTS

for sort in SORTS:
    test_sort(sort[0], sort[1])

