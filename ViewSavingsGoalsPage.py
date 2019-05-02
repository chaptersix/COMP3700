import tkinter as tk
import TigerWallet


class ViewSavingsGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.name = tk.StringVar()
        self.goal_amt = tk.StringVar()
        self.exp_date= tk.StringVar()
        listbox = tk.Listbox(self)

        lbl = tk.Label(self, text="Your current savings goal are listed below.")
        lbl.pack(pady=10, padx=10)

        f = open("database/savingsGList.dat.txt", "r")
        for line in f.readlines():
             line = line.split()
             self.var_name = line[0]
             self.goal_amt = line[1]
             self.exp_date = line[2]
             listbox.insert(self.name)
             listbox.insert(self.notify_day)
             listbox.insert(self.exp_date)
        listbox.pack()




