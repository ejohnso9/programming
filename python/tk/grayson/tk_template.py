#!/usr/bin/.env python

"""
DESCRIPTION
    6 frames on one row w/ different kinds of border
    "Python and Tkinter Programming", John Grayson

    NB: code slightly modified to deal with modern Python 3
        (e.g., from tkinter, not: from Tkinter)

HISTORY
    20126Jun07  typed in, tested: works! 
"""

# Standard Python Library
from tkinter import Label, mainloop

Label(text="This has to be the\nsimplest bit of code").pack()

# start the app
mainloop()
