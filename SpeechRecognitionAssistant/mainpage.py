import sys
import os
from tkinter import *

ws = Tk()
ws.geometry('780x500')
ws.title('Speech recognition')
ws['bg']='#e6e6e6'

f = ("Times bold", 14)

def browserassistant():
    ws.destroy()
    os.system('python browserassistantgui.py')

def desktophelper():
    ws.destroy()
    os.system('python desktopassistantgui.py')
    
def games():
    ws.destroy()
    os.system('python games.py')
    
def change_color(choice):
    choice = variable.get()
    ws.config(bg=choice)
    label1.config(bg=choice)
    label2.config(bg=choice)
    
    
label1=Label(
    ws,
    text="Speech recognition main page",
    padx=20,
    pady=20,
    bg='#e6e6e6',
    font=f
)
label1.place(x=225, y=110)

label2=Label(
    ws,
    text="Change background color",
    padx=10,
    pady=10,
    bg='#e6e6e6',
    font=("Times bold", 13)
)
label2.place(x=550, y=0)
Button(
    ws,
    text="Browser assistant",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=browserassistant
    ).place(x=90, y=200)

Button(
    ws, 
    text="Desktop helper",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=desktophelper
    ).place(x=290, y=200)

Button(
    ws, 
    text="Game controller",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=games
    ).place(x=490, y=200)


color_list = ['aquamarine', 'light blue', 'olive drab', 'gray', 'green', 'red', 'blue', 'yellow']

variable = StringVar()
variable.set(color_list[1])

dropdown = OptionMenu(
    ws,
    variable,
    *color_list,
    command=change_color
)
dropdown.config(width=9)
dropdown.config(height=1)
dropdown.place(x=600, y=40)

ws.mainloop()