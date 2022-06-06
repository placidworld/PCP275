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
  
root = tk.Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = root.Create_text(root, height = 5, width = 52)
 
# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))
 
Fact = """A man can be arrested in
Italy for wearing a skirt in public."""
 
# Create button for next text.
b1 = Button(root, text = "Next", )
 
# Create an Exit button.
b2 = Button(root, text = "Exit", command = root.destroy)
 
l.pack()
T.pack()
b1.pack()
b2.pack()
 
# Insert The Fact.
T.insert(tk.END, Fact)
 
tk.mainloop()
