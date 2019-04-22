import tkinter as tk

# font for labels.
LARGE_FONT = ("Times New Roman", 14)


class FinancialGoalController(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (AddGoalPage, SelectTypePage, NewExpenseGoal, NewSavingsGoal, NewBillReminder):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AddGoalPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class AddGoalPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text="Welcome to the TigerWallet Financial Goals Menu!", fg='blue',
                       font=LARGE_FONT)
        lbl.pack(pady=10, padx=10)

        add_btn = tk.Button(self, text='Add Financial Goal', fg='blue',
                            command=lambda: controller.show_frame(SelectTypePage))
        add_btn.pack(padx=10, pady=10)

        view_expense_goal_btn = tk.Button(self, text="View Your Expense Goals", fg='orange',
                                          command=lambda: controller.show_frame(ExpenseGoals))
        view_expense_goal_btn.pack(pady=10, padx=10)

        view_savings_goal_btn = tk.Button(self, text="View Your Savings Goals", fg='green',
                                          command=lambda: controller.show_frame(SavingsGoals))
        view_savings_goal_btn.pack(pady=10, padx=10)

        view_bill_reminders_btn = tk.Button(self, text="View Your Bill Reminders", fg='teal',
                                            command=lambda: controller.show_frame(BillReminders))
        view_bill_reminders_btn.pack(pady=10, padx=10)

        home_btn = tk.Button(self, text="Main Menu", command=lambda: controller.show_frame(AddGoalPage))
        home_btn.pack(pady=10, padx=10)


class SelectTypePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text="Please check the box of the new goal to create or click cancel.",
                       fg='blue', font=LARGE_FONT)
        lbl.pack(padx=10, pady=10)

        # add new expense goal checkbox.
        expense_goal_btn = tk.Button(self, text="Add Expense Goal", fg='purple',
                                     command=lambda: controller.show_frame(NewExpenseGoal))
        expense_goal_btn.pack(pady=10, padx=10)

        # add new savings goal checkbox. var2 performs same as above.
        savings_goal_btn = tk.Button(self, text="Add Savings Goal", fg='green',
                                     command=lambda: controller.show_frame(NewSavingsGoal))
        savings_goal_btn.pack(pady=10, padx=10)

        # add new bill reminder checkbox. var3 performs same as above.
        bill_reminder_btn = tk.Button(self, text="Add Bill Reminder", fg='blue',
                                      command=lambda: controller.show_frame(NewBillReminder))
        bill_reminder_btn.pack(pady=10, padx=10)

        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame(AddGoalPage))
        cancel_btn.pack(pady=10, padx=10)


class NewExpenseGoal(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        frame1 = tk.Frame(self)
        frame1.pack(fill='x')

        name_lbl = tk.Label(frame1, text="Goal Name:", width=9)
        name_lbl.pack(side='left', padx=5, pady=5)
        name_entry = tk.Entry(frame1)
        name_entry.pack(fill='x', padx=5, expand=True)

        frame2 = tk.Frame(self)
        frame2.pack(fill='x')

        monthly_spend_limit_lbl = tk.Label(frame2, text="Monthly Spending Limit:", width=18)
        monthly_spend_limit_lbl.pack(side='left', padx=5, pady=5)
        monthly_spend_limit_entry = tk.Entry(frame2)
        monthly_spend_limit_entry.pack(fill='x', padx=5, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack(fill='both', expand=True)

        exp_date_lbl = tk.Label(frame3, text="Specify Time Limit/EXP date(mm/dd/yyyy):", width=32)
        exp_date_lbl.pack(side='left', padx=5, pady=5)
        exp_date_entry = tk.Entry(frame3)
        exp_date_entry.pack(fill='x', padx=5, expand=True)

        # need to change this to command that will add the new goal to this list.
        # we can do this after the merge.
        clk_ok_btn = tk.Button(self, text="Okay", fg='blue',
                               command=lambda: controller.show_frame(AddGoalPage))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financail goals main menu.
        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame(AddGoalPage))
        cancel_btn.pack(pady=3)


class NewSavingsGoal(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        frame1 = tk.Frame(self)
        frame1.pack(fill='x')

        name_lbl = tk.Label(frame1, text="Goal Name:", width=9)
        name_lbl.pack(side='left', padx=5, pady=5)
        name_entry = tk.Entry(frame1)
        name_entry.pack(fill='x', padx=5, expand=True)

        frame2 = tk.Frame(self)
        frame2.pack(fill='x')

        goal_amt_lbl = tk.Label(frame2, text="Savings Goal Amount:", width=16)
        goal_amt_lbl.pack(side='left', padx=5, pady=5)
        goal_amt_entry = tk.Entry(frame2)
        goal_amt_entry.pack(fill='x', padx=5, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack(fill='both', expand=True)

        exp_date_lbl = tk.Label(frame3, text="Specify Time Limit/EXP date(mm/dd/yyyy):", width=32)
        exp_date_lbl.pack(side='left', padx=5, pady=5)
        exp_date_entry = tk.Entry(frame3)
        exp_date_entry.pack(fill='x', padx=5, expand=True)

        # need to change this to command that will add the new goal to this list.
        # we can do this after the merge.
        clk_ok_btn = tk.Button(self, text="Okay", fg='blue',
                               command=lambda: controller.show_frame(AddGoalPage))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame(AddGoalPage))
        cancel_btn.pack(pady=3)


class NewBillReminder(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        frame1 = tk.Frame(self)
        frame1.pack(fill='x')

        name_lbl = tk.Label(frame1, text="Reminder Name:", width=12)
        name_lbl.pack(side='left', padx=5, pady=5)
        name_entry = tk.Entry(frame1)
        name_entry.pack(fill='x', padx=5, expand=True)

        frame2 = tk.Frame(self)
        frame2.pack(fill='x')

        notify_day_lbl = tk.Label(frame2, text="Monthly Notification Day(0-31):", width=23)
        notify_day_lbl.pack(side='left', padx=5, pady=5)
        notify_day_entry = tk.Entry(frame2)
        notify_day_entry.pack(fill='x', padx=5, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack(fill='both', expand=True)

        exp_date_lbl = tk.Label(frame3, text="Specify Time Limit/EXP date(mm/dd/yyyy):", width=32)
        exp_date_lbl.pack(side='left', padx=5, pady=5)
        exp_date_entry = tk.Entry(frame3)
        exp_date_entry.pack(fill='x', padx=5, expand=True)

        # need to change this to command that will add the new goal to this list.
        # we can do this after the merge.
        clk_ok_btn = tk.Button(self, text="Okay", fg='blue',
                               command=lambda: controller.show_frame(AddGoalPage))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame(AddGoalPage))
        cancel_btn.pack(pady=3)


class ExpenseGoals(object):

    def __init__(self, name, spend_limit, exp_date):
        self.name = name
        self.spend_limit = spend_limit
        self.exp_date = exp_date

    expense_goal_lst = []


class SavingsGoals(object):
    def __init__(self, name, goal_amt, exp_date):
        self.name = name
        self.goal_amount = goal_amt
        self.exp_date = exp_date

    savings_goals_lst = []


class BillReminders(object):
    def __init__(self, name, notify_date, exp_date):
        self.name = name
        self.notification_date = notify_date
        self.exp_date = exp_date

    bill_reminders_lst = []


app = FinancialGoalController()
app.mainloop()
