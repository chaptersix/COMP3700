import tkinter as tk 
import TigerWallet
import LoginPage

class ManageBankAccountPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)


        # unsuccessful account notification 
        self.unsuccessful1 = tk.Label(self, text="Unsuccesful. The account number you entered is already in use.")
        # successful account notification 
        self.successful = tk.Label(self, text="Success! You have added a bank account to your TigerWallet account.")

        # break up layout into multiple sub frames 
        welcome_frame = tk.Frame(self)
        welcome_frame.pack()
        select_bank_frame = tk.Frame(self)
        select_bank_frame.pack()
        account_number_frame = tk.Frame(self)
        account_number_frame.pack()

        navigation_frame = tk.Frame(self) 
        navigation_frame.pack()

        self.controller = controller

        self.lbl = tk.Label(welcome_frame, text="Manage Your Bank Accounts within TigerWallet!")
        self.lbl.pack()

        # navigation buttons
        add_button = tk.Button(navigation_frame, text="Add an Account", 
                                command=lambda: controller.show_frame("AddBankAccountPage"))
        add_button.pack()

        add_button = tk.Button(navigation_frame, text="Remove an Account", 
                                command=lambda: controller.show_frame("RemoveBankAccountPage"))
        add_button.pack()

        return_button = tk.Button(navigation_frame, text="Return to Main Menu", 
                                command=lambda: controller.show_frame("MainMenu"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit", 
                                command=quit)
        exit_button.pack()

