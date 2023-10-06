'''Tuples are immutable'''
days_of_week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
'''This statement generates error'''
#days_of_week[0] = 'Sunday'


#GUI example
from tkinter import *
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)


        self.myCanvas = Canvas(width = 300, height=200)
        my_font = ("Times", 16)
        self.myCanvas.create_text(50,50,text="First",font=my_font)
        self.myCanvas.create_text(80,80,text="Second",font=my_font)
        self.myCanvas.grid()

frame02=MyFrame()
frame02.mainloop()
