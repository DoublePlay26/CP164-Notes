"""
------------------------------------------------------------------------
Assignment 2, Task 1 - Movie_utilities#get_by_year
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-20
------------------------------------------------------------------------
"""
from Movie_utilities import get_by_year, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

year = int(input("Enter a year: "))

ymovies = get_by_year(movies, year)

print("Movies in the year {}: ".format(year))

for movie in ymovies:
    print("==============================================")
    print(movie)