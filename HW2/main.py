#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Initialize several variables of various types and print them out.
For the purposes of the Pirple Python is easy course.
Formatted according to PEP8
"""


def artist():
    """Just return global variable artist"""
    return artist


def album():
    """Just return global variable album"""
    return album


def genre():
    """Just return global variable genre"""
    return genre


def boolean_function(query):
    """Extra credit function
    Take query, return True if query is 1 else return False
    """
    if query == 1:
        return True
    else:
        return False

# String song atributes
artist = "Liquido"
album = "Liquido"
genre = "R&B/soul, Rock"
released_on_month_str = "August"
lyrics_beginning = ("So you face it with a smile\n"
                    "There is no need to cry\n"
                    "For a trifle's more than this\n"
                    "Will you still recall my name\n"
                    "And the month it all began\n"
                    "Will you release me with a kiss\n"
                    "Have I tried to draw the veil\n"
                    "If I have - how could I fail?\n"
                    "Did I fear the consequence\n"
                    "Dazed by carelss words\n"
                    "Cosy in my mind"
                    )

# Integer song atributes
released_on_day = 31
released_on_month = 8
released_on_year = 1998
duration_sec = 233
sold_singles = 700000
artist_founded = 1996
artist_disbanded = 2009

# Float song atributes
rating1 = 4.4   # at bestsongserver.com
rating2 = 3.38  # at rateyourmusic.com
rating3 = 4.99  # my personal rating

# Call functions and print what they return
print(artist())
print(album())
print(genre())
print(boolean_function(1))
print(boolean_function(0))

# Print all variables out
# - String variables
print(artist)
print(album)
print(genre)
print(released_on_month_str)
print(lyrics_beginning)
# - Integer variables
print(released_on_day)
print(released_on_month)
print(released_on_year)
print(duration_sec)
print(sold_singles)
print(artist_founded)
print(artist_disbanded)
# - Float variables
print(rating1)
print(rating2)
print(rating3)
