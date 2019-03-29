"""
------------------------------------------------------------------------
Lab 10, Task 4 - Sorts with Linked Lists
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-25
------------------------------------------------------------------------
"""
from test_Sorts_List_linked import test_sort, SIZE, SORTS

print("n:{:^10d}    |{:^24s}|\t|{:^22s}|".format(SIZE, "Comparisons", "Swaps"))
print("{:<15s} {:<8s} {:<8s} {:^8s}\t{:<8s} {:<8s} {:<8s}".format("Algorithm", \
                                                                  "In Order", "Reversed", \
                                                                  "Random", "In Order", \
                                                                  "Reversed", "Random"))
SEP = "-"
print(SEP*15, SEP*8, SEP*8, SEP*8, '\t' + SEP*8, SEP*8, SEP*6)

for sort in SORTS:
    title = sort[0]
    sort_func = sort[1]
    test_sort(title, sort_func)
