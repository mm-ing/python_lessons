# Import Modules
from tkinter import *
import random

class RollTheDiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roll The Dice")

        self.textbox = Entry(root, font=("Arial", 32), justify="center", width=2)
        self.textbox.pack(pady=20)

        self.start_button = Button(root, text="Start", font=("Arial", 16), command=self.start_rolling1)
        self.start_button.pack(pady=10)

        self.rolling = False

    def start_rolling1(self):
        loops = random.randint(5, 10)
        for i in range(loops):
            digit = random.randint(1, 6)
            self.textbox.delete(0, END)
            self.textbox.insert(0, str(digit))
            root.update()
            root.after(100)  # Pause for 100 milliseconds

if __name__ == "__main__":
    root = Tk()
    app = RollTheDiceApp(root)
    root.mainloop()