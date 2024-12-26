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
root.title("Generic Tree")
# Set geometry (width x height)
root.geometry(f'{canvasWidth}x{canvasHeight}')

# create a canvas to draw
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, bg=background)

# create an instance of Draw
df = Draw(canvas)

# draw tree
centerTree = [250, 500]
truckHeight = 120
branchLength = 250
lineWight = 18
depth = 6

def drawBranch(center, branchLength, lineWight, depth):
    if depth == 0:
        return
    depth -= 1    
    lineWight -= 3
    twickHeight = 60

    newCenterLeft = [center[0]-branchLength, center[1]-twickHeight]
    newCenterRight = [center[0]+branchLength, center[1]-twickHeight]

    # branch
    coords = [newCenterLeft[0], newCenterLeft[1], center[0]-branchLength, center[1], center[0]+branchLength, center[1], newCenterRight[0], newCenterRight[1]]
    df.create_polyline(coords, line_width=lineWight)

    # node
    df.create_circle(center[0], center[1], 5, line_width=1, fill_color='red')

    # draw branches left
    drawBranch(newCenterLeft, branchLength/2, lineWight, depth)

    # draw branches right
    drawBranch(newCenterRight, branchLength/2, lineWight, depth)

    df.update()
    time.sleep(.1)

def drawTree():
    # draw trunk
    trunkEnd = [centerTree[0], centerTree[1]-truckHeight]
    df.create_line(centerTree[0], centerTree[1], trunkEnd[0], trunkEnd[1], line_width=lineWight)

    # draw branches
    drawBranch(trunkEnd, branchLength/2, lineWight, depth)

# Button Creation 
buttonTextFont = ("Helvetica", 20)
drawButton = Button(root, bg="blue", fg="yellow", font=buttonTextFont,
                        text = "Draw Tree",  
                        command = drawTree)
drawButton.place(x=10, y=440)	


# Execute Tkinter
root.mainloop()