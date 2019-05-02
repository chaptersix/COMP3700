import tkinter as tk
import TigerWallet


class ViewExpenseGoalsPage(tk. Frame):

    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.var_name = tk.StringVar()
        self.var_limit = tk.StringVar()
        self.exp_date = tk.StringVar()
        listbox = tk.Listbox(self)

        lbl = tk.Label(self, text="Your Current Expense Goals are listed below.")
        lbl.pack(pady=10, padx=10)

        f = open("database/expenseGList.dat", "r")
        for line in f.readlines():
            line = line.split()
            self.var_name = line[0]
            listbox.insert(self.var_name)
            listbox.insert(self.var_limit)
            listbox.insert(self.exp_date)
        listbox.pack()

        main_menu_btn = tk.Button(self, text="Main Menu",
                                  command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=3)
