#!/usr/bin/env python

"""
2025July31
    copied from frame.py
    updated for Python3
    ej minor mods / cleanup
    working
"""


import tkinter as tk
from tkinter import RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID
from tkinter import LEFT


root = tk.Tk()
root.title('Frames')


for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    frame = tk.Frame(root, borderwidth=2, relief=relief)
    tk.Label(frame, text=relief, width=10).pack(side=LEFT)
    frame.pack(side=LEFT, padx=5, pady=5)        

root.mainloop()

