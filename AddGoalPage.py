import tkinter as tk
import TigerWallet

class AddGoalPage(tk.Frame):

    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Welcome to the TigerWallet Financial Goals Menu!")
        lbl.pack(pady=10, padx=10)

        add_btn = tk.Button(self, text='Add Financial Goal',
                            command=lambda: controller.show_frame("SelectTypePage"))
        add_btn.pack(padx=10, pady=10)

        # view current expense goals
        view_expense_btn = tk.Button(self, Text="View Current Expense Goals",
                                     command=lambda: controller.show_frame("ViewExpenseGoalsPage"))
        view_expense_btn.pack(pady=10, padx=10)

        view_savings_btn = tk.Button(self, Text="View Current Expense Goals",
                                     command=lambda: controller.show_frame("ViewSavingsGoalsPage"))
        view_savings_btn.pack(pady=10, padx=10)

        view_reminders_btn = tk.Button(self, Text="View Current Expense Goals",
                                       command=lambda: controller.show_frame("ViewReminderGoalsPage"))
        view_reminders_btn.pack(pady=10, padx=10)

        home_btn = tk.Button(self, text="Main Menu", command=lambda: controller.show_frame("MainMenu"))
        home_btn.pack(pady=10, padx=10)
