"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-05
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    pq.insert(i)

pq.split_key(5)
for i in pq:
    print(i)