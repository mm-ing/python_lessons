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

def create_loco_body(lower_left_x, lower_left_y, line_length):
    geometry = []
    offset = 0     
    x = lower_left_x+offset
    y = lower_left_y-offset   
    lines = [['v', -6], ['h', -1], ['v', -1], ['h', 5], ['v', 3], ['h', 2], ['v', -1]]
    geometry.append(df.create_ortho_lines(lines, line_length, x, y))
    lines = [['h', 13], ['vh', -2], ['v', -2], ['h', -1], ['v', -4], ['h', -1], ['v', 4], ['h', -1], ['v', -1]]
    geometry.append(df.create_ortho_lines(lines, line_length, x, y))
    return geometry

def run_loco(): 
    circles = []
    seg_length = 10
    locoStart = [i, 400]
    # body
    loco = create_loco_body(locoStart[0], locoStart[1], seg_length)
    # smoke pipe
    coord = locoStart[0] + 6 * seg_length, locoStart[1] - 6 * seg_length, locoStart[0] + 8 * seg_length, locoStart[1] - 4 * seg_length
    circles.append(df.create_arc(coord[0], coord[1], coord[2], coord[3], 0, 180, fill_color='red')) 
    # window
    coord = locoStart[0] + 1 * seg_length, locoStart[1] - 4 * seg_length, locoStart[0] + 3 * seg_length, locoStart[1] - 6 * seg_length
    circles.append(df.create_rectangle(coord[0], coord[1], coord[2], coord[3]))
    # wheel 1
    circles.append(df.create_circle(locoStart[0] + 3 * seg_length, locoStart[1], seg_length))
    # wheel 2
    circles.append(df.create_circle(locoStart[0] + 9 * seg_length, locoStart[1], seg_length))

    canvas.pack()
    canvas.update()    
    
    time.sleep(.1)

    # delete all objects
    for loco_line in loco:
        canvas.delete(loco_line)

    for circle in circles:
        canvas.delete(circle)
    canvas.pack()

for j in range(1, 10):
    for i in range(15, 370, 5):
        run_loco()
    for i in range(370, 15, -5):
        run_loco()

# Execute Tkinter
root.mainloop()