#! /usr/bin/env python

from Tkinter import *

root = Tk()
root.title(sys.argv[0].split('/')[-1])

c = Canvas(root, bg='#FFFFFF', width=500, height=400)
c.create_oval(100, 100, 400, 300, fill='green')
c.pack()

root.mainloop()
