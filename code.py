from PIL import ImageGrab
from Tkinter import *
import os
import time

 
root = Tk()

root.title("Screen Capture")
top = Frame(root)
top.pack(side=TOP)


def screenGrab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\capture_' + str(int(time.time())) +
'.png', 'PNG')
 
first = Button(top, width=35 , bg='#0303FF',activebackground='#0303FF', text = "Capture")
first["command"] = screenGrab
first.pack()


root.configure(bg='#0303FF')
root.mainloop()
