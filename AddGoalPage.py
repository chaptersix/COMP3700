import tkinter as tk

class AddGoalPage(tk.Frame):

    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Welcome to the TigerWallet Financial Goals Menu!")
        lbl.pack(pady=10, padx=10)

        add_btn = tk.Button(self, text='Add Financial Goal', fg='blue',
                            command=lambda: controller.show_frame("SelectTypePage"))
        add_btn.pack(padx=10, pady=10)

        view_expense_goal_btn = tk.Button(self, text="View Your Expense Goals",
                                          command=lambda: controller.show_frame("ExpenseGoals"))
        view_expense_goal_btn.pack(pady=10, padx=10)

        view_savings_goal_btn = tk.Button(self, text="View Your Savings Goals",
                                          command=lambda: controller.show_frame("SavingsGoals"))
        view_savings_goal_btn.pack(pady=10, padx=10)

        view_bill_reminders_btn = tk.Button(self, text="View Your Bill Reminders",
                                            command=lambda: controller.show_frame("BillReminders"))
        view_bill_reminders_btn.pack(pady=10, padx=10)

        home_btn = tk.Button(self, text="Return to Main Menu", command=lambda: controller.show_frame("MainMenu"))
        home_btn.pack(pady=10, padx=10)