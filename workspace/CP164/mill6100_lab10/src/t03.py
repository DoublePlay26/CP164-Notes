"""
------------------------------------------------------------------------
Lab 10, Task 3 - Using test_sort
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-25
------------------------------------------------------------------------
"""
from test_Sorts_array import test_sort, SORTS, SIZE

print("n:{:^10d}    |{:^23s}|\t|{:^22s}|".format(SIZE, "Comparisons", "Swaps"))
print("{:<15s} {:<8s} {:<8s} {:^8s}\t{:<8s} {:<8s} {:<8s}".format("Algorithm", \
                                                                  "In Order", "Reversed", \
                                                                  "Random", "In Order", \
                                                                  "Reversed", "Random"))
SEP = "-"
print(SEP*15, SEP*8, SEP*8, SEP*7, '\t' + SEP*8, SEP*8, SEP*6)

for sort in SORTS:
    title = sort[0]
    sort_func = sort[1]
    test_sort(title, sort_func)
