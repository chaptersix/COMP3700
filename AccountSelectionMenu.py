import tkinter as tk


# This class helps to the user to narrow down which account he or she would like to view.


class AccountSelectionMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        options_frame = tk.Frame(self)
        options_frame.pack()

        # Add text for instructions.
        instructions = tk.Label(options_frame, text="Select which accounts you would like to view", fg="black")
        instructions.pack()

        checking_button = tk.Button(options_frame, text="Checking Accounts", fg="black")
        checking_button.pack(side="left")
        savings_button = tk.Button(options_frame, text="Savings Accounts", fg="black")
        savings_button.pack(side="left")

        # Make a frame for the home button and for the exit button.

        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side="bottom")
        home_button = tk.Button(bottom_frame, text="Back Home", fg="black")
        home_button.pack()

        exit_button = tk.Button(bottom_frame, text="Exit", fg="black", command = quit)
        exit_button.pack()









