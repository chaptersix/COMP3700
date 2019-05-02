import tkinter as tk 
import TigerWallet

class SelectTypePage(tk.Frame):

    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Please check the box of the new goal to create or click cancel.")
        lbl.pack(padx=10, pady=10)

        # add new expense goal checkbox.
        expense_goal_btn = tk.Button(self, text="Add Expense Goal", fg='purple',
                                     command=lambda: controller.show_frame("NewExpenseGoal"))
        expense_goal_btn.pack(pady=10, padx=10)

        # add new savings goal checkbox. var2 performs same as above.
        savings_goal_btn = tk.Button(self, text="Add Savings Goal", fg='green',
                                     command=lambda: controller.show_frame("NewSavingsGoal"))
        savings_goal_btn.pack(pady=10, padx=10)

        # add new bill reminder checkbox. var3 performs same as above.
        bill_reminder_btn = tk.Button(self, text="Add Bill Reminder", fg='blue',
                                      command=lambda: controller.show_frame("NewBillReminder"))
        bill_reminder_btn.pack(pady=10, padx=10)

        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame("AddGoalPage"))
        cancel_btn.pack(pady=10, padx=10)