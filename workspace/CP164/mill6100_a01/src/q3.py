"""
------------------------------------------------------------------------
Assignment 1, Task 3 - Is Palindrome
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from functions import is_palindrome

word = input("Enter a word: ")

palindrome = is_palindrome(word)

if palindrome:
    print("{} is a palindrome!".format(word))
else:
    print("{} is NOT a palindrome!".format(word))