# Import Modules
from tkinter import *
from Fruit_cls import Fruits  # Import Fruits class from Fruit_cls.py

canvasWidth = 500
canvasHeight = 250
background = 'yellow'
 
# create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
root = Tk()
 
# root window title and dimension
root.title("Fruit App")
# Set geometry (width x height)
root.geometry(f'{canvasWidth}x{canvasHeight}')

# create fruits instance
myfruits = Fruits()

# Start
# Label Creation 
start_lbl = Label(root, text = "Bitte Frucht auswählen")
start_lbl.config(font=("Courier", 16)) # Set font and size 
start_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=W)

# Dropdown menu options
fruits = myfruits.getFruits().split(', ')  # Get list of fruits from the class

# Variable to store selected fruit
selected_fruit = StringVar(root)
selected_fruit.set(fruits[0])  # set default value

# Create dropdown menu
fruit_dropdown = OptionMenu(root, selected_fruit, *fruits)
fruit_dropdown.config(font=("Courier", 18))
fruit_dropdown.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=W)

# Common label
# Label Creation
common_lbl = Label(root, text = "")
common_lbl.config(font=("Courier", 18)) # Set font and size
common_lbl.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# price function
def fruit_price():
    # get the price of the selected fruit
    price = myfruits.getPrice(selected_fruit.get())
    common_lbl.config(text = f"{price}") # Set text of common label

# Button Creation
start_btn = Button(root, text="GET PRICE", command=fruit_price)
start_btn.config(font=("Courier", 18)) # Set font and size
start_btn.grid(row=1, column=3, columnspan=3, padx=10, pady=10)

root.mainloop() # Execute Tkinter event loop