#!/usr/bin/env python

import tkinter as tk

def on_slide(value):
    print(f"Slider value: {value}")

root = tk.Tk()

scale = tk.Scale(root, from_=0, to=1000, orient='horizontal', command=on_slide)
scale.pack(fill='x', expand=True)

root.mainloop()
