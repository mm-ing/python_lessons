# Import Module
from tkinter import *
from DrawingFunctions import Draw
import time

canvasWidth = 500
canvasHeight = 500
background = 'yellow'

 
# create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Graphics")
# Set geometry (width x height)
root.geometry(f'{canvasWidth}x{canvasHeight}')

# create a canvas to draw
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg=background)

# create an instance of Draw
df = Draw(canvas)

# generate code ....

canvas.pack()



# Execute Tkinter
root.mainloop()