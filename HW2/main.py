#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Create very basic functions that return various outputs.
For the purposes of the Pirple Python is easy course.
Formatted according to PEP8
"""

genre_of_song = "R&B/soul, Rock"


def artist():
    """Just return the name of the artist"""
    return "Liquido"


def album():
    """Just return the name of the album which is defined as local variable"""
    album = "Liquido"
    return album


def genre():
    """Just return the global variable genre_of_song"""
    return genre_of_song


def boolean_function(query):
    """Extra credit function
    Take query, return True if query is 1 else return False
    """
    if query == 1:
        return True
    else:
        return False

# Call functions and print what they return
print(artist())
print(album())
print(genre())
print(boolean_function(1))
print(boolean_function(0))
