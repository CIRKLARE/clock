#!/bin/python3
from tkinter import *
from tkinter.ttk import *
from time import  strftime
import time

root= Tk()
root.title("Clock")

def time():
    string=strftime('%r')
    label.config(text=string)
    label.after(1000, time)

label= Label(root, font= ("ds-digital",20) , background= "blue" , foreground= "white")
label.pack(anchor="center")
time()
mainloop()
