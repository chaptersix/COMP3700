import tkinter as tk
from tkinter import*
import TigerWallet


class NewBillReminder(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

        # success label for adding a new bill reminder.
        self.success = tk.Label(self, text="Your new Bill Reminder has been added.")

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

        bill_reminder_list = []

        # takes you back to the Financial goals main menu.
        clk_ok_btn = tk.Button(self, text="Okay", 
                               command=lambda: self.add_bill_reminder_goal(name_entry.get(),
                                                                      notify_day_entry.get(), exp_date_entry.get()))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Main Menu",
                               command=lambda: controller.show_frame("AddGoalPage"))
        cancel_btn.pack(pady=3)

        def add_bill_reminder_goal(self, name, notify_day_in, exp_date_in):
            name = name
            notify_day = notify_day_in
            exp_date = exp_date_in
            bill_reminder_list.append(name)
            bill_reminder_list.append(notify_day)
            bill_reminder_list.append(exp_date)

            write_goal(self, name, notify_day, exp_date)

        def write_goal(self, name, notify_day, exp_date_in):
            f = open("database/billReminderList.dat", "a")
            f.writelines(["Goal Name: " + name + "\n" + "Notification Data: $ " 
                                + notify_day + "\n" + "Expires On: " + exp_date_in + "\n"])
            f.close()

            self.success.pack(bottom)
