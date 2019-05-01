import tkinter as tk



class CheckingAccountsMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        # Make a frame for the list of the user's checking accounts.
        main_frame = tk.Frame(self)
        main_frame.pack()

        # Add place holder buttons for the user's checking accounts. The buttons will be formatted to contain the text
        # of the account number and the current balance of that account.

        acct_button_1 = tk.Button(main_frame, text = "Checking Account 1", fg = "black")
        acct_button_1.pack()

        acct_button_2 = tk.Button(main_frame, text = "Checking Account 2", fg = "black")
        acct_button_2.pack()

        acct_button_3 = tk.Button(main_frame, text="Checking Account 3", fg="black")
        acct_button_3.pack()

        # Add a return button to go back to the AccountSelectionMenu
        account_select_button = tk.Button(main_frame, text = "Go Back to Account Types", fg = "black",
                                          command=lambda: controller.show_frame("AccountSelectionMenu"))
        account_select_button.pack()

        # Add an exit button for closing the program.
        exit_button = tk.Button(main_frame, text="Exit", fg="black", command=quit)
        exit_button.pack()




