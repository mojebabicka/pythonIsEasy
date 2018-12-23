#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Store atributes of my favorite song in a dictionary. Print out all values.

Extra credit:
Allow user to guess keys and values from the dictionary.

For the purposes of the Pirple Python is easy course.
Formatted according to PEP8
"""


def check_dictionary(key, value):
    if key not in song_atributes:
        print("Incorrect key.")
        return False
    elif song_atributes[key] == value:
        print("That is a correct answer.")
        return True
    else:
        print("Incorrect value.")
        return False

# Storing everything in a dictionary
song_atributes = {
    "artist": "Liquido",
    "album": "Liquido",
    "genre": "R&B/soul, Rock",
    "released_on_month_str": "August",
    "lyrics_beginning": ("So you face it with a smile\n"
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
                         ),
    "released_on_day": 31,
    "released_on_month": 8,
    "released_on_year": 1998,
    "duration_sec": 233,
    "sold_singles": 700000,
    "artist_founded": 1996,
    "artist_disbanded": 2009,
    "rating1": 4.4,   # at bestsongserver.com
    "rating2": 3.38,  # at rateyourmusic.com
    "rating3": 4.99   # my personal rating
    }

# Print all values of the dictionary
for atribute_key in song_atributes:
    print(song_atributes[atribute_key])

# Loop which allows user to guess keys and values in the dictionary
print("If you want to quit, enter key 'quit'.")
while True:
    key = input("Guess a key: ")
    if key == "quit":
        break
    value = input("Guess a corresponding value to that key: ")
    check_dictionary(key, value)
