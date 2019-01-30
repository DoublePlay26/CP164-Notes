"""
------------------------------------------------------------------------
Assingment 2, Task 4 - Movie_utilities#get_by_genres
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-21
------------------------------------------------------------------------
"""
from Movie_utilities import get_by_genres, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

genres = []

user_input = int(input("Enter a genre code (-1 TO QUIT): "))
while user_input != -1:
    genres.append(user_input)
    user_input = int(input("Enter a genre code (-1 TO QUIT): "))

gmovies = get_by_genres(movies, genres)

for movie in gmovies:
    print("===========================================")
    print(movie)
