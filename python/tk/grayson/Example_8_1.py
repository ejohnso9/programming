#!/usr/bin/env python
# file: Example_8_1.py

"""
"Python and Tkinter Programming", John Grayson, 2nd printing, Example 8.1

This code is being updated to use best practices and run under Python 3.

In particular, NOTE (from ChatGPT answer):
    In Python 2, Tkinter modules were named like:
        Tkinter, tkFileDialog, tkMessageBox, etc.
    In Python 3, they are all grouped under the tkinter package (lowercase):
        tkinter, tkinter.filedialog, tkinter.messagebox, etc.

HISTORY
  2025Jul28 entered code from book, running
"""


import tkinter as tk
import tkinter.messagebox
import Pmw


class App:
    def __init__(self, master):
        # after answering the dialog, the main app window is an EntryField showing the button value
        # returned from the dialog
        self.result = Pmw.EntryField(master, entry_width=8, value='',
                                     # label_text='Returned value: ', labelpos=tk.W, labelmargin=1)
                                     label_text='RV button: ', labelpos=tk.W, labelmargin=1)
        self.result.pack(padx=15, pady=15)


root = tk.Tk()
question = App(root)

# NB: the book code of using tk.NO (value 0) no longer valid. Need string: 'no'.
button = tkinter.messagebox.askquestion("Question:", "Oh dear, did somebody\nsay mattress to Mr. Lambert?",
                                        default="no")
question.result.setentry(button)
root.mainloop()

