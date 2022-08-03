import sys
import os
from tkinter import *

ws = Tk()
ws.geometry('780x500')
ws.title('Speech recognition')
ws['bg']='#e6e6e6'

f = ("Times bold", 14)

def start():
    os.system('python gamecommands(fireemblemGBA).py')

def mainmenu():
    ws.destroy()
    os.system('python mainpage.py')
    
def games():
    ws.destroy()
    os.system('python games.py')
    
def change_color(choice):
    choice = variable.get()
    ws.config(bg=choice)
    label1.config(bg=choice)
    label2.config(bg=choice)
    label3.config(bg=choice)
    
label1=Label(
    ws,
    text="GBA controller",
    padx=20,
    pady=20,
    bg='#e6e6e6',
    font=f
)
label1.place(x=270, y=10)

label2=Label(
    ws,
    text="Commands",
    padx=20,
    pady=20,
    bg='#e6e6e6',
    font=f
)
label2.place(x=500, y=50)

label3=Label(
    ws,
    text="Change background color",
    padx=10,
    pady=10,
    bg='#e6e6e6',
    font=("Times bold", 13)
)
label3.place(x=550, y=0)

Button(
    ws, 
    text="Start",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=start
    ).place(x=100, y=200)

Button(
    ws, 
    text="Return to main menu",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=mainmenu
    ).place(x=100, y=420)

Button(
    ws, 
    text="Return to game selection",
    bd = 5,
    highlightthickness=4, 
    borderwidth=3,
    font=f,
    command=games
    ).place(x=400, y=420)

text = Text(ws, height=10,width=40, font = ('Ariel',12) , state = DISABLED, wrap=WORD )
text.place(x=400, y=100)
text.configure(state='normal')
text.insert('1.0', 'up - pritisak prema gore, down - pritisak prema dolje \n left - pritisak prema lijevo, right- pritisak prema desno \nstart - pritisak start, select - pritisak select \nback - pritisak B, ok - pritisak A \noption - pritisak R, return - pritisak L \nexit - izlaz iz programa')
text.configure(state='disabled')

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