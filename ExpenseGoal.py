class ExpenseGoals():
    def __init__(self, name, spend_limit, exp_date):
        self.name = name
        self.spend_limit = spend_limit
        self.exp_date = exp_date

    # in order for this to be persistent across sessions and users, 
    # goals should be written to a file associated with a username
    expense_goal_list = []