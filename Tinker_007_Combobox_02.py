# import everything from tkinter module
# import tkinter -- Python 3.x
# import Tkinter -- Python 2.x

# python program demonstrating
# Combobox widget using tkinter
  
"""
A combobox is a combination of an Entry widget and a Listbox widget.
A combobox widget allows you to select one value in a set of values.
In addition, it allows you to enter a custom value.
"""
  
import tkinter as tk
from tkinter import ttk
  
# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')

# Label
ttk.Label(window, text = "Select the Month :", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 15, padx = 10, pady = 25)
  
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December')
  
monthchoosen.grid(column = 1, row = 15)
  
# Shows January as a default value
monthchoosen.current(0)

# Shows february as a default value
# monthchoosen.current(1)

window.mainloop()
