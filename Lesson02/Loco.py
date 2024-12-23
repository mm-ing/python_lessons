# Import Module
from tkinter import *
import math
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

def create_circle(center_x, center_y, radius, outline_color, width):  
    x, y = center_x, center_y
    r = radius
    circle = canvas.create_oval(x-r, y-r, x+r, y+r, outline=outline_color, fill='red', width=width)
    return circle

def create_ortho_lines(line_list, line_length, x, y):
    loco = []
    for line in line_list:
        s_x = x
        s_y = y
        e_x = s_x
        e_y = s_y
        if line[0] == 'v':
            e_y = s_y + line_length * line[1]
        if line[0] == 'h':
            e_x = s_x + line_length * line[1]
        if line[0] == 'vh':
            e_x = s_x + line_length * line[1]
            e_y = s_y + line_length * line[1]
        # create line
        loco.append(canvas.create_line(s_x, s_y, e_x, e_y, fill='blue', width=2))
        x = e_x
        y = e_y    
    return [x, y, loco]

def create_loco_body(lower_left_x, lower_left_y, line_length):
    offset = 0     
    x = lower_left_x+offset
    y = lower_left_y-offset   
    lines = [['v', -6], ['h', -1], ['v', -1], ['h', 5], ['v', 3], ['h', 2], ['v', -1]]
    line_def = create_ortho_lines(lines, line_length, x, y)
    loco = line_def[2]
    lines = [['v', 1], ['h', 1], ['v', -4], ['h', 1], ['v', 4], ['h', 1], ['v', 2], ['vh', 2], ['h', -13]]
    line_def[0] = line_def[0] + 2 * line_length
    line_def = create_ortho_lines(lines, line_length, line_def[0], line_def[1])
    loco.extend(line_def[2])
    return loco

circles = []
seg_length = 10
locoStart = [15, 400]
#body
loco = create_loco_body(locoStart[0], locoStart[1], seg_length)

#wheel 1
circles.append(create_circle(locoStart[0] + 3 * seg_length, locoStart[1], seg_length, 'blue', width=2))
#wheel 2
circles.append(create_circle(locoStart[0] + 9 * seg_length, locoStart[1], seg_length, 'blue', width=2))

canvas.pack()
canvas.update()
time.sleep(1)

# Delete all objects
for loco_line in loco:
    canvas.delete(loco_line)

for circle in circles:
    canvas.delete(circle)

canvas.pack()

# Execute Tkinter
root.mainloop()