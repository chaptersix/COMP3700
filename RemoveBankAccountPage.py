import tkinter as tk
import LoginPage
from BankAccount import BankAccountController

class RemoveBankAccountPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        # member username_password_map
        # store user data in user_data during execution
        # current user is a User object
        self.BankController = BankAccountController()
        # unsuccessful account notification
        self.unsuccessful1 = tk.Label(self, text="Unsuccesful. The account number you entered does not exist")
        # successful account notification
        self.successful = tk.Label(self, text="Success! You have removed a bank account from your TigerWallet account.")

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

        self.lbl = tk.Label(welcome_frame, text="Remove a Bank Account from Your TigerWallet Account!")
        self.lbl.pack()

        m_text = tk.StringVar()
        m_text.set("Enter the corresponding Account Number for the Account You Wish to Remove.")
        self.lbl = tk.Label(welcome_frame, textvariable=m_text)
        self.lbl.pack()


        # get account_number
        account_number_label = tk.Label(account_number_frame, text="Account Number:", height=4)
        account_number_label.pack(side="left")
        self.account_number = tk.Entry(account_number_frame, width=15)
        self.account_number.pack(side="left")


        # navigation buttons
        remove_button = tk.Button(navigation_frame, text="Remove Account",
                                command=lambda: on_remove(self))
        remove_button.pack()

        return_button = tk.Button(navigation_frame, text="Back",
                                command=lambda: controller.show_frame("ManageBankAccountPage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit",
                                command=quit)
        exit_button.pack()

        def on_remove(self):
            self.unsuccessful1.pack_forget()
            self.successful.pack_forget()
            if self.BankController.remove_account( self.account_number.get(), LoginPage.get_current_session().get_username()):
                self.successful.pack()
                return
            self.unsuccessful1.pack()