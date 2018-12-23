#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Print out a table that consists of the following element
 |
--

The table cell consists of a space and borders.
Horizontal boarders are not used for the cells in the last row.
Vertical boarders are not used for the cells in the last column.
Because of this all tables consist of rows of (2 * columns - 1) characters.
Because of this all tables consist of columns of (2 * rows - 1) characters.

Extra credit:
The script checks the width of the terminal window and does not allow tables
that are wider than the width of the terminal window.

For the purposes of the Pirple Python is easy course.
Formatted according to PEP8.
"""

import os


def create_table(rows, columns):
    """Check the terminal width and return False if the width of the table is
    higher than the width of the terminal.
    Take rows and columns and create table of appropriate dimensions.
    Return True.
    """
    rows = 2 * rows - 1
    columns = 2 * columns - 1
    if os.get_terminal_size().columns >= columns:
        for row in range(rows):
            for column in range(columns):
                if row % 2 == 0:
                    if column == columns - 1:
                        print(" ")
                    elif column % 2 == 0:
                        print(" ", end="")
                    else:
                        print("|", end="")
                else:
                    if column == columns - 1:
                        print("-")
                    else:
                        print("-", end="")
        return True
    else:
        print("Table of size {}x{} does not fit the terminal window."
              .format(int((rows+1)/2), int((columns+1)/2))
              )
        return False

# Simple test of the solution
# - Create small table
create_table(3, 3)
# - Create rectangular table
create_table(5, 8)
# - Create big table (fits standard width of a terminal = 80)
create_table(40, 40)
# - Create huge table (should not fit any normal sized terminal)
create_table(40, 100)
