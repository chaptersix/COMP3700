import tkinter as tk
import CheckingAccountsMenu as cam
import SavingsAccountsMenu as sam


# This class helps to the user to narrow down which account he or she would like to view.


class AccountSelectionMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        instructions_frame = tk.Frame(self)
        instructions_frame.pack()

        # Add text for instructions.
        instructions = tk.Label(instructions_frame, text="Select which accounts you would like to view", fg="black")
        instructions.pack()

        # Initialize other sub-pages of the AccountSelectionMenu
        # tuple containing all active pages
        page_list = (cam.ChecckingAccountsMenu, sam.SavingsAccountsMenu)
        # dictionary mapping frames to the corresponding page names
        self.frames = {}
        # add additional pages to this tuple
        for F in page_list:
            page_name = F.__name__
            frame = F(context=context, controller=self)
            self.frames[page_name] = frame
            # ensures frames are placed in the same location
            frame.grid(row=0, column=0, sticky="nsew")

        # Add options for the user's navigation.
        options_frame = tk.Frame(self)
        options_frame.pack()

        checking_button = tk.Button(options_frame, text="Checking Accounts", fg="black")
        checking_button.grid(row = 0, column = 0)

        savings_button = tk.Button(options_frame, text="Savings Accounts", fg="black")
        savings_button.grid(row = 0, column = 1)

        home_button = tk.Button(options_frame, text="Back Home", fg="black",
                                command=lambda: controller.show_frame("HomePage"))
        home_button.grid(row = 1, columnspan = 2)

        exit_button = tk.Button(options_frame, text="Exit", fg="black", command = quit)
        exit_button.grid(row = 3, columnspan = 2)









