# import everything from tkinter module
# import tkinter -- Python 3.x
# import Tkinter -- Python 2.x

from tkinter import *
  
root = Tk()

"""
C = Canvas(root, height, width, bd, bg, ......)
Root = root window
height = height of the canvas widget
width = width of the canvas widget
bg = background color for canvas
bd = bordr of the canvas window
scrollregion (w, n, e, s) = tuple defined as a region for scrolling left, top,
                            bottom and right
hightlightcolor = color shown in the focus highlight
cursor = it can be defined as a cursor for the canvas which can be a circle,
         a do, an arrow, etc.
confine = decides if canvas can be accessed outside the scroll region
relief = type of the border which can be SUNKEN, RAISED, GROOVE and RIDGE
"""

# Canvas widget display various graphics on the application.
# It can be used to draw simple shapes to complicated graphs.
# It can also display kinds of custom wedgets according to the needs

# C = Canvas(root, height, width, bd, bg ...)

C = Canvas(root, bg="yellow", height=250, width=300)
 
# Creating a line
# line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)

line = C.create_line(108, 120, 320, 40, fill="green")

# Creating an arc
# arc = C.create_arc(20, 50, 190, 240, start=0, extend=110, fill="red")

arc = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")

# Creating an Oval
# oval = C.create_polygon(x0, y0, x1, yn, ..., xn, yn, options)

oval = C.create_oval(80, 30, 140, 150, fill="blue")
 
C.pack()
mainloop()
