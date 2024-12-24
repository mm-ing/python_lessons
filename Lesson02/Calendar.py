# Import the 'calendar' module
from calendar import calendar
from tkinter import *

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

def create_calendar(year, month):
    # Print the calendar for the specified year and month
    return calendar.month(year, month)

# input1 TextBox  
inputYear = Text(root, 
                   height = 2, 
                   width = 20) 
inputYear.pack() 

# input1 TextBox  
inputMonth = Text(root, 
                   height = 2, 
                   width = 20) 
inputMonth.pack() 

# ouput TextBox  
output_calendar = Text(root, 
                   height = 25, 
                   width = 100) 
output_calendar.pack()  


def printCalendar():     
    year = inputYear.get(1.0, "end")
    month = inputMonth.get(1.0, "end")
    calendar_result = calendar(int(year), int(month))
    output_calendar.delete(1.0, END)
    output_calendar.insert(END, calendar_result) 


  
# Button Creation 
printButton = Button(root, 
                        text = "Print calendar",  
                        command = printCalendar) 
printButton.pack() 

canvas.pack()

# Execute Tkinter
root.mainloop()


# # Prompt the user to input the year and month
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))

# # Print the calendar for the specified year and month
# print(calendar.month(y, m))