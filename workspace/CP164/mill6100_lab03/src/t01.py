"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-28
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

values = [44,22,11,55,33]

for val in values:
    pq.insert(val)
    
assert pq.peek() == 11, "Error"