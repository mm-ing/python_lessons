# Import Modules
from tkinter import *
import random

class RockPaperSiccors:
    def __init__(self, root):
        self.root = root

        # root window title and dimension
        self.root.title("Rock Paper Siccor")

        self.canvasWidth = 500
        self.canvasHeight = 500
        self.background = 'yellow'

        # Set geometry (width x height)
        self.root.geometry(f'{self.canvasWidth}x{self.canvasHeight}')

        # create ui content ************************

        self.choices = ["rock", "paper", "scissors"]

        # Label Creation 
        self.start_lbl = Label(root, text = "Choose rock, paper, or scissors: ")
        self.start_lbl.config(font=("Arial", 18)) # Set font and size 
        self.start_lbl.pack(pady=10)

        self.player = Entry(root, font=("Arial", 24), justify="center", width=10)
        self.player.pack(pady=20)

        self.start_button = Button(root, text="Start", font=("Arial", 16), command=self.start_game)
        self.start_button.pack(pady=10)

        self.computer_lbl = Label(root, text = "")
        self.computer_lbl.config(font=("Arial", 18)) # Set font and size
        self.computer_lbl.pack(pady=10) 

        self.result_lbl = Label(root, text = "")
        self.result_lbl.config(font=("Arial", 24)) # Set font and size
        self.result_lbl.pack(pady=10) 

    def start_game(self):
        player_choice = self.player.get().strip().lower()
        computer = random.choice(self.choices)
        self.computer_lbl.config(text=f"Computer chose: {computer}")
        if player_choice == computer:
            self.result_lbl.config(text="It's a tie!")
        elif (player_choice == "rock" and computer == "scissors") or (player_choice == "paper" and computer == "rock") or (player_choice == "scissors" and computer == "paper"):
            self.result_lbl.config(text="You win!")
        elif player_choice in self.choices:
            self.result_lbl.config(text="Computer wins!")
        else:
            self.result_lbl.config(text="Invalid input! Please choose rock, paper, or scissors.")

if __name__ == "__main__":
    # create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
    root = Tk()
    app = RockPaperSiccors(root)
    root.mainloop()
