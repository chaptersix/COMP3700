import tkinter as tk
from BankAccount import BankAccountEntity
import LoginPage
import User


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

        # Add options for the user's navigation.
        options_frame = tk.Frame(self)
        options_frame.pack()

        # Determine what accounts are associated with the user.
        # Get the current user's information.

        current_user = LoginPage.get_current_session()

        print("From AccountSelctionMenu current user is: " + current_user.get_username())

        # Find the bank accounts associated with this user.
        bank_account_info = BankAccountEntity()
        bank_accounts = bank_account_info.load_account_data()

        checking_accounts = []
        savings_accounts = []

        for account in bank_accounts:
            owner = account[0]
            user = account[1]
            account_number = account[2]
            account_type = account[3]
            balance = account[4]

            if current_user.get_username() == user and account_type == "checking":
                checking_accounts.append([owner, user, account_number, balance])
            if current_user.get_username() == user and account_type == "savings":
                savings_accounts.append([owner, user, account_number, balance])

        # Determine which buttons will be displayed. Checking Accounts Button, Savings Accounts Button, or both.

        no_checking_notification = tk.Label(options_frame, text = "You have no checking accounts!", fg = "black")
        no_savings_notification = tk.Label(options_frame, text="You have no savings account!", fg="black")

        if len(checking_accounts) == 0:
            no_checking_notification.pack()

        if len(checking_accounts) > 0:
            checking_button = tk.Button(options_frame, text="Checking Accounts", fg="black",
                                        command=lambda: controller.show_frame("CheckingAccountsMenu"))
            checking_button.pack()

        if len(savings_accounts) == 0:
            no_savings_notification.pack()

        if len(savings_accounts) > 0:
            savings_button = tk.Button(options_frame, text="Savings Accounts", fg="black",
                                       command=lambda: controller.show_frame("SavingsAccountsMenu"))
            savings_button.pack()

        home_button = tk.Button(options_frame, text="Return to Main Menu", fg="black",
                                command=lambda: controller.show_frame("MainMenu"))
        home_button.pack()

        exit_button = tk.Button(options_frame, text="Exit", fg="black", command = quit)
        exit_button.pack()









