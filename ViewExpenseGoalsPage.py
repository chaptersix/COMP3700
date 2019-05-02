import tkinter as tk


class ViewExpenseGoalsPage(tk. Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.name = tk.StringVar()
        self.monthly_limit = tk.StringVar()
        self.exp_date= tk.StringVar()
        listbox = tk.Listbox(self)

        lbl = tk.Label(self, text="Your current Expense Goals are listed below.")
        lbl.pack(pady=10, padx=10)

        f = open("database/expenseGList.dat.txt", "r")
        for line in f.readlines():
             line = line.split()
             self.var_name = line[0]
             self.monthly_limit = line[1]
             self.exp_date = line[2]
             listbox.insert(self.name)
             listbox.insert(self.notify_day)
             listbox.insert(self.exp_date)
        listbox.pack()