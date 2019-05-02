import tkinter as tk


class ViewReminderGoalsPage(tk.Frame):
    def __init__(self, context, controller):

        tk.Frame.__init__(self, context)

        lbl = tk.Label(self, text="Your Bill Reminder goals are listed below")
        lbl.pack(pady=10, padx=10)


