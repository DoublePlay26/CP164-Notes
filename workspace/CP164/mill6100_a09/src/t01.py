"""
------------------------------------------------------------------------
Assignment 9, Task 1 - Hash_Set_Array, insert_words, comparison_total
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-03-25
------------------------------------------------------------------------
"""
from functions import insert_words, comparison_total
from Hash_Set_array import Hash_Set

print("Using array-based list Hash_Set")

fv = open('miserables.txt', 'r')
hs = Hash_Set(20)

insert_words(fv, hs)
total, max_word = comparison_total(hs)

print("\nTotal Comparisons: {:,}".format(total))
print("Word with max comparisons: {}: {:,}".format(max_word.word, max_word.comparisons))