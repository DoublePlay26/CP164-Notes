"""
------------------------------------------------------------------------
Assignment 1, Task 4 - Is Leap Year
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-14
------------------------------------------------------------------------
"""
from functions import is_leap_year

year = int(input("Enter a year: "))

leap_year = is_leap_year(year)

if leap_year:
    print("{} is a leap year!".format(year))
else:
    print("{} is NOT a leap year!".format(year))