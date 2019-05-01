class BillReminders():
    def __init__(self, name, notify_date, exp_date):
        self.name = name
        self.notification_date = notify_date
        self.exp_date = exp_date

    # in order for this to be persistent across sessions and users, 
    # goals should be written to a file associated with a username    
    bill_reminders_list = []