# Import Modules
from tkinter import *
class UI_Template:
    def __init__(self, root):
        self.root = root
        # root window title and dimension
        self.root.title("UI Template")
        self.canvasWidth = 500
        self.canvasHeight = 500
        self.background = 'yellow'
        # Set geometry (width x height)
        self.root.geometry(f'{self.canvasWidth}x{self.canvasHeight}')

        # create ui content ************************

        # Label Creation 
        self.start_lbl = Label(root, text = "Sample Label")
        self.start_lbl.config(font=("Arial", 18)) # Set font and size 
        self.start_lbl.pack(pady=10)
        # Entry Creation
        self.user_entry = Entry(root, width=5, font=("Arial", 18))
        self.user_entry.pack(pady=10)
        # Button Creation
        self.start_button = Button(root, text="Start", font=("Arial", 16), command=self.start)
        self.start_button.pack(pady=10)
        # Result Label Creation
        self.result_lbl = Label(root, text = "")
        self.result_lbl.config(font=("Arial", 24)) # Set font and size
        self.result_lbl.pack(pady=10) 
    # Function Creation
    def start(self):
        userEntry = self.user_entry.get()
        self.result_lbl.config(text=f"UI started! {userEntry}")
        self.result_lbl.update()
# Only if it is the main module run the code
if __name__ == "__main__":
    # create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
    root = Tk()
    app = UI_Template(root)
    root.mainloop()
