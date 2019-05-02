import tkinter as tk
import TigerWallet


class NewSavingsGoal(tk.Frame):

    def __init__(self, context, controller):

        savings_goal_list = []
        tk.Frame.__init__(self, context)

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

        instruc_lbl = tk.Label(self, text="After you click the okay button click the Main Menu button")
        instruc.pack()

        clk_ok_btn = tk.Button(self, text="Okay", fg='blue',
                               command=lambda: add_savings_goal(name_entry.get(), goal_amt_entry.get(), exp_date_entry.get()))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Cancel",
                               command=lambda: controller.show_frame("AddGoalPage"))
        cancel_btn.pack(pady=3)

        main_menu_btn = tk.Button(self, text="Main menu")
        main_menu_btn.pack()

        def add_savings_goal(name, goal_amt, exp_date_in):
            name = name
            goal_amount = goal_amt
            exp_date = exp_date_in
            savings_goal_list.append(name)
            savings_goal_list.append(goal_amount)
            savings_goal_list.append(exp_date)

            write_goal(name, goal_amount, exp_date)
            

        def write_goal(name, goal_amt, exp_date_in):
            f = open("database/savingsGList.dat.txt", "a")
            f.writelines([name + "\n" + goal_amt + "\n" + exp_date_in + "\n"])
            f.close()

