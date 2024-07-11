# *** UI for a Slot Machine Game ***
# Initial
# credit balance: 10
# Text: "Try your luck!"
# Button: "Spin the wheel"
# Action: All wheels spin 10 times, than first stop. Next 10 times loop, than second stop. Next 10 times loop, than third stop.
# Rewards: 2xeqal no -> +1, 3x equal no -> +5, 3x 7 -> +10 otherwise -1
# Text: "You won x credits!" or "You lost x credit!"
# Option: for each spin stop-button

# *** section Import

import tkinter as tk
from slot_machine_data import Spinner
from logging import Logger

# *** section button INITIALIZATION

class BUTTON:
    def __init__(self, root, data_model, worker_name) -> None:
        self.data_model = data_model
        self.worker_name = worker_name        

        # Start Button Text
        self.Text= "Spin\n\nthe\n\nwheel"
        self.Font = {'family' : 'normal',
                        'weight' : 'bold',
                        'size'   : 42}

        # button widget with red color text inside
        self.button = tk.Button(root,
                        text=self.Text,
                        bg="yellow",
                        fg="blue", 
                        font=self.Font, 
                        width=5,
                        height=5,
                        command=self.start)
        self.button["state"] = "normal"
        self.button.grid(column=7, row=1, columnspan=7, rowspan=3, sticky="w", padx=2, pady=2)

    # function for action when button is clicked
    def start(self):
        self.button["state"] = tk.DISABLED
        self.data_model.workers[self.worker_name].start_worker()

    def stop(self):
        self.data_model.workers[self.worker_name].stop_worker()
        self.button["state"] = tk.NORMAL

    def reset(self):
        self.button["state"] = tk.NORMAL

# *** section gui INITIALIZATION

class GUI:
    def __init__(self, data_model: Spinner):
        self.data_model = data_model

        # *** UI: create root window    Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
        self.root = tk.Tk() 
        # root window title and dimension
        self.root.title("Lucky No 7")
        # Set geometry (width x height)
        self.root.geometry('350x250')

        # initialize the UI controls
        self.initialize()

    def initialize(self):
        self.data_model.setInitialValues()        

        # define grid size
        col_count = 10
        row_count = 6

        for col in range(col_count):
            self.root.grid_columnconfigure(col, minsize=30)

        for row in range(row_count):
            self.root.grid_rowconfigure(row, minsize=30)

        #credit label
        self.creditTextFont = {'family' : 'normal',
                            'weight' : 'bold',
                            'size' : 32}
        self.creditLabel = tk.Label(self.root, text="Current Credit: " + str(self.data_model.credit), font=self.creditTextFont)
        self.creditLabel.grid(column=1, row=0, columnspan=10, padx=2, pady=5)

        # adding a message to the root window
        self.guidingTextFont = {'family' : 'normal',
                            'weight' : 'bold',
                            'size' : 24}
        self.guidingMessage = tk.Message(self.root, text = self.data_model.message, width=320, font=self.guidingTextFont)
        self.guidingMessage.grid(column=0, columnspan=10, row=4, rowspan=2, padx=2, pady=10)

        # adding spinner value labels to the root window
        self.spinnerTextFont = {'family' : 'normal',
                            'weight' : 'bold',
                            'size' : 50}
        col = 1
        self.spinnerLabels = []
        frame = []
        for x in range(3):
            frame.append(tk.Frame(self.root, borderwidth=1, relief="sunken", bg="white"))
            frame[x].grid(column=col, row=1, rowspan=3, padx=0, pady=2)
            self.spinnerLabels.append(tk.Label(frame[x], text = self.data_model.slots[x], font=self.spinnerTextFont, bg="white"))
            self.spinnerLabels[x].grid(column=col, row=1, rowspan=3, padx=10, pady=10)
            col += 2
        
        # adding button
        self.button = BUTTON(self.root, self.data_model, 'slot_machine_worker')

        self.data_model.update_slots = self.update_slots

        self.data_model.update_credit = self.update_credit

        self.data_model.update_message = self.update_message

        # bind the close event to the shutdown method
        self.root.protocol("WM_DELETE_WINDOW", self.shutdown)


    def update_slots(self):
        # update the spinner labels
        for i in range(3):    
            self.spinnerLabels[i].configure(text = self.data_model.slots[i])
            self.spinnerLabels[i].update()    

    def update_message(self):
        self.guidingMessage.configure(text = self.data_model.message)
        self.guidingMessage.update()

    def update_credit(self):
        self.creditLabel.configure(text = "Current Credit: " + str(self.data_model.credit))
        self.creditLabel.update()
        self.button.reset()
    
    def shutdown(self):
        self.data_model.shutdown = True
        self.data_model.stop_workers()
        self.root.destroy()
