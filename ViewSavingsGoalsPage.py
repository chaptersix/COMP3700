import tkinter as tk


class ViewSavingsGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.name = tk.StringVar()
        self.goal_amt = tk.StringVar()
        self.exp_date = tk.StringVar()

        lbl = tk.Label(self, text="Your Current Savings Goals are listed below.")
        lbl.pack(pady=10, padx=10)

        listbox = tk.Listbox(self)

        f = open("database/savingsGList.dat", "r")
        for line in f.readlines():
            if ("database/savingsGList" == None):
                self.empty = tk.StringVar()
                empty_lbl = tk.Label(self, text="Savings Goal list is empty")
                empty_lbl.pack()
            line = line.split()
            self.var_name = line[0]
            self.goal_amt = line[1]
            self.exp_date = line[2]
            listbox.insert(self.var_name)
            listbox.insert(self.goal_amt)
            listbox.insert(self.exp_date)
        listbox.pack()

        main_menu_btn = tk.Button(self, text="Main Menu", fg='blue',
                                  command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=3)


