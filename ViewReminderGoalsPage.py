import tkinter as tk
import TigerWallet


class ViewReminderGoalsPage(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        self.name = tk.StringVar()
        self.notify_day = tk.StringVar()
        self.exp_date = tk.StringVar()
        listbox = tk.Listbox(self)

        lbl = tk.Label(self, text="Your Current Bill Reminder goals are listed below.")
        lbl.pack(pady=10, padx=10)

        f = open("database/billReminderList.dat", "r")
        for line in f.readlines():
            line = line.split()
            self.var_name = line[0]
            self.notify_day = line[1]
            self.exp_date = line[2]
            listbox.insert(self.name)
            listbox.insert(self.notify_day)
            listbox.insert(self.exp_date)
        listbox.pack()

        main_menu_btn = tk.Button(self, text="Main Menu",
                                  command=lambda: controller.show_frame("AddGoalPage"))
        main_menu_btn.pack(pady=3)

