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

# Creating title
window.title('Combobox')

# Creating the frame size
window.geometry('500x250')
  
# label text for title
ttk.Label(window, text = "GFG Combobox Widget", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
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
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()
