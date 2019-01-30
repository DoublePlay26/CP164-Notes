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
from Movie_utilities import read_movies
from utilities import priority_queue_test

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

priority_queue_test(movies)