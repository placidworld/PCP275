### tinkter
"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        
frame01 = MyFrame()
frame01.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("250x200")
        self.master.title("My GUI")
        self.grid()

        self.message = Label(self, text = "Hello World!")
        self.message.grid()

frame01 = MyFrame()
frame01.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x260")
        self.master.title("My GUI Test")
        self.grid()

        self.button_click_here = Button(self, text = "Click Here",
                                        command = self.click_here_click)
        self.button_click_here.grid()

    def click_here_click(self):
        print("You Dit It!")

frame02 = MyFrame()
frame02.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x280")
        self.master.title("Haha, My GUI")
        self.grid()

        self.button_click_here = Button(self, text = "Click Here",
                                        command = self.click_here_click)
        self.button_click_here.grid()

        self.my_text = StringVar()

        self.message = Label(self, textvariable = self.my_text)
        self.message.grid()

    def click_here_click(self):
        self.my_text.set("You Did It!")

frame03 = MyFrame()
frame03.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("320x220")
        self.master.title("I try Tkinter GUI")
        self.grid()

        self.prompt = Label(self, text = "What's your name?")
        self.prompt.grid()

        self.input = Entry(self)
        self.input.grid()

        self.button_submit = Button(self, text = "Submit", command = self.submit_click)
        self.button_submit.grid()

        self.my_text = StringVar()
        self.message = Label(self, textvariable = self.my_text)
        self.message.grid()

    def submit_click(self):
        output_message = "Hi " + self.input.get()
        self.my_text.set(output_message)

frame04 = MyFrame()
frame04.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("400x200")
        self.master.title("This is GUI")
        self.grid()

        self.prompt = Label(self, text = "What's your name?")
        self.prompt.grid(row = 0, column = 0)

        self.input = Entry(self)
        self.input.grid(row = 0, column = 1)

        self.button_submit = Button(self, text = "Submit",
                                    command = self.submit_click)
        self.button_submit.grid()

        self.my_text = StringVar()
        self.message = Label(self, textvariable = self.my_text)
        self.message.grid()

    def submit_click(self):
        output_message = "Hi " + self.input.get()
        self.my_text.set(output_message)

frame05 = MyFrame()
frame05.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Try different GUI frame")
        self.grid()

        self.prompt = Label(self, text = "What's your name?")
        self.prompt.grid(row = 0, column = 0)

        self.input = Entry(self)
        self.input.grid(row = 0, column = 1)

        self.button_submit = Button(self, text = "Submit",
                                    command = self.submit_click)
  #      self.button_submit.grid(columnspan = 2)
        self.button_submit.grid(columnspan = 2, pady = 10)

        self.my_text = StringVar()
        self.message = Label(self, textvariable = self.my_text)
        self.message.grid(columnspan = 2)

    def submit_click(self):
        output_message = "Hi " + self.input.get()
        self.my_text.set(output_message)

frame06 = MyFrame()
frame06.mainloop()
"""

"""
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text = "Some Sample Text",
                                  font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                                      variable = self.bold_on,
                                      command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                                           variable = self.underline_on,
                                           command = self.set_font)
        self.check_underline.grid(row = 1, column =1)

    def set_font(self):
        new_font = "Courier 10"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"

        self.sample_label.config(font = new_font)

frame07 = MyFrame()
frame07.mainloop()
"""

from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Try RadioButton")
        self.grid()

        self.sample_label = Label(self, text = "Some Sample Text", font = "Calibri 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                                     variable = self.bold_on,
                                     command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                                           variable = self.underline_on,
                                           command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

        self.point_size = StringVar()
        self.point_size.set("10")
        
        self.ten_point = Radiobutton(self, text = "10 point",
                                     variable = self.point_size, value = "10",
                                     command = self.set_font)
        self.ten_point.grid(row = 2, column = 0)

        self.twelve_point = Radiobutton(self, text = "12 point",
                                        variable = self.point_size, value = "12",
                                        command = self.set_font)
        self.twelve_point.grid(row = 2, column = 1)

    def set_font(self):
        new_font = "Courier"

        if self.point_size.get() == "10":
            new_font = new_font + " 10"
        else:
            new_font = new_font + " 12"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"

        self.sample_label.config(font = new_font)

frame08 = MyFrame()
frame08.mainloop
