import sys
import os
from tkinter import *

ws = Tk()
ws.geometry('780x500')
ws.title('Speech recognition')
ws['bg']='#e6e6e6'

f = ("Times bold", 14)

def start():
    os.system('python browserassistant.py')

def mainmenu():
    ws.destroy()
    os.system('python mainpage.py')
    
def change_color(choice):
    choice = variable.get()
    ws.config(bg=choice)
    label1.config(bg=choice)
    label2.config(bg=choice)
    label3.config(bg=choice)
    
label1=Label(
    ws,
    text="Browser assistant",
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
    ).place(x=250, y=420)


text = Text(ws, height=19,width=54, font = ('Ariel',10) , state = DISABLED, wrap=WORD )
text.place(x=380, y=100)
text.configure(state='normal')
text.insert('1.0', 'Search - searches google, video - searches youtube \nclose -  closes tab,  home - hoempage \nright,left -selects next right or left tab, \nrefresh - page refresh, top,bottom - goes to top or bottom of page up,down - scrolls up or down on page \nbookmark - bookmarks page, previous - back on last page forward - goes on next loaded page \nnext,back - goes on next selectable or on previous \nprint - prints page, put down - writes, ok - enter \ndownload - opens downloads, manager - opens bookmark \nmenu - opens options, find - finds on page, save - saves page \nhistory - opens history, full - opens fullscreen or closes\ndeveloper - opens developer tab , delete - deletes history \nwait- stops program for 60 sec, hold - stops for 300 seconds \ntime out - stops until user says start, exit - closes program')
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