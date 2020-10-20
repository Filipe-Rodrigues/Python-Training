'''
Created on Oct 20, 2020

@author: Filipe
'''

from tkinter import Tk
from tkinter import Label
from tkinter import Button

window = Tk()
window.title("Minesweeter")
window.geometry("640x480")

lbl = Label(window, text = "Sweet!", font = ("Tahoma", 18))
lbl.grid(column = 0, row = 0)

btn = Button(window, text = "Not a bomb")
btn.grid(column = 1, row = 0)

window.mainloop()




























