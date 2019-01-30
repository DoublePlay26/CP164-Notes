"""
------------------------------------------------------------------------
Testing for Stack_array#is_empty, pop, and peek methods
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from Stack_array import Stack

values = [1, 2, 3, 4]

print("Values: {}".format(values))

s = Stack()

print(">> Is the stack empty?")
empty = s.is_empty()

print("Expect: {}\tGot: {}".format(True, empty))

print(">> Pushing values onto Stack")

for val in values:
    s.push(val)
    
print("Stack contents: ", end='')
print("Expect: {}\tGot: ".format(values[::-1]), end='')
for elem in s:
    print(elem, end=' ')
print()
print(">> Pop top of stack")
value = s.pop()
print("Expect: {}\tGot: {}".format(values[-1], value))

print(">> Peek the top of the stack")
peeked = s.peek()
print("Expect: {}\tGot: {}".format(values[-2], peeked))
