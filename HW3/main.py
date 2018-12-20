#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Create very basic function that returns True if there are at least two equal
inputs.
For the purposes of the Pirple Python is easy course.
Formatted according to PEP8.
"""


def are_equal(input1, input2, input3):
    """Take three inputs and return True if at least two are equal.
    Return false if there are no similarities.
    Convert string input to int (non-integer strings will raise an error).
    """
    input1 = int(input1)
    input2 = int(input2)
    input3 = int(input3)

    condition1 = (input1 == input2)
    condition2 = (input2 == input3)
    condition3 = (input3 == input1)

    if condition1 or condition2 or condition3:
        return True
    else:
        return False

# Simple test of the solution
# - Prints True because at least two are equal
print(are_equal(2, 2, 1))
# - Prints True because at least two are equal
print(are_equal(5, 5.0, 2))
# - Prints True because at least two are equal
print(are_equal(3, 3, 3))
# - Prints True because at least two are equal (one is string)
print(are_equal(6, 5, "5"))
# - Prints False because none are equal
print(are_equal(10, 20, 30))
