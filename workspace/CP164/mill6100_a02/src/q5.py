"""
------------------------------------------------------------------------
Assignment 2, Task 5 - Movie_utilities#genre_counts
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-22
------------------------------------------------------------------------
"""
from Movie_utilities import genre_counts, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

counts = genre_counts(movies)

print("Counts: {}".format(counts))
