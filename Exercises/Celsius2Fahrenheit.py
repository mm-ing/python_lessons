# Import Modules
from tkinter import *
class UI_Template:
    def __init__(self, root):
        self.root = root
        # root window title and dimension
        self.root.title("Temparature Converter")
        self.canvasWidth = 300
        self.canvasHeight = 300
        self.background = 'yellow'
        # Set geometry (width x height)
        self.root.geometry(f'{self.canvasWidth}x{self.canvasHeight}')
        # create ui content ************************       

        # Label Creation 
        self.start_lbl = Label(root, text = "Temperatur eingeben:")
        self.start_lbl.config(font=("Arial", 18)) # Set font and size 
        self.start_lbl.pack(pady=10)
        # Entry Creation
        self.celsius_entry = Entry(root, width=5, font=("Arial", 18))
        self.celsius_entry.pack(pady=10)
        # Button Creation
        self.celsius_button = Button(root, text="C2F", font=("Arial", 16), command=self.celsius_to_fahrenheit)
        self.celsius_button.pack(pady=10)
        self.celsius_button = Button(root, text="F2C", font=("Arial", 16), command=self.fahrenheit_to_celsius)
        self.celsius_button.pack(pady=10)
        # Result Label Creation
        self.result_lbl = Label(root, text = "")
        self.result_lbl.config(font=("Arial", 24)) # Set font and size
        self.result_lbl.pack(pady=10) 
    # Function Creation
    def celsius_to_fahrenheit(self):
        # formula to convert Celsius to Fahrenheit\n",
        celsius = float(self.celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        self.result_lbl.config(text=f"{fahrenheit:.2f} °F") 
        self.result_lbl.update()
    def fahrenheit_to_celsius(self):
        # formula to convert Fahrenheit to Celsius\n",
        fahrenheit = float(self.celsius_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        self.result_lbl.config(text=f"{celsius:.2f} °C")
        self.result_lbl.update()

# Only if it is the main module run the code
if __name__ == "__main__":
    # create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
    root = Tk()
    app = UI_Template(root)
    root.mainloop()    