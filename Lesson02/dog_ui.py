# Import Module
from tkinter import *  # Import all tkinter constants
from tkinter.constants import W  # Import W for grid sticky parameter
# import pillow
from PIL import ImageTk, Image
import os
from dog_cls import dog  # Import dog class from dog_cls.py

canvasWidth = 600
canvasHeight = 800
background = 'yellow'

# Get the working directory of the script
working_path = os.path.dirname(os.path.abspath(__file__))
# print(f"Working Path: {working_path}")

waving_hand_path = working_path + '/waving_hand.png' # path for image
dog_path = working_path + '/dog.png' # path for image
dog_barking_path = working_path + '/dog_barking.png'
dog_feeding_path = working_path + '/dog_feeding.jpg'
dog_sleeping_path = working_path + '/dog_sleeping.png'

# create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Mein Hund")
# Set geometry (width x height)
root.geometry(f'{canvasWidth}x{canvasHeight}')

# Grid.columnconfigure(root, 2, weight=1, minsize=5)
# Grid.rowconfigure(root, 1, weight=1, minsize=5)
for col in range(7):
    root.grid_columnconfigure(col, minsize=25, weight=1)
# Name
# Label Creation 
name_lbl = Label(root, text = "Hundename:")
name_lbl.config(font=("Courier", 14)) # Set font and size 
name_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)

# TextBox Creation 
name_input = Text(root, height = 2, width = 20, font=("Courier", 22))   
name_input.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

# Age
# Label Creation
age_lbl = Label(root, text = "Alter:")
age_lbl.config(font=("Courier", 14)) # Set font and size 
age_lbl.grid(row=1, column=0, columnspan=2, padx=10, pady=10) 

# TextBox Creation 
age_input = Text(root, height = 2, width = 10, font=("Courier", 18))   
age_input.grid(row=1, column=2, columnspan=1, padx=10, pady=10) 

# Energy
# Label Creation
energy_lbl = Label(root, text = "Energie:")
energy_lbl.config(font=("Courier", 14)) # Set font and size
energy_lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

energy_value_lbl = Label(root, text = "100")
energy_value_lbl.config(font=("Courier", 14)) # Set font and size
energy_value_lbl.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

# Common label
# Label Creation
common_lbl = Label(root, text = "Bitte starten!")
common_lbl.config(font=("Courier", 18)) # Set font and size
common_lbl.grid(row=3, column=0, columnspan=7, padx=10, pady=10)

# Create a dog object
myDog = dog("Bello", 3) # Create a dog object

# set common image
img = ImageTk.PhotoImage(Image.open(waving_hand_path))
panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(row=6, column=0, columnspan=7, padx=10, pady=10)

def dog_starts():
    inpName = name_input.get(1.0, "end-1c")
    inpAge = age_input.get(1.0, "end-1c")    
    myDog = dog(inpName, inpAge) # Create a dog object
    common_lbl.config(text = f"{myDog}") # Set text of common label

    img = ImageTk.PhotoImage(Image.open(dog_path))
    panel = Label(root, image = img)
    panel.grid(row=6, column=0, columnspan=7, padx=10, pady=10)

def dog_barks():    
    common_lbl.config(text = f"{myDog.bark()}") # Set text of common label   
    energy_value_lbl.config(text = f"{myDog.energy}") # Set text of energy label 
    img = ImageTk.PhotoImage(Image.open(dog_barking_path))
    panel = Label(root, image = img)
    panel.grid(row=6, column=0, columnspan=7, padx=10, pady=10)

def dog_naps():        
    common_lbl.config(text = f"{myDog.nap()}") # Set text of common label
    energy_value_lbl.config(text = f"Energie: {myDog.energy}") # Set text of energy label
    img = ImageTk.PhotoImage(Image.open(dog_sleeping_path))
    panel = Label(root, image = img)
    panel.grid(row=6, column=0, columnspan=7, padx=10, pady=10)

def dog_feeds():
    common_lbl.config(text = f"{myDog.feed()}") # Set text of common label
    energy_value_lbl.config(text = f"Energie: {myDog.energy}") # Set text of energy label
    img = ImageTk.PhotoImage(Image.open(dog_feeding_path))
    panel = Label(root, image = img)
    panel.grid(row=6, column=0, columnspan=7, padx=10, pady=10)

 
# Button Creation 
startButton = Button(root, text = "START", command = dog_starts) 
startButton.grid(row=4, column=0, columnspan=2, padx=10, pady=10) 
  
barkButton = Button(root, text = "B E L L E N", command = dog_barks) 
barkButton.grid(row=4, column=2, columnspan=2, padx=10, pady=10) 

napButton = Button(root, text = "S C H L A F E N", command = dog_naps) 
napButton.grid(row=4, column=4, columnspan=2, padx=10, pady=10) 

feedButton = Button(root, text = "F Ü T T E R N", command = dog_feeds) 
feedButton.grid(row=4, column=6, columnspan=2, padx=10, pady=10) 
  

root.mainloop() # Execute Tkinter