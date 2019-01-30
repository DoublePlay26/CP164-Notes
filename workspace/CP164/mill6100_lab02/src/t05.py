"""
------------------------------------------------------------------------
Lab 2, Task 5 - utilities#stack_test but with Movie objects
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from utilities import stack_test
from Movie_utilities import read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

stack_test(movies)