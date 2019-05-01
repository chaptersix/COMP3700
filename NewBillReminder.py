import tkinter as tk

class NewBillReminder(tk.Frame):
    def __init__(self, context, controller):
        tk.Frame.__init__(self, context)

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
                               command=lambda: controller.show_frame("AddGoalPage"))
        clk_ok_btn.pack(pady=3)

        # takes you back to the tigerWallet financial goals main menu.
        cancel_btn = tk.Button(self, text="Cancel", fg='red',
                               command=lambda: controller.show_frame("AddGoalPage"))
        cancel_btn.pack(pady=3)