import tkinter as tk
import LoginPage
from BankAccount import BankAccountController


class AddBankAccountPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        # member username_password_map
        # store user data in user_data during execution
        # current user is a User object
        self.BankController = BankAccountController()

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

        self.lbl = tk.Label(welcome_frame, text="Add a Bank Account to Your TigerWallet Account!")
        self.lbl.pack()

        m_text = tk.StringVar()
        m_text.set("Choose a Supported Bank and Enter Your Account Number.")
        self.lbl = tk.Label(welcome_frame, textvariable=m_text)
        self.lbl.pack()

        # get bank
        bank_label = tk.Label(select_bank_frame, text="Name of Bank:", height=4)
        bank_label.pack(side="left")
        self.bank = tk.Entry(select_bank_frame, width=15)
        self.bank.pack(side="left")

        # get account_number
        account_number_label = tk.Label(account_number_frame, text="Account Number:", height=4)
        account_number_label.pack(side="left")
        self.account_number = tk.Entry(account_number_frame, width=15)
        self.account_number.pack(side="left")


        # navigation buttons
        add_button = tk.Button(navigation_frame, text="Add Account",
                                command=lambda: on_add(self))
        add_button.pack()

        return_button = tk.Button(navigation_frame, text="Back",
                                command=lambda: controller.show_frame("ManageBankAccountPage"))
        return_button.pack()

        exit_button = tk.Button(navigation_frame, text="Exit",
                                command=quit)
        exit_button.pack()

        def on_add(self):
            self.unsuccessful1.pack_forget()
            self.successful.pack_forget()
            if self.BankController.add_account(self.bank.get(), self.account_number.get(), LoginPage.get_current_session().get_username()):
                self.successful.pack()
                return
            self.unsuccessful1.pack()