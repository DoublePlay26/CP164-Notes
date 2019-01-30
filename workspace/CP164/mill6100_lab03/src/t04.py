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

values = [66,55,44,33,22,11]

for i in values:
    pq.insert(i)

removed = pq.remove()
print("removed: {}\tpeeked: {}".format(removed, pq.peek()))
assert pq.peek() == values[-2]