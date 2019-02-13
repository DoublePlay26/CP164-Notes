"""
------------------------------------------------------------------------
Lab 5, Task 6 - Bag to Set
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-11
------------------------------------------------------------------------
"""
from functions import bag_to_set

#bag = [4,3,2,1,0]
#bag = [0,1,2,3,4]
bag = [4,5,3,4,5,2,2,4]
print("Bag: {}".format(bag))
set = bag_to_set(bag)
print("Set: {}".format(set))