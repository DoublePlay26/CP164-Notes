"""
------------------------------------------------------------------------
Midterm Practice - Set Testing
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-02-13
------------------------------------------------------------------------
"""
from Set import Set

set = Set()
vals = [1,2,3,4,3]
for i in range(len(vals)):
    set.insert(0, vals[i])
    
while not set.is_empty():
    val = set.remove()
    print(val)