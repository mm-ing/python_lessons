# Import Module
from tkinter import *
 
# create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Python GUI")
# Set geometry (widthxheight)
root.geometry('350x100')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='Menu', menu=item)
root.config(menu=menu)
 
# adding a label to the root window
lbl = Label(root, text = "Are you a Geek? Give an answer! ")
lbl.grid()
 
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
 
 
# function to display user text when
# button is clicked
def clicked():
 
    res = "You wrote " + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)
 
# Execute Tkinter
root.mainloop()