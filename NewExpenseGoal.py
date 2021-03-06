import tkinter as tk
from tkinter import*

# font for labels.
LARGE_FONT = ("Times New Roman", 14)


class NewExpenseGoal(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        expense_goal_list = [] 

        # success label for adding the new goal.
        self.success = tk.Label(self, text="Your new expense goal has been added.")

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

        # Returns you to the Financial goals main menu.
        clk_ok_btn = tk.Button(self, text="Okay",
                               command=lambda: self.add_expense_goal(name_entry.get(),
                                                                monthly_spend_limit_entry.get(), exp_date_entry.get()))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Main Menu",
                               command=lambda: controller.show_frame("AddGoalPage"))
        cancel_btn.pack(pady=3)

        def add_expense_goal(self, name, spend_limit_in, exp_date_in):
            name = name
            spend_limit = spend_limit_in
            exp_date = exp_date_in
            expense_goal_list.append(name)
            expense_goal_list.append(spend_limit)
            expense_goal_list.append(exp_date)

            write_goal(self, name, spend_limit, exp_date)

        def write_goal(self, name, limit, exp_date_in):
            f = open("database/expenseGList.dat", "a")
            f.writelines(["Goal Name: " + name + "\n" + "Monthly Spend Limit: $ "
                                 + limit + "\n" + "Expires On: " + exp_date_in + "\n"])
            f.close()

            self.success.pack(bottom)
           
