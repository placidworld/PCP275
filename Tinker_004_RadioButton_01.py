# import everything from tkinter module
# import tkinter -- Python 3.x
# import Tkinter -- Python 2.x

# Importing Tkinter module
from tkinter import *

# from tkinter.ttk import *
 
# Creating master Tkinter window
master = Tk()
master.geometry("220x220")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons using dictionary
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5",
          "RadioButton 6" : "6"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value, indicator = 0,
                background = "light pink").pack(fill = X, ipady = 6)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
