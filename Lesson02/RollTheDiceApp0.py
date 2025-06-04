# Import Modules
from tkinter import *
import random

canvasWidth = 100
canvasHeight = 150
background = 'yellow'
 
# create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Roll The Dice App")
# Set geometry (width x height)
root.geometry(f'{canvasWidth}x{canvasHeight}')

# create content ************************

def start_rolling():
    loops = random.randint(5, 10)
    for i in range(loops):
        digit = random.randint(1, 6)
        textbox.delete(0, END)
        textbox.insert(0, str(digit))
        root.update()
        root.after(100)  # Pause for 100 milliseconds

textbox = Entry(root, font=("Arial", 32), justify="center", width=2)
textbox.pack(pady=20)

start_button = Button(root, text="Start", font=("Arial", 16), command=start_rolling)
start_button.pack(pady=10)

# Execute Tkinter event loop ************
root.mainloop() 

