### Tuple can't be updated
#days_of_week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
#days_of_week[0] = 'Sunday'

#print(days_of_week)

PRINT("Introduction to Python")

PRINT(Introduction to Python)

### Tinker

"""
from tkinter import *

class MyFrame(Frame):
   def __init__(self):
      Frame.__init__(self)

      self.myCanvas = Canvas(width=300, height=200)

      my_font = ("Times", 16)

      self.myCanvas.create_text(50, 50, text="First", font=my_font)
      self.myCanvas.create_text(80, 80, text="Second", font=my_font)

      self.myCanvas.grid()

frame02 = MyFrame()
frame02.mainloop()
"""

from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=150, height=150, bg="white")
     self.myCanvas.grid()

     self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
     self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
     self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

     print ("Finds all shapes")
     print (self.myCanvas.find_enclosed(0, 0, 30, 70))

     print ("Finds middle shape")
     print (self.myCanvas.find_enclosed(0, 25, 30, 45))

     print ("Finds no shapes")
     print (self.myCanvas.find_enclosed(0, 0, 1, 1) )

frame02 = MyFrame()
frame02.mainloop()
