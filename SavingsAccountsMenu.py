import tkinter as tk
import TigerWallet
import LoginPage
from BankAccount import BankAccountEntity


class SavingsAccountsMenu(tk.Frame):
    # context = parent
    # controller = TigerWallet object
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.controller = controller

        # Make a frame for the list of the user's checking accounts.
        main_frame = tk.Frame(self)
        main_frame.pack()

        # Get the current user's information.
        current_user = LoginPage.get_current_session()

        # Find the bank accounts associated with this user.
        bank_account_info = BankAccountEntity()
        bank_accounts = bank_account_info.load_account_data()

        buttons = []

        for account in bank_accounts:
            owner = account[0]
            user = account[1]
            account_number = account[2]
            account_type = account[3]
            balance = account[4]
            if current_user.get_username() == user and account_type == "savings":
                savings_account = tk.Button(main_frame, text="Account Number: " + account_number
                                                              + " Balance: $" + balance, fg="black")
                buttons.append(savings_account)

        for button in buttons:
            button.pack()

        # Add a return button to go back to the AccountSelectionMenu
        account_select_button = tk.Button(main_frame, text = "Go Back to Account Types", fg = "black",
                                          command=lambda: controller.show_frame("AccountSelectionMenu"))
        account_select_button.pack()

        # Add an exit button for closing the program.
        exit_button = tk.Button(main_frame, text="Exit", fg="black", command=quit)
        exit_button.pack()