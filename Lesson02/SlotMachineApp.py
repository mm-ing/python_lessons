#UI for a Slot Machine Game
# Initial
# credit balance: 10
# Text: "Try your luck!"
# Button: "Spin the wheel"
# Action: All wheels spin 10 times, than first stop. Next 10 times loop, than second stop. Next 10 times loop, than third stop.
# Rewards: 2xeqal no -> +1, 3x equal no -> +5, 3x 7 -> +10 otherwise -1
# Text: "You won x credits!" or "You lost x credit!"
# Option: for each spin stop-button

# Import Module
from tkinter import *
import clsSlotMachine

# *** section INITIALIZATION

# add spinner with array of random values, credit balance and result message
spinner=clsSlotMachine.Spinner()

# *** UI: create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Lucky No 7")
# Set geometry (width x height)
root.geometry('350x250')

# define grid size
col_count = 10
row_count = 6

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=30)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=30)

#credit label
creditTextFont = {'family' : 'normal',
                    'weight' : 'bold',
                    'size' : 32}
creditLabel = Label(root, text="Current Credit: " + str(spinner.credit), font=creditTextFont)
creditLabel.grid(column=1, row=0, columnspan=10, padx=2, pady=5)

# adding a message to the root window
guidingTextFont = {'family' : 'normal',
                    'weight' : 'bold',
                    'size' : 24}
guidingMessage = Message(root, text = spinner.actionText[0], width=320, font=guidingTextFont)
guidingMessage.grid(column=0, columnspan=10, row=4, rowspan=2, padx=2, pady=10)

# adding spinner value labels to the root window
spinnerTextFont = {'family' : 'normal',
                    'weight' : 'bold',
                    'size' : 50}
col = 1
spinnerLabel = []
frame = []
for x in range(3):
    frame.append(Frame(root, borderwidth=1, relief="sunken", bg="white"))
    frame[x].grid(column=col, row=1, rowspan=3, padx=0, pady=2)
    spinnerLabel.append(Label(frame[x], text = spinner.s[x], font=spinnerTextFont, bg="white"))
    spinnerLabel[x].grid(column=col, row=1, rowspan=3, padx=10, pady=10)
    col += 2

# *** section BUTTON

# Start Button Text
startButtonText= "Spin\n\nthe\n\nwheel"
startButtonFont = {'family' : 'normal',
    'weight' : 'bold',
    'size'   : 42}

# function for action when button is clicked
def clicked():  
    startButton["state"] = DISABLED

    # check if credit is enough
    if spinner.credit < 1:
        guidingMessage.configure(text = spinner.actionText[3])
        return
    
    guidingMessage.configure(text = spinner.actionText[1])

    spinner.setInitialValues()

    spinner.rotate(spinnerLabel)

    startButton["state"] = "normal"
    
    guidingMessage.configure(text = spinner.resultMessage()) 
    creditLabel.configure(text="Current Credit: " + str(spinner.credit))
 
# button widget with red color text inside
startButton = Button(root,
                        text = startButtonText,
                        bg="yellow",
                        fg="blue", 
                        font=startButtonFont, 
                        width=5,
                        height=5,
                        command=clicked)
startButton.grid(column=7, row=1, columnspan=7, rowspan=3, sticky="w", padx=2, pady=2)


# Execute Tkinter
root.mainloop()