"""
------------------------------------------------------------------------
Assignment 2, Task 3 - Movie_utilities#get_by_genre
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-20
------------------------------------------------------------------------
"""
from Movie_utilities import get_by_genre, read_movies

file_handle = open("movies.txt", 'r')

movies = read_movies(file_handle)

genre = int(input("Enter a genre code: "))

gmovies = get_by_genre(movies, genre)

for movie in gmovies:
    print("========================================")
    print(movie)