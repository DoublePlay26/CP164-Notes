"""
------------------------------------------------------------------------
Assignment 1, Task 2: Shift
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-11
------------------------------------------------------------------------
"""
from functions import shift

file_handle_r = open('pelee.txt', 'r')
file_handle_w = open('shift.txt', 'w')

# Read lines from the file
file_handle_r.seek(0)
file_contents = file_handle_r.readlines()

plaintext = "".join(file_contents)

n = int(input("Enter shift amount: "))

estring = shift(plaintext, n)

for char in estring:
    file_handle_w.write(char)