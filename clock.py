from tkinter import Tk
from tkinter import Label
import time
import sys


mster = Tk()
mster.title("Clock")

def get_time():
    timeVar = time.strftime('     %I:%M:%S:%p       ')
    clock.config(text=timeVar)
    clock.after(1000,get_time)

    

def clockDisplay():
    backround ="black"
    backround = Maximize
    forground = Maximize
    




clock = Label(mster, font=('ds-digital', 80,),bg="black",fg="cyan")
clock.pack(anchor='center')






get_time()

mster.mainloop()
