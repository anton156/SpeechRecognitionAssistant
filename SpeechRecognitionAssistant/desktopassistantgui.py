import sys
import os
from tkinter import *

ws = Tk()
ws.geometry('780x500')
ws.title('Speech recognition')
ws['bg']='#e6e6e6'

f = ("Times bold", 14)

def start():
    os.system('python desktophelper.py')

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
    text="Desktop assistant",
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

text = Text(ws, height=15,width=54, font = ('Ariel',10) , state = DISABLED, wrap=WORD )
text.place(x=380, y=100)
text.configure(state='normal')
text.insert('1.0', 'recycle - recycles recycle bin, screenshot - takes screenshot \nencrypt - turns word into morse code \nmemory - tells user RAM and CPU usage \nbattery - tells battery percentage \ncreate - creates folder on desktop, time - tells time \ntext - writes txt file, joke - tells python joke \ncamera - takes picture with camera \ndown - volume down by 10, up - voulume up by 10 \nwindows -presses windows key \nshut down - shuts down pc, restart - restarts pc \nwait - stops program for 60 sec, stop - stops for 300 sec \nhold - stops for 600 sec \ntime out - stop program until user says start \nexit - closes program')
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