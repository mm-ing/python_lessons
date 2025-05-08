#Graphics sample: Hypnosis Circles
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

df = Draw(canvas)

time_span = 0.1

# create circles
color = 'red'
startRadius = int(canvasWidth/2) # 250
endRadius = 25
center_x = canvasWidth/2
center_y = canvasHeight/2

for x in range(5):

    line_width = 22
    circle = []
    for radius in range(startRadius, endRadius, -25):
        if  line_width > 0:            
            circle.append(df.create_circle(center_x=center_x, center_y=center_y, radius=radius, line_width=line_width, outline_color=color, fill_color=background))
            canvas.pack()
            canvas.update()
            time.sleep(time_span)
            if color == 'red':
                color = 'blue'
            else:
                color = 'red'
            line_width -= 2

    # delete circles
    maxCircles = len(circle)-1
    for i in range(maxCircles, -1, -1):
        canvas.delete(circle[i])
        canvas.update()
        time.sleep(time_span)    

# Execute Tkinter
root.mainloop()