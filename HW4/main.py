#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Create a function that allows inserting of various inputs. Duplicit inputs
are stored in left overs list (duplicity not checked in this list).
For the purposes of the Pirple Python is easy course.
Formatted according to PEP8.
"""

# Create an empty lists
myUniqueList = []
myLeftovers = []


def append_list(input):
    """Take an input, check for duplicity and append if not duplicit
    (return True).
    If the input is duplicit, append it to left overs list
    (return False).
    """
    if input not in myUniqueList:
        myUniqueList.append(input)
        return True
    else:
        myLeftovers.append(input)
        return False

# Simple test of the solution
# - Initial element is added to the list
# - (anything will be added - cannot be duplicit)
append_list("Initial Element")
# - Another element that is not duplicit is added
append_list("Non-duplicit Element")
# - Another element of a different type is added
append_list(3)
# - A string element "3" is added. It is not duplicit because the previous
# - element is of a different type (integer).
append_list("3")
# - Duplicit element (ends up in myLeftovers list)
append_list("Initial Element")
# - Another duplicit element (ends up in myLeftovers list, no duplicity test)
append_list("Initial Element")
# - Print myUniqueList and myLeftovers
# - Expected result myUniqueList:
# - ["Initial Element", "Non-duplicit Element", 3, "3"]
# - Expected result myLeftovers:
# - ["Initial Element", "Initial Element"]
print(myUniqueList)
print(myLeftovers)
