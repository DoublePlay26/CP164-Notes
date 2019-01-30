"""
------------------------------------------------------------------------
Assignment 2, Task 2 - Movie_utilities#get_by_rating
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-20
------------------------------------------------------------------------
"""
from Movie_utilities import get_by_rating, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

rating = float(input("Enter a rating: "))

rmovies = get_by_rating(movies, rating)

print("Movies with a rating >= {}: ".format(rating))

for movie in rmovies:
    print("==============================================")
    print(movie)
